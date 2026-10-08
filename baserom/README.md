# baserom/

Place **your own legally obtained dump** here as `baserom.sfc`. Everything in this directory except this file is git-ignored.

- Prefer a headerless dump (size is a multiple of 32 KiB). If `make header` reports a 512-byte copier header, strip it: `python3 tools/rom_header.py baserom/baserom.sfc --strip baserom/headerless.sfc`, then rename.
- Run `make header` and record the results in `docs/ROM_INFO.md`.
- Put the headerless SHA-1 in `/rom.sha1` (a hash is not game data and is committed).
- Treat files here as read-only.
