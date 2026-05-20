from fastapi import APIRouter

router = APIRouter(prefix="/artigos", tags=["Artigos"])

@router.get("/")
def listar_artigos():
    return [
        {"id": 1, "titulo": "Deep Learning Aplicado", "resumo": "Estudo sobre redes neurais"},
        {"id": 2, "titulo": "Otimização de Queries", "resumo": "Técnicas de performance em SQL"},
    ]

@router.get("/{id}")
def buscar_artigo(id: int):
    return {"id": id, "titulo": "Deep Learning Aplicado", "resumo": "Estudo sobre redes neurais"}

@router.post("/")
def criar_artigo(dados: dict):
    return {"mensagem": "Artigo criado com sucesso", "dados": dados}

@router.put("/{id}")
def atualizar_artigo(id: int, dados: dict):
    return {"mensagem": f"Artigo {id} atualizado com sucesso", "dados": dados}

@router.delete("/{id}")
def deletar_artigo(id: int):
    return {"mensagem": f"Artigo {id} deletado com sucesso"}