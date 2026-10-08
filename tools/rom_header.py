#!/usr/bin/env python3
"""Inspect a SNES ROM: copier header, internal header, map mode, checksum, hashes.

Usage:
    tools/rom_header.py baserom/baserom.sfc
    tools/rom_header.py baserom/baserom.sfc --json
    tools/rom_header.py baserom/baserom.sfc --strip baserom/headerless.sfc
    tools/rom_header.py baserom/baserom.sfc --expect-sha1-file rom.sha1

Hashes are always computed over the headerless image (copier header removed).
Exit codes: 0 ok, 2 no plausible SNES header found, 3 SHA-1 mismatch.
"""
import argparse
import hashlib
import json
import sys
import zlib
from pathlib import Path

COPIER_HEADER_SIZE = 0x200
LAYOUTS = {"LoROM": 0x7FC0, "HiROM": 0xFFC0, "ExHiROM": 0x40FFC0}
# Low nibble of the map-mode byte -> (name, layouts it is plausible for)
MAP_MODES = {
    0x0: ("LoROM", {"LoROM"}),
    0x1: ("HiROM", {"HiROM"}),
    0x2: ("LoROM + S-DD1", {"LoROM"}),
    0x3: ("LoROM + SA-1", {"LoROM"}),
    0x5: ("ExHiROM", {"ExHiROM"}),
    0xA: ("HiROM + SPC7110", {"HiROM"}),
}
COUNTRIES = {
    0x00: "Japan", 0x01: "USA", 0x02: "Europe", 0x03: "Sweden/Scandinavia",
    0x06: "France", 0x07: "Netherlands", 0x08: "Spain", 0x09: "Germany",
    0x0A: "Italy", 0x0B: "China/HK", 0x0D: "Korea", 0x0F: "Canada",
    0x10: "Brazil", 0x11: "Australia",
}


def split_copier_header(raw):
    """Return (copier_header_bytes, image). Heuristic: size % 32 KiB == 512."""
    if len(raw) & 0x7FFF == COPIER_HEADER_SIZE:
        return raw[:COPIER_HEADER_SIZE], raw[COPIER_HEADER_SIZE:]
    return b"", raw


