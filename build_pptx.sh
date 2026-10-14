#!/usr/bin/env bash
# Build an editable PPTX (real text boxes, not images) from slides.md.
# Requires LibreOffice (used by Marp's --pptx-editable).
set -euo pipefail
cd "$(dirname "$0")"
npx -y @marp-team/marp-cli@latest slides.md --no-stdin --html --allow-local-files \
    --pptx --pptx-editable -o slides.pptx
python3 tools/fix_pptx.py slides.pptx
chmod 644 slides.pptx
echo "Wrote $(pwd)/slides.pptx"
