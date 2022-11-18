mkmd
====

**M**a**k**e **M**ark**d**own Documents in Python.


Features
--------

* [x] Heading
* [x] Paragraph
* [x] Code Block
* [x] Horizontal Rule
* [x] Reference
* [x] Image
* [x] Unordered List
* [x] Ordered List


Installation
------------

```bash
pip install mkmd
```


Basic Usage
-----------

```python
import mkmd
from mkmd.utils import *

md = mkmd.Markdown()

(md
    .add_heading(f"Hello {bold_and_italic('MKMD')}",)
    
    .add_paragraph(f"""
        This markdown document was generated by using
        {refer('mkmd', '1')}. This is a quick example showing how to
        use it:
    """, wrapped = True)
    
    .add_codeblock("""
        import mkmd
        
        md = mkmd.Markdown()
        md.add_heading("Hello World")
        md.add_paragraph("Lorem ipsum dolor sit amet.")
    """, language = "python")
    
    .add_ordered_list(
        *"So many things are possible!".split()
    )
    
    .add_reference("1", "http://example.org", "Look at this")
    
    .add_image("Linux Mascot",
        "https://mdg.imgix.net/assets/images/tux.png?auto=format&fit=clip&q=40&w=100"
    )
)

if __name__ == "__main__":
    md.save("example_result.md")
```


Links
-----

* [Documentation](https://phoenixr-codes.github.io/mkmd/)
* [PyPI](https://pypi.org/project/mkmd)
* [Repository](https://github.com/phoenixr-codes/mkmd/)
