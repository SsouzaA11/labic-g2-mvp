from passlib.context import CryptContext

# modelo de geração de hashs
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# funções para senhas
def gerar_hash_senha(senha_pura: str) -> str:
    return pwd_context.hash(senha_pura)

def verificar_senha(senha_inserida: str, senha_hash_usuario: str) -> bool:
    return pwd_context.verify(senha_inserida, senha_hash_usuario)