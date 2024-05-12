import subprocess

class PDF():
    def __init__(self, pdf_file_path:str, drm=False):
        self.file_path = pdf_file_path    
        self.drm = drm

    def __make_pdf(self, args=None):

        def add_extra_options(args, options):
            if args:
                options.extend(args)
                return options
            else:
                return options

        if self.drm is True:
            options = ["pdf2htmlEX", f"{self.file_path}", "--no-drm", f"{self.drm}"]
            options = add_extra_options(args, options)
            subprocess.call(options)
        else:
            options = ["pdf2htmlEX", f"{self.file_path}"]
            options = add_extra_options(args, options)
            subprocess.call(options)

    def to_pdf(self, file_path=None):
        if file_path:
            args = ["-o", file_path]
            self.__make_pdf(args)
        else:
            self.__make_pdf()
        