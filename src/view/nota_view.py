# /views/car_view.py
from fastapi import APIRouter
from controller.NotaControl import NotaControl
from model.comprovante_model import ComprovanteModel
from fastapi import UploadFile, File, HTTPException, Form

router_comprovantes = APIRouter()

@router_comprovantes.post("/comprovante")
async def comprovante_post(
        file: UploadFile = File(..., description="Imagem do comprovante"),
        password: str = Form(default="", description="senha para acessar a api")
):
    try:
        return await NotaControl.post(file, password)
    except ValueError as err:
        raise HTTPException(status_code=404, detail=err.args[0])
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail="Error Server")
