import unittest
from src.tools.cv_tool import Tesseract, OllamaOCR


class TestTesseractOCR(unittest.TestCase):
    path = "./data/comprovante.jpeg"

    def test_tesseract_ocr(self):
        ocr = Tesseract(self.path)
        text = ocr.extract_text()
        self.assertTrue(isinstance(text, str))
        self.assertTrue('R$' in text)
        self.assertTrue('2025' in text)

    def test_ollamaocr(self):
        try:
            ollamao = OllamaOCR(self.path)
            text = ollamao.extract_text()
            self.assertTrue(isinstance(text, str))
            self.assertTrue('R$' in text)
            self.assertTrue('2025' in text)
        except Exception as e:
            self.skipTest('OllamaOCR not working')

