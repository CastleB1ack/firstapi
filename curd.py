from fastapi import Depends, HTTPException, APIRouter, status
from typing import List
from sqlalchemy.orm import Session
from d import get_db
import sch, tt, hashpass

ph = hashpass.phs
ru = APIRouter(
    prefix='/u',
    tags=['users'])
f = tt.User
p = sch.p

@ru.get("/", ) 
def g_a(db: Session = Depends(get_db)):
    al = db.query(f).all()
    return al

@ru.post("/")
def c_p(p:p, db: Session = Depends(get_db)) :
    h = ph.hash(p.pas)
    p.pas = h
    n = f(**p.dict())
    db.add(n)
    db.commit()
    db.refresh(n)
    return n 

@ru.get('/{id}')
def g_i (id:int, db: Session = Depends(get_db)) :
    p = db.query(f).filter(f.id == id).first()
    if not p :
        raise HTTPException(status_code=404, detail= 'no thing')
    return p

@ru.delete('/{id}')
def d_i (id:int, db: Session = Depends(get_db)) :
    p = db.query(f).filter(f.id == id)
    if not p :
        raise HTTPException(status_code=404, detail= 'no thing')
    p.delete(synchronize_session=False)
    db.commit()
    al = db.query(f).all()
    return al

@ru.put('/{id}')
def p_i (p:p, id:int, db: Session = Depends(get_db)) :
    post = db.query(f).filter(f.id == id)

    if not post :
        raise HTTPException(status_code=404, detail= 'no thing')
    post.update(p.dict(),synchronize_session=False)
    db.commit()
    al = db.query(f).all()
    return al

@ru.post("/")
def c_p(p:p, db: Session = Depends(get_db)) :
    h = ph.hash(p.pas)
    p.pas = h
    n = f(**p.dict())
    db.add(n)
    db.commit()
    db.refresh(n)
    return n 