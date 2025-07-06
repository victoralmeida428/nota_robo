import datetime

from pydantic import BaseModel, Field

class FileModel(BaseModel):
    nome_original: str = Field(..., description="The final purchase value, usually preceded by R$, U$")
    nome_armazenado: str = Field(..., description="The exact moment of the transaction DD/MM/YYYY HH:MM:SS")
    path: str = Field(..., description="It can be credit for DEBITO or credito for CREDITO or pix for PIX")
    data_upload: datetime.datetime = Field(..., description="The name of the company where the purchase was made.")