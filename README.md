[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)
[![Build Status](https://travis-ci.com/leejeonghun/jpg2pdf.svg?token=vPnYhgsqQx6vveRqjzR8&branch=master)](https://travis-ci.com/leejeonghun/jpg2pdf)
[![codecov](https://codecov.io/gh/leejeonghun/jpg2pdf/branch/master/graph/badge.svg?token=PFD5RT6WX4)](https://codecov.io/gh/leejeonghun/jpg2pdf)
[![PyPI version](https://badge.fury.io/py/jpg2pdf.svg)](https://badge.fury.io/py/jpg2pdf)

# jpg2pdf

Simple Python module for generating PDF document from JPEG files.

It can put multiple scans/photos of pages in JPEG(.jpg) into one PDF file without quality loss.
Python 3.6 or higher is required, no dependencies on external libraries.

## Usage

```python
import jpg2pdf

with jpg2pdf.create('test.pdf') as pdf:
    pdf.add('1.jpg')
    pdf.add('2.jpg')
    pdf.add('3.jpg')
```
