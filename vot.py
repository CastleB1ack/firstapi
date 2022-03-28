from fastapi import Depends, HTTPException, APIRouter, status
from typing import List
from sqlalchemy.orm import Session
from d import get_db
import sch, tt, tok

ru = APIRouter(
    prefix='/v',
    tags=['vot'])
f = tt.vot
po= tt.pp
p = sch.vot


@ru.post("/")
def c_p(p: p, db: Session = Depends(get_db), us: int = Depends(tok.gg)) :
	popo = db.query(po).filter(po.id == p.pi).first()
	user = db.query(f).filter(f.ui == us['user_id'], f.pi == p.pi)
	if not popo :
		raise HTTPException(status_code=404, detail= 'no thing')
	elif p.vod == 1 :
		if user.first():
			raise HTTPException(status_code=403, detail= 'no more')
		n = f(ui= us['user_id'], pi= p.pi)
		db.add(n)
		db.commit()
		return {"fff":"fff"}
	else :
		if not user.first():
			raise HTTPException(status_code=403, detail= 'not')
		user.delete(synchronize_session=False)
		db.commit()
		al = db.query(f).all()
		return al

@ru.get("/",)
def g_a( db: Session = Depends(get_db), us = Depends(tok.gg)):
    al = db.query(f).all()
    return al




    	
    
    
    return n 
