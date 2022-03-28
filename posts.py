from fastapi import Depends, HTTPException, APIRouter, status
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import func
from d import get_db
import sch, tt, tok

ru = APIRouter(
    prefix='/p',
    tags=['post'])
f = tt.pp
p = sch.pv
#
@ru.get("/",  response_model=List[p])
def g_a( db: Session = Depends(get_db), us = Depends(tok.gg)):
    al = db.query(f, func.count(tt.vot.pi).label("vot")).join(tt.vot, tt.vot.pi==f.id, isouter=True).group_by(f.id).all()
    return al

@ru.post("/")
def c_p(p:p, db: Session = Depends(get_db), us: int = Depends(tok.gg)) :  
    n = f(**p.dict(), em = us['user'])
    db.add(n) 
    db.commit()
    db.refresh(n)
    return n 

@ru.get('/{id}')
def g_i (id:int, db: Session = Depends(get_db)) :
    p = db.query(f, func.count(tt.vot.pi).label("vot")).join(tt.vot, tt.vot.pi==f.id, isouter=True).group_by(f.id).filter(f.id == id).first()
    if not p :
        raise HTTPException(status_code=404, detail= 'no thing')
    return p

@ru.delete('/{id}')
def d_i (id:int, db: Session = Depends(get_db), us = Depends(tok.gg)) :

    po = db.query(f).filter(f.id == id)
    p = po.first()
    if not p :
        raise HTTPException(status_code=404, detail= 'no thing')
    if us.get('user') != p.em :
        raise HTTPException(status_code=403, detail= 'no thing')        
    
    po.delete(synchronize_session=False)
    db.commit()
    al = db.query(f).all()
    return al

@ru.put('/{id}')
def p_i (p:p, id:int, db: Session = Depends(get_db), us = Depends(tok.gg)) :
    post = db.query(f).filter(f.id == id)

    if not post :
        raise HTTPException(status_code=404, detail= 'no thing')
    post.update(p.dict(),synchronize_session=False)
    db.commit()
    al = db.query(f).all()
    return al
