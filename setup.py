import os
from setuptools import setup
from jpg2pdf import __version__

curr_path = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(curr_path, 'README.md'), encoding='utf-8') as f:
    long_desc = f.read()

setup(name='jpg2pdf',
      version=__version__,
      description='Python module for generating PDF document from JPEG files.',
      long_description=long_desc,
      long_description_content_type='text/markdown',
      author='Jeonghun Lee',
      url='https://github.com/leejeonghun/jpg2pdf',
      python_requires=">=3.6",
      license='BSD',
      py_modules=['jpg2pdf'],
      platforms=['any'])
