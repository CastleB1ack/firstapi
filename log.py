from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from d import get_db
import sch, tt, hashpass, tok
f  = tt.User
p  = sch.p
ph = hashpass.phs
ru = APIRouter(tags=['log'])

@ru.post('/lo')
def log(p:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
	user = db.query(f).filter(f.email == p.username).first()
	if not p :
		raise HTTPException(status_code=404, detail= 'no thing')
	if not ph.verify(p.password, user.pas):
		raise HTTPException(status_code=404, detail= 'no thing')
	at = tok.ct(d={"user_id":user.id, "user": user.email,})

	return {"g":at}  
	