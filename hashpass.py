from passlib.context import CryptContext

phs = CryptContext(schemes=["bcrypt"], deprecated="auto")
