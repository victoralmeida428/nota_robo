from fastapi import FastAPI

from view.nota_view import router_comprovantes

app = FastAPI()

app.include_router(router_comprovantes, prefix='/api/v1', tags=['comprovantes'])

@app.get("/")
async def root():
    return {"status": "checked"}


