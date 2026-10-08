#!/bin/sh
# Fail if any tracked or staged file looks like a ROM or ripped game asset.
# See docs/decisions/0004-no-copyrighted-material.md.
set -eu

files=$( { git ls-files; git diff --cached --name-only --diff-filter=ACM; } | sort -u)
bad=""

# By extension.
ext_hits=$(printf '%s\n' "$files" | grep -iE '\.(sfc|smc|swc|fig|nes|fds|gb|gbc|gba|nds|z64|n64|v64)$' || true)
[ -n "$ext_hits" ] && bad="$bad$ext_hits\n"

# By content: any file >= 32 KiB outside docs that is not text is suspicious.
for f in $(printf '%s\n' "$files"); do
    [ -f "$f" ] || continue
    size=$(wc -c < "$f")
    if [ "$size" -ge 32768 ] && ! grep -Iq . "$f" 2>/dev/null; then
        bad="$bad$f (binary, $size bytes)\n"
    fi
done

if [ -n "$bad" ]; then
    printf 'ERROR: ROM-like or large binary files are tracked/staged:\n' >&2
    printf "$bad" >&2
    printf 'Game data must never be committed. Use baserom/ or references/ (git-ignored).\n' >&2
    exit 1
fi
echo "check-no-roms: ok"
