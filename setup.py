
from distutils.core import setup

setup(
    name='mkdocs-nbconvert',
    version='0.1.0',
    author='Andy Oakley',
    author_email='ao@ao.vc',
    packages=['mkdocs_nbconvert'],
    license='LICENSE.txt',
    description='Mkdocs plugin to render Jupyter notebooks.',
    install_requires=[
        'nbconvert',
        'fnmatch',
    ],

    entry_points={
        'mkdocs.plugins': [
            'nbconvert = mkdocs_nbconvert.nbconvert:NotebookConverter',
        ]
    }
)

