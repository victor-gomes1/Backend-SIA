from fastapi import APIRouter
from sqlalchemy import text
from database import engine
from pydantic import BaseModel

router = APIRouter(prefix="/acessos", tags=["Acessos"])

class AcessoRequest(BaseModel):
    codigo_qr: str


# Validar QR Code
@router.post("/validar-qr")
def validar_qr(dados: AcessoRequest):
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT * FROM usuarios 
                WHERE codigo_qr = :codigo_qr
            """), {
                "codigo_qr": dados.codigo_qr
            }).fetchone()

        if not result:
            return {"status": "QR Code inválido ❌"}

        usuario = dict(result._mapping)

        if usuario["status_acesso"] != "Ativo":
            return {
                "status": "Acesso bloqueado ❌",
                "motivo": "Usuário inativo"
            }

        usuario.pop("senha", None)

        return {
            "status": "Acesso liberado ✅",
            "usuario": usuario
        }

    except Exception as e:
        return {"erro": str(e)}


# Registrar acesso
@router.post("/registrar-acesso")
def registrar_acesso(dados: AcessoRequest):
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT * FROM usuarios 
                WHERE codigo_qr = :codigo_qr
            """), {
                "codigo_qr": dados.codigo_qr
            }).fetchone()

        if not result:
            return {"status": "QR Code inválido ❌"}

        usuario = dict(result._mapping)

        if usuario["status_acesso"] == "Ativo":
            status = "Liberado"
            motivo = None
        else:
            status = "Negado"
            motivo = "Usuário inativo"

        with engine.begin() as conn:
            conn.execute(text("""
                INSERT INTO registro_acesso 
                (usuario_id, data_hora, status_liberacao, local, motivo)
                VALUES (:usuario_id, NOW() - INTERVAL '3 hours', :status_liberacao, :local, :motivo)
            """), {
                "usuario_id": usuario["id"],
                "status_liberacao": status,
                "local": "Entrada Principal",
                "motivo": motivo
            })

        return {
            "status": f"Acesso {status} ✅",
            "usuario": usuario["nome_completo"]
        }

    except Exception as e:
        return {"erro": str(e)}
    