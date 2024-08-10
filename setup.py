from setuptools import setup

with open("README.md", "r") as file:
    readme = file.read()

setup(name='pypdf2htmlex',
    version='1.8',
    license='MIT License',
    author='Gabriel Batistuta',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='batistutag190@gmail.com',
    keywords='pdf2htmlEX pdf-to-html pdf html wrapper',
    description=u'Wrapper não oficial do pdf2htmlEX',
    packages=['pypdf2htmlEX'],
    url="https://github.com/gabriel-batistuta/pypdf2htmlEX",
    project_urls = {
        'Repository': 'https://github.com/gabriel-batistuta/pypdf2htmlEX'
    },
    install_requires=[],)

