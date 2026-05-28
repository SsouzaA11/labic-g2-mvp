from datetime import datetime, timedelta, timezone
import jwt
from passlib.context import CryptContext
from core.config import settings

# modelo de geração de hashs
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# funções para senhas
def gerar_hash_senha(senha_pura: str) -> str:
    return pwd_context.hash(senha_pura)

def verificar_senha(senha_inserida: str, senha_hash_usuario: str) -> bool:
    return pwd_context.verify(senha_inserida, senha_hash_usuario)

# geração de token JWT para login
def criar_token_acesso(dados: dict) -> str:
    dados_para_codificar = dados.copy()

    # gera e adiciona tempo máximo de login
    horario_atual = datetime.now(timezone.utc)
    horario_expiracao = horario_atual + timedelta(minutes=settings.ACESS_TOKEN_EXPIRE_MINUTES)

    dados_para_codificar.update({"exp": horario_expiracao})

    # define o token
    token_jwt = jwt.encode(
        dados_para_codificar,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return token_jwt