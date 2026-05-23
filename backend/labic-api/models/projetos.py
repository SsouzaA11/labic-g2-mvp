from sqlalchemy import Column, Integer, String, Text, Date
from database import Base

class ProjetoModel(Base):
    __tablename__ = "projetos"

    id_projeto = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(150), nullable=False)
    descricao = Column(Text, nullbase=False)
    data_inicio = Column(Date, nullable=True)
    data_fim = Column(Date, nullable=True)

    status = Column(String(50), default="Em planejamento")
