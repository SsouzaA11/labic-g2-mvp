from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from models.associacoes import projeto_artigo

class ProjetoModel(Base):
    __tablename__ = "projetos"

    # atributos
    id_projeto = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(150), nullable=False)
    descricao = Column(Text, nullable=True)
    data_inicio = Column(Date, nullable=True)
    data_fim = Column(Date, nullable=True)
    status = Column(String(50), default="Em Planejamento")

    # chave estrangeira
    linha_pesquisa_id = Column(Integer, ForeignKey("linhas_pesquisa.id_linha"))

    # relacionamentos
    artigos = relationship("ArtigoModel", secondary=projeto_artigo, back_populates="projetos")
    pesquisadores_associacao = relationship("PesquisadorProjetoModel", back_populates="projeto")
    linha_pesquisa = relationship("LinhaPesquisaModel", back_populates="projetos")

