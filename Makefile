# dbz-ssj-myth build. See docs/SETUP.md and docs/WORKFLOW.md.
#
#   make header     inspect baserom/baserom.sfc (map mode, checksum, hashes)
#   make verify     check baserom matches rom.sha1
#   make            assemble + link src/*.s -> build/dbz-ssj.sfc
#   make compare    build, then require byte-identical output to rom.sha1
#   make test       run tool unit tests
#   make check      test + ensure no ROMs/copyrighted assets are tracked

PYTHON  ?= python3
CA65    ?= ca65
LD65    ?= ld65
BASEROM ?= baserom/baserom.sfc
BUILD   := build
TARGET  := $(BUILD)/dbz-ssj.sfc
LINKCFG := linker/snes.cfg
SRCS    := $(wildcard src/*.s)
OBJS    := $(SRCS:src/%.s=$(BUILD)/%.o)

.PHONY: all compare header verify test check-no-roms check hooks clean

all:
ifeq ($(strip $(SRCS)),)
	@echo "Nothing to build yet: src/ has no .s files. See docs/WORKFLOW.md."
else
	@$(MAKE) --no-print-directory $(TARGET)
endif

$(BUILD)/%.o: src/%.s $(wildcard include/*.inc) | $(BUILD)
	$(CA65) -g -I include -o $@ $<

$(TARGET): $(OBJS) $(LINKCFG)
	$(LD65) -C $(LINKCFG) -m $(BUILD)/dbz-ssj.map -Ln $(BUILD)/dbz-ssj.lbl -o $@ $(OBJS)
	@sha1sum $@

$(BUILD):
	mkdir -p $@

compare: all
	@test -f rom.sha1 || { echo "rom.sha1 missing - create it from 'make header' output (see docs/ROM_INFO.md)"; exit 1; }
	@test -f $(TARGET) || { echo "No build output to compare."; exit 1; }
	@$(PYTHON) tools/rom_header.py $(TARGET) --expect-sha1-file rom.sha1 >/dev/null

header:
	@test -f $(BASEROM) || { echo "Put your own dump at $(BASEROM) (see baserom/README.md)"; exit 1; }
	@$(PYTHON) tools/rom_header.py $(BASEROM)

verify:
	@test -f $(BASEROM) || { echo "Put your own dump at $(BASEROM) (see baserom/README.md)"; exit 1; }
	@$(PYTHON) tools/rom_header.py $(BASEROM) --expect-sha1-file rom.sha1 >/dev/null

test:
	$(PYTHON) -m unittest discover -s tests

check-no-roms:
	@sh tools/check_no_roms.sh

check: test check-no-roms

hooks:
	git config core.hooksPath .githooks
	@echo "Pre-commit hook enabled (blocks ROM/asset commits)."

clean:
	rm -rf $(BUILD)
