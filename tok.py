from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
sect = "b4y546546b4b36e0y23n65b456b4b989oks3qv43v3vb5b"
alg = "HS256"
ti = 30
oo = OAuth2PasswordBearer(tokenUrl='lo')


def ct (d) :
	d = d.copy()
	de = jwt.encode(d,sect,algorithm=alg)
	return de

def ve (to:str, err):
	try :
		id :int = jwt.decode(to,sect,algorithms=[alg])
		return id
	except JWTError:
		raise err

def gg (to:str = Depends(oo)) :
	err = HTTPException(status_code=401, detail= 'no auuuuu')

	return ve(to,err)




