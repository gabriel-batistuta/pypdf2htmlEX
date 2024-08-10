import subprocess
import os
from os.path import basename
from typing import Union

class PDF():
    def __init__(self, pdf_file_path:str, drm=None):
        self.file_path = pdf_file_path    
        self.drm = drm

    def __make_html(self, args=None):

        '''
        Private main function to make the HTML file from the PDF passing the parameters.

        Parameters:
        args (list, optional): Additional arguments to pass to pdf2htmlEX that is not in the library. Defaults to None.
        '''

        def add_extra_options(args, options):
            if args:
                options.extend(args)
                return options
            else:
                return options

        if self.drm is True:
            options = ["pdf2htmlEX", f"{self.file_path}", "--no-drm", "1"]
            options = add_extra_options(args, options)
            print(options)
            for i in options:
                print(i, end=" ")
            subprocess.call(options)
        else:
            options = ["pdf2htmlEX", f"{self.file_path}"]
            options = add_extra_options(args, options)
            subprocess.call(options)

    def to_html(self, dest_dir=None, pdf_filename=None, new_file_name=None):
        '''
        Converts the PDF file to HTML.

        Parameters:
        dest_dir (str, optional): The path to save the converted HTML file. Defaults to None will save in the same directory that pdf_file_path of PDF class.
        '''

        if dest_dir:
            args = ["--dest-dir", dest_dir]
            self.__make_html(args)
        else:
            self.__make_html()
        if pdf_filename and new_file_name:
            try:
                pdf_filename = pdf_filename.replace(".pdf", ".html")
                os.rename(f"{dest_dir}/{pdf_filename}", f"{dest_dir}/{new_file_name}")
            except Exception as e:
                print(f"Error renaming {dest_dir}/{pdf_filename}: {e}")
        
def dir_to_html(dir_path, dest_dir=None, new_file_name=None):
    '''
    Converts all PDF files in a directory to HTML.

    Parameters:
    dest_dir (str, optional): The path to the destination directory to save the HTML files. Defaults to None will save in same dir.
    new_file_name (str, optional): The new name for the HTML files. Generates sequential for pdfs, ex: pdf0, pdf1, pdf2. Defaults to None will maintly name them as is replacing .pdf for .html
    '''

    pdf_files = [f"{dir_path}/{file}" for file in os.listdir(dir_path) if file.endswith(".pdf")]

    for i, pdf_file in enumerate(pdf_files):
        pdf = PDF(pdf_file, drm=True)
        if dest_dir:
            if new_file_name:
                if '.html' not in new_file_name:
                    pdf.to_html(dest_dir=dest_dir, pdf_filename=basename(pdf_file), new_file_name=f"{new_file_name}_{i+1}.html")
                else:
                    pdf.to_html(dest_dir=dest_dir, pdf_filename=basename(pdf_file), new_file_name=f'{new_file_name.replace(".html","")}_{i+1}.html')
            else:
                pdf.to_html(dest_dir=dest_dir)
        else:
            pdf.to_html()