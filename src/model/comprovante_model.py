from pydantic import BaseModel, Field

class ComprovanteModel(BaseModel):
    valor: float = Field(..., description="The final purchase value, usually preceded by R$, U$")
    moeda: str = Field(..., description="The currency of the transaction, which can be the symbol (e.g., 'R$', '$', '€') or the ISO code (e.g., 'BRL', 'USD', 'EUR').")
    data_hora: str = Field(..., description="The exact moment of the transaction DD/MM/YYYY HH:MM:SS")
    meio_pagamento: str = Field(..., description="It can be credit for DEBITO or credito for CREDITO or pix for PIX")
    estabelecimento: str = Field(..., description="The name of the company where the purchase was made.")