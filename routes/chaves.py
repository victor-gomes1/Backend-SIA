from fastapi import APIRouter
from sqlalchemy import text
from database import engine
from pydantic import BaseModel

router = APIRouter(prefix="/chaves", tags=["Chaves"])

class ChaveRequest(BaseModel):
    chave_id: int
    usuario_id: int


@router.post("/retirar-chave")
def retirar_chave(dados: ChaveRequest):
    try:
        with engine.begin() as conn:

            chave = conn.execute(text("""
                SELECT * FROM chaves WHERE id = :id
            """), {"id": dados.chave_id}).fetchone()

            if not chave:
                return {"status": "Chave não encontrada ❌"}

            chave = dict(chave._mapping)

            if chave["status"] != "Disponivel":
                return {"status": "Chave já está em uso ❌"}

            conn.execute(text("""
                INSERT INTO controle_chaves 
                (chave_id, usuario_id, data_retirada)
                VALUES (:chave_id, :usuario_id, NOW() - INTERVAL '3 hours')
            """), {
                "chave_id": dados.chave_id,
                "usuario_id": dados.usuario_id
            })

            conn.execute(text("""
                UPDATE chaves
                SET status = 'Em uso'
                WHERE id = :id
            """), {"id": dados.chave_id})

            return {"status": "Chave retirada com sucesso 🔑"}

    except Exception as e:
        return {"erro": str(e)}


@router.post("/devolver-chave")
def devolver_chave(dados: ChaveRequest):
    try:
        with engine.begin() as conn:

            result = conn.execute(text("""
                UPDATE controle_chaves
                SET data_devolucao = NOW() - INTERVAL '3 hours'
                WHERE chave_id = :chave_id
                AND data_devolucao IS NULL
            """), {
                "chave_id": dados.chave_id
            })

            if result.rowcount == 0:
                return {"status": "Nenhuma retirada em aberto para essa chave ❌"}

            conn.execute(text("""
                UPDATE chaves
                SET status = 'Disponivel'
                WHERE id = :id
            """), {"id": dados.chave_id})

            return {"status": "Chave devolvida com sucesso 🔓"}

    except Exception as e:
        return {"erro": str(e)}


@router.get("/historico-chave/{chave_id}")
def historico_chave(chave_id: int):
    try:
        with engine.connect() as conn:

            result = conn.execute(text("""
                SELECT 
                    c.usuario_id,
                    u.nome_completo,
                    c.data_retirada,
                    c.data_devolucao
                FROM controle_chaves c
                LEFT JOIN usuarios u ON u.id = c.usuario_id
                WHERE c.chave_id = :id
                ORDER BY c.data_retirada DESC
            """), {"id": chave_id})

            historico = [dict(row._mapping) for row in result]

            return {
                "total": len(historico),
                "historico": historico
            }

    except Exception as e:
        return {"erro": str(e)}