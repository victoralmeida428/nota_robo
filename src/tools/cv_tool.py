import pytesseract
from ollama_ocr import OCRProcessor
from abc import ABC, abstractmethod

class OCR(ABC):
    img_path = None

    def __init__(self, img_path):
        self.img_path = img_path

    def process_ocr_output(self, text: str) -> str:
        return text.replace(",  ", ".").replace("[^R]$", "").replace("RG", "R$")

    @abstractmethod
    def extract_text(self): raise NotImplementedError


class Tesseract(OCR):

    def extract_text(self) -> str:
        return self.process_ocr_output(pytesseract.image_to_string(self.img_path))

class OllamaOCR(OCR):

    def extract_text(self) -> str:
        ocr = OCRProcessor(model_name='llama3.2-vision:11b')
        return self.process_ocr_output(ocr.process_image(
            image_path=self.img_path,
            format_type="json"
        ))