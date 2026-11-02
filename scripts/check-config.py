#!/usr/bin/env python3
"""Validate the variable-font build config before gftools runs."""
from pathlib import Path
import re
import sys

CONFIG = Path(__file__).resolve().parent.parent / "sources" / "config.yaml"
text = CONFIG.read_text(encoding="utf-8")

def need(pattern: str, label: str) -> None:
    if not re.search(pattern, text, re.MULTILINE):
        raise SystemExit("missing %s" % label)

need(r"^familyName:\s*Sudo\s*$", "familyName: Sudo")
need(r"^buildVariable:\s*true\s*$", "buildVariable: true")
need(r"^\s*-\s*Sudo\.glyphspackage\s*$", "Sudo.glyphspackage source")
need(r"^\s*-\s*SudoUI\.glyphspackage\s*$", "SudoUI.glyphspackage source")
need(r"wght", "wght axis")
need(r"YTDE", "YTDE axis")
print("config OK: Sudo variable sources and axes present")
