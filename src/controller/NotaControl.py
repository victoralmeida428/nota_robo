import os
from datetime import datetime
from fastapi import UploadFile
from model.comprovante_model import ComprovanteModel
from model.file_model import FileModel
from werkzeug.utils import secure_filename
from .utils import EXTENSOES_IMG
import tempfile
from tools.cv_tool import Tesseract
from Service.deepseek_server import DeepSeekServer

from Service.AuthService import AuthService


class NotaControl:


    @staticmethod
    def auth(password):
        auth = AuthService()
        auth.authenticate(password)


    @classmethod
    async def post(cls, file: UploadFile, password: str) -> dict:
        cls.auth(password)
        file_name = secure_filename(file.filename)
        cls.validacao_img(file_name)
        info_file = await cls.salvar_arquivo(file, file_name)
        deepseek_service = DeepSeekServer()
        return deepseek_service.response(Tesseract(info_file.path).extract_text())

    @staticmethod
    def validacao_img(nome: str):
        extensao = nome.rsplit(".", 1)[-1].lower()
        if extensao not in EXTENSOES_IMG:
            raise ValueError("Extensão não permitida")

        if extensao == "":
            raise ValueError("Nome do arquivo em branco")

    @staticmethod
    async def salvar_arquivo(file: UploadFile, nome_seguro) -> FileModel:
        tempDir = tempfile.mkdtemp()
        file_path = os.path.join(tempDir, nome_seguro)

        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)


        file = FileModel(
            nome_original = file.filename,
            nome_armazenado=nome_seguro,
            path = file_path,
            data_upload=datetime.now()
        )
        return file


