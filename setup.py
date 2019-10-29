from setuptools import setup
setup(
    name='pdf2md',
    version='0.8',
    description='Convert pdf file into jpg and put to markdown file.',
    long_description='readme.md',
    author='nyamel',
    author_email='twilight6sachirin@gmail.com',
    licence='MIT',
    install_requests=['pdf2image','click'],
    entry_points={
        'console_scripts':[
            'pdf2md=src.core:main'
        ]
    }
)