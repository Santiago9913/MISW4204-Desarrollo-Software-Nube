from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

OAuth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
