"""Post-process a Marp `--pptx-editable` export so text doesn't re-wrap.

The export sizes each text box exactly around its rendered text, with zero
insets. Font sizes get rounded on the way (e.g. 12.75pt -> 12.8pt), so in
PowerPoint / Google Slides the text ends up slightly wider than its box and
wraps onto the next line, overlapping it. Widening every text box a bit fixes
that; the boxes are transparent and left-anchored, so nothing moves visually.
"""
import re
import shutil
import sys
import tempfile
import zipfile

WIDEN = 1.08


def fix_slide(xml):
    def fix_shape(m):
        shape = m.group(0)
        if 'txBox="1"' not in shape:
            return shape
        shape = re.sub(
            r'(<a:ext cx=")(\d+)(")',
            lambda e: f"{e.group(1)}{int(int(e.group(2)) * WIDEN)}{e.group(3)}",
            shape,
            count=1,
        )
        return re.sub(r"<a:bodyPr(?![^>]*\bwrap=)", '<a:bodyPr wrap="none"', shape)

    return re.sub(r"<p:sp>.*?</p:sp>", fix_shape, xml, flags=re.S)


def main(src, dst):
    with tempfile.NamedTemporaryFile(suffix=".pptx", delete=False) as tmp:
        with zipfile.ZipFile(src) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if re.fullmatch(r"ppt/slides/slide\d+\.xml", item.filename):
                    data = fix_slide(data.decode("utf-8")).encode("utf-8")
                zout.writestr(item, data)
    shutil.move(tmp.name, dst)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else sys.argv[1])
