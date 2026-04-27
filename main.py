from fastapi import FastAPI

from routes.auth import router as auth_router
from routes.acessos import router as acessos_router
from routes.chaves import router as chaves_router
from routes.usuarios import router as usuarios_router
from database import engine

app = FastAPI()

app.include_router(auth_router)
app.include_router(acessos_router)
app.include_router(chaves_router)
app.include_router(usuarios_router)

#  Rota inicial
@app.get("/")
def home():
    return {"mensagem": "API rodando 🚀"}

#  Teste de conexão com banco
@app.get("/test-db")
def test_db():
    try:
        with engine.connect() as conn:
            return {"status": "Conectado com sucesso ✅"}
    except Exception as e:
        return {"erro": str(e)}

    




