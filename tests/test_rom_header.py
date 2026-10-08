import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import rom_header  # noqa: E402


def make_rom(layout="LoROM", size=0x80000, title=b"TEST ROM", map_byte=None):
    """Build a synthetic ROM with a self-consistent internal header."""
    off = rom_header.LAYOUTS[layout]
    rom = bytearray(size)
    for i in range(0, size, 251):
        rom[i] = i & 0xFF
    map_byte = map_byte if map_byte is not None else (0x20 if layout == "LoROM" else 0x21)
    h = bytearray(0x20)
    h[0:21] = title.ljust(21)
    h[0x15], h[0x16] = map_byte, 0x00
    h[0x17] = size.bit_length() - 11  # 2**n KiB
    h[0x19] = 0x00
    h[0x1C:0x20] = bytes([0xFF, 0xFF, 0x00, 0x00])
    rom[off:off + 0x20] = h
    # Stored checksum bytes always contribute 0x1FE together with their complement.
    csum = rom_header.compute_checksum(bytes(rom))
    rom[off + 0x1C:off + 0x20] = bytes([(~csum) & 0xFF, ((~csum) >> 8) & 0xFF, csum & 0xFF, csum >> 8])
    return bytes(rom)


class RomHeaderTests(unittest.TestCase):
    def test_lorom(self):
        info, _ = rom_header.analyse(make_rom("LoROM"))
        h = info["header"]
        self.assertEqual(h["layout"], "LoROM")
        self.assertEqual(h["title"], "TEST ROM")
        self.assertTrue(h["checksum_ok"])
        self.assertEqual(h["declared_rom_kib"], 512)
        self.assertEqual(info["header_confidence"], "high")

    def test_hirom(self):
        info, _ = rom_header.analyse(make_rom("HiROM", size=0x100000))
        self.assertEqual(info["header"]["layout"], "HiROM")
        self.assertTrue(info["header"]["checksum_ok"])

    def test_copier_header_is_stripped_before_hashing(self):
        rom = make_rom("LoROM")
        plain, _ = rom_header.analyse(rom)
        headered, image = rom_header.analyse(b"\x00" * 512 + rom)
        self.assertTrue(headered["copier_header"])
        self.assertEqual(image, rom)
        self.assertEqual(headered["sha1"], plain["sha1"])
        self.assertEqual(headered["header"]["layout"], "LoROM")

    def test_garbage_has_no_header(self):
        info, _ = rom_header.analyse(bytes(0x80000))
        self.assertIsNone(info["header"])

    def test_cli_sha1_check(self):
        rom = make_rom("LoROM")
        info, _ = rom_header.analyse(rom)
        with tempfile.TemporaryDirectory() as d:
            rom_path, sha_path = Path(d, "r.sfc"), Path(d, "rom.sha1")
            rom_path.write_bytes(rom)
            sha_path.write_text(f"# comment\n{info['sha1']}  baserom.sfc\n")
            self.assertEqual(rom_header.main([str(rom_path), "--expect-sha1-file", str(sha_path)]), 0)
            sha_path.write_text("0" * 40 + "\n")
            self.assertEqual(rom_header.main([str(rom_path), "--expect-sha1-file", str(sha_path)]), 3)


if __name__ == "__main__":
    unittest.main()
