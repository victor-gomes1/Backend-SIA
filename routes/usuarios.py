from fastapi import APIRouter
from sqlalchemy import text
from database import engine

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.get("/")
def listar_usuarios():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM usuarios"))
            
            usuarios = []
            for row in result:
                user = dict(row._mapping)
                user.pop("senha", None)
                usuarios.append(user)

        return {
            "total": len(usuarios),
            "usuarios": usuarios
        }

    except Exception as e:
        return {"erro": str(e)}