def compute_checksum(image):
    """SNES checksum: 16-bit byte sum; non-power-of-two images mirror the tail.

    Best effort for odd sizes (exact only when the tail size divides the
    power-of-two part), which covers essentially all commercial ROMs.
    """
    n = len(image)
    if n == 0:
        return 0
    p = 1 << (n.bit_length() - 1)
    if p == n:
        return sum(image) & 0xFFFF
    r = n - p
    return (sum(image[:p]) + sum(image[p:]) * (p // r)) & 0xFFFF


def parse_header(image, layout, offset):
    if offset + 0x20 > len(image):
        return None
    h = image[offset:offset + 0x20]
    title_raw = h[0x00:0x15]
    map_byte, rom_type, size_byte, sram_byte = h[0x15], h[0x16], h[0x17], h[0x18]
    country, dev_id, version = h[0x19], h[0x1A], h[0x1B]
    complement = h[0x1C] | (h[0x1D] << 8)
    checksum = h[0x1E] | (h[0x1F] << 8)

    score = 0
    if (complement ^ checksum) == 0xFFFF:
        score += 4
    printable = sum(1 for b in title_raw if 0x20 <= b < 0x7F or 0xA1 <= b <= 0xDF)
    if printable >= 18:
        score += 2
    mode = MAP_MODES.get(map_byte & 0x0F)
    if mode and layout in mode[1]:
        score += 2
    if map_byte & 0xE0 == 0x20:  # high bits 001 on every licensed cart
        score += 1
    if 1 <= size_byte <= 0x0D and (1 << size_byte) * 1024 <= len(image) * 2:
        score += 1

    return {
        "layout": layout,
        "offset": offset,
        "score": score,
        "title": bytes(b if 0x20 <= b < 0x7F else 0x3F for b in title_raw).decode("ascii").rstrip(),
        "title_hex": title_raw.hex(),
        "map_mode_byte": map_byte,
        "map_mode": mode[0] if mode else "unknown",
        "fastrom": bool(map_byte & 0x10),
        "rom_type_byte": rom_type,
        "declared_rom_kib": (1 << size_byte) if size_byte <= 0x10 else None,
        "declared_sram_kib": (1 << sram_byte) if 0 < sram_byte <= 0x0A else 0,
        "country": COUNTRIES.get(country, f"unknown (0x{country:02X})"),
        "developer_id": dev_id,
        "version": f"1.{version}",
        "checksum_stored": checksum,
        "checksum_complement": complement,
    }


def analyse(raw):
    copier, image = split_copier_header(raw)
    candidates = [
        c for layout, off in LAYOUTS.items()
        if (c := parse_header(image, layout, off)) is not None
    ]
    best = max(candidates, key=lambda c: c["score"], default=None)
    info = {
        "file_size": len(raw),
        "copier_header": bool(copier),
        "image_size": len(image),
        "image_size_pow2": len(image) & (len(image) - 1) == 0 if image else False,
        "sha1": hashlib.sha1(image).hexdigest(),
        "md5": hashlib.md5(image).hexdigest(),
        "crc32": f"{zlib.crc32(image) & 0xFFFFFFFF:08x}",
        "sha1_with_header": hashlib.sha1(raw).hexdigest(),
        "header": None,
        "header_confidence": "none",
    }
    if best and best["score"] >= 5:
        best["checksum_computed"] = compute_checksum(image)
        best["checksum_ok"] = best["checksum_computed"] == best["checksum_stored"]
        info["header"] = best
        info["header_confidence"] = "high" if best["score"] >= 8 else "medium"
    return info, image


def render_text(info):
    lines = [
        f"File size            : {info['file_size']} bytes",
        f"Copier header        : {'YES (512 bytes, strip before hashing/building)' if info['copier_header'] else 'no'}",
        f"Image size           : {info['image_size']} bytes ({info['image_size'] // 1024} KiB)"
        + ("" if info["image_size_pow2"] else "  [not a power of two]"),
        f"SHA-1 (headerless)   : {info['sha1']}",
        f"MD5   (headerless)   : {info['md5']}",
        f"CRC32 (headerless)   : {info['crc32']}",
    ]
    h = info["header"]
    if not h:
        lines.append("Internal header      : NOT FOUND (not a SNES ROM, or an unusual mapper)")
        return "\n".join(lines)
    lines += [
        f"Internal header      : {h['layout']} @ 0x{h['offset']:X} (confidence: {info['header_confidence']}, score {h['score']})",
        f"Title                : {h['title']!r}",
        f"Map mode             : 0x{h['map_mode_byte']:02X} = {h['map_mode']}{' (FastROM)' if h['fastrom'] else ' (SlowROM)'}",
        f"ROM type byte        : 0x{h['rom_type_byte']:02X}",
        f"Declared ROM size    : {h['declared_rom_kib']} KiB",
        f"Declared SRAM size   : {h['declared_sram_kib']} KiB",
        f"Country              : {h['country']}",
        f"Developer id         : 0x{h['developer_id']:02X}",
        f"Version              : {h['version']}",
        f"Checksum stored      : 0x{h['checksum_stored']:04X} (complement 0x{h['checksum_complement']:04X})",
        f"Checksum computed    : 0x{h['checksum_computed']:04X} -> {'OK' if h['checksum_ok'] else 'MISMATCH (bad dump, overdump, or odd size)'}",
    ]
    return "\n".join(lines)


def read_expected_sha1(path):
    for line in Path(path).read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            return line.split()[0].lower()
    return None


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("rom", type=Path)
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--strip", type=Path, metavar="OUT", help="write headerless image to OUT")
    ap.add_argument("--expect-sha1-file", type=Path, metavar="FILE",
                    help="fail (exit 3) if headerless SHA-1 differs from first hash in FILE")
    args = ap.parse_args(argv)

    info, image = analyse(args.rom.read_bytes())
    print(json.dumps(info, indent=2) if args.json else render_text(info))

    if args.strip:
        args.strip.write_bytes(image)
        print(f"wrote headerless image to {args.strip}", file=sys.stderr)

    if args.expect_sha1_file:
        expected = read_expected_sha1(args.expect_sha1_file)
        if expected is None:
            print(f"{args.expect_sha1_file}: no hash found", file=sys.stderr)
            return 3
        if expected != info["sha1"]:
            print(f"SHA-1 MISMATCH: expected {expected}, got {info['sha1']}", file=sys.stderr)
            return 3
        print("SHA-1 matches rom.sha1", file=sys.stderr)

    return 0 if info["header"] else 2


if __name__ == "__main__":
    sys.exit(main())
