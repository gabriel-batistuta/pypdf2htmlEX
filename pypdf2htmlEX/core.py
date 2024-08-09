import subprocess

class PDF():
    def __init__(self, pdf_file_path:str, drm=None):
        self.file_path = pdf_file_path    
        self.drm = drm

    def __make_html(self, args=None):

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
        if file_path:
            args = ["--dest-dir", file_path]
            self.__make_html(args)
        else:
            self.__make_html()
        