import subprocess
import os
from os.path import basename

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
            subprocess.call(options)
        else:
            options = ["pdf2htmlEX", f"{self.file_path}"]
            options = add_extra_options(args, options)
            subprocess.call(options)

    def to_html(self, file_path=None):
        '''
        Converts the PDF file to HTML.

        Parameters:
        file_path (str, optional): The path to save the converted HTML file. Defaults to None will save in the same directory that pdf_file_path of PDF class.
        '''

        if file_path:
            args = ["--dest-dir", file_path]
            self.__make_html(args)
        else:
            self.__make_html()
        
def dir_to_html(dir_path, dest_dir=None):
    '''
    Converts all PDF files in a directory to HTML.

    Parameters:
    dir_path (str): The path to the directory containing PDF files.
    dest_dir (str, optional): The path to the destination directory to save the HTML files. Defaults to None will save in same dir.
    '''

    pdf_files = [f"{dir_path}/{file}" for file in os.listdir(dir_path) if file.endswith(".pdf")]

    for pdf_file in pdf_files:
        pdf = PDF(pdf_file, drm=True)
        if dest_dir:
            pdf.to_html(file_path=f'{dest_dir}/{basename(pdf_file).replace(".pdf", ".html")}')
        else:
            pdf.to_html()