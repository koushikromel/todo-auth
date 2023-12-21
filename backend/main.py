from fastapi import FastAPI
from routes import todo as TodoRouter
from routes import todo as UserRouter


app = FastAPI()

app.include_router(TodoRouter)
app.include_router(UserRouter)
