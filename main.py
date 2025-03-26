from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Word"}
#teste
@app.get("/teste1234")
async def funcaoteste():
    return {"teste": "deu certo"}