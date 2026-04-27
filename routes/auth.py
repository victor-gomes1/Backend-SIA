from fastapi import APIRouter
from sqlalchemy import text
from database import engine
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Autenticação"])

class LoginRequest(BaseModel):
    email: str
    senha: str

@router.post("/login")
def login(dados: LoginRequest):
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT * FROM usuarios
                WHERE email = :email AND senha = :senha
            """), {
                "email": dados.email,
                "senha": dados.senha
            }).fetchone()

            if result:
                usuario = dict(result._mapping)
                usuario.pop("senha", None)
                return {
                    "status": "Login realizado com sucesso ✅",
                    "usuario": usuario
                }
            else:
                return {"erro": "Email ou senha inválidos ❌"}

    except Exception as e:
        return {"erro": str(e)}