from sqlalchemy import Column, Integer, String, Text
from database import Base

class PesquisadorModel(Base):
    __tablename__ = "pesquisadores"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    senha = Column(String(255), nullable=False)
    biografia = Column(Text, nullable=True)
    link_lattes = Column(String(255), nullable=True)