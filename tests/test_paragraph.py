from pathlib import Path

import mkmd

lorem_ipsum = """
    Lorem ipsum dolor sit amet, consetetur
    sadipscing elitr, sed diam nonumy eirmod
    tempor invidunt ut labore et dolore magna
    aliquyam.
"""

def test_with_heading():
    md = mkmd.Markdown()
    
    md.add_heading("Hello World")
    md.add_paragraph(lorem_ipsum, wrapped = True)
    doc = str(md)
    
    assert doc == (
        Path(__file__)
        .parent
        / f"{__name__}-test_with_heading-expect.md"
    ).read_text()


def test_multiple():
    md = mkmd.Markdown()
    
    md.add_paragraph(lorem_ipsum, wrapped = True)
    md.add_paragraph(lorem_ipsum, wrapped = True)
    
    doc = str(md)
    
    assert doc == (
        Path(__file__)
        .parent
        / f"{__name__}-test_multiple-expect.md"
    ).read_text()
    