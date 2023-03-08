from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Nginx": "I'm alive over TvT v9000 T.T nakimasu yametekudastop!!!"}
