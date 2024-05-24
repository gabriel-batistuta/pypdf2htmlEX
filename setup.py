from setuptools import setup

with open("README.md", "r") as file:
    readme = file.read()

with open("requirements.txt") as file:
    requirements_aux = []
    requirements = file.readlines()
    for r in requirements:
        r = r.replace("\n","")
        requirements_aux.append(r)

setup(name='pypdf2htmlex',
    version='1.0',
    license='MIT License',
    author='Gabriel Batistuta',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='batistutag190@gmail.com',
    keywords='pdf2htmlEX pdf-to-html pdf html wrapper',
    description=u'Wrapper não oficial do pdf2htmlEX',
    packages=['pypdf2htmlEX'],
    install_requires=requirements_aux,)

