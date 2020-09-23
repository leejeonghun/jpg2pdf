import os
import unittest
import jpg2pdf
import test.pdfvalid


class Unittest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.path = os.path.dirname(__file__)
        self.test_pdf = os.path.join(self.path, 'test.pdf')

    def _clean(self):
        if os.path.exists(self.test_pdf):
            os.remove(self.test_pdf)

    def setUp(self):
        self._clean()

    def tearDown(self):
        self._clean()

    def test_convert_single_jpg(self):
        with jpg2pdf.create(self.test_pdf) as pdf:
            pdf.add(os.path.join(self.path, '1.jpg'))
        self.assertTrue(test.pdfvalid.validation(self.test_pdf))

    def test_convert_multiple_jpg(self):
        with jpg2pdf.create(self.test_pdf) as pdf:
            pdf.add(os.path.join(self.path, '1.jpg'))
            pdf.add(os.path.join(self.path, '2.jpg'))
        self.assertTrue(test.pdfvalid.validation(self.test_pdf))


if __name__ == "__main__":
    unittest.main()
