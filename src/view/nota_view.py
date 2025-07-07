# /views/car_view.py
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from controller.NotaControl import NotaControl
from model.comprovante_model import ComprovanteModel
from fastapi import UploadFile, File, HTTPException, Form, APIRouter, Depends
import secrets
from dotenv import load_dotenv
load_dotenv()
import os

security = HTTPBasic()
router_comprovantes = APIRouter()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, os.environ.get("PASSWORD", "admin"))
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
@router_comprovantes.post("/comprovante")
async def comprovante_post(
        file: UploadFile = File(..., description="Imagem do comprovante"),
        _: str = Depends(get_current_username)
):
    try:
        return await NotaControl.post(file)
    except ValueError as err:
        raise HTTPException(status_code=404, detail=err.args[0])
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail="Error Server")
