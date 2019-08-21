import setuptools


with open('README.md', 'r') as f:
    long_description = f.read()


setuptools.setup(
    name = 'bdtrans',
    version = '0.q2.1',
    author = 'Mxsyx',
    author_email = 'zsimline@163.com',
    description = 'A library for china baidu translation',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    license = 'GNU GENERAL PUBLIC LICENSE',
    url = 'https://github.com/zsimline/bdtrans',
    packages = setuptools.find_packages(),
    platforms = 'any',
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent'
    ]
)

