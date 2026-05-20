from fastapi import FastAPI
from routers import pesquisadores_router, projetos_router, artigos_router, linhas_pesquisa_router, auth_router

app = FastAPI(title="LABIC API")

app.include_router(auth_router.router)
app.include_router(pesquisadores_router.router)
app.include_router(projetos_router.router)
app.include_router(artigos_router.router)
app.include_router(linhas_pesquisa_router.router)