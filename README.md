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
## making HTML files from dir with various pdf 

this code will make html files of all pdf in same folder 'pdfs'
```python
import pypdf2htmlEX

pypdf2htmlEX.dir_to_html(dir_path='pdfs')
```

this code will make html files of all pdf in folder 'pdfs' on folder 'htmls'
```python
import pypdf2htmlEX

pypdf2htmlEX.dir_to_html(dir_path='pdfs', dest_dir='test')
```

this code will make html files of all pdf in folder 'pdfs' on folder 'htmls' and every html file will have sequential after the name File, ex: "File_1.html", "File_2.html".
```python
import pypdf2htmlEX

pypdf2htmlEX.dir_to_html(dir_path='pdfs', dest_dir='test', new_file_name='File_')
```
