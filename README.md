# PDF2HTMLEX
pypdf2htmlex is a Python wrapper for the PDF2HTMLEX

# Installing
```bash
pip install pypdf2htmlex
```

# Using

## making the HTML file from a pdf
```python
import pypdf2htmlEX

pdf = pypdf2htmlEX.PDF("path-to-my-file.pdf")
pdf.to_html()
# will be generated a html file on folder path-to-my-file
```

## setting drm
can pass True for drm parameter to convert a file to html without restrition
the value is False by default

```python
import pypdf2htmlEX

pdf = pypdf2htmlEX.PDF("path-to-my-file.pdf", drm=True)
pdf.to_html()
```
