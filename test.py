from fastapi.middleware.cors import CORSMiddleware
# from fastapi.params import Body
from fastapi import FastAPI
from d import e
import curd, tt, log, posts, vot

app = FastAPI()

app.include_router(curd.ru)
app.include_router(log.ru)
app.include_router(posts.ru)
app.include_router(vot.ru)
tt.b.metadata.create_all(bind=e)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )




'''response_model=List[rp]'''







