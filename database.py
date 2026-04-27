from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres.uyrfdpvfcgarcirkaagy:Fccba03450345.FCCB@aws-1-us-east-2.pooler.supabase.com:6543/postgres"

engine = create_engine(
    DATABASE_URL,
    connect_args={"sslmode": "require"}
)