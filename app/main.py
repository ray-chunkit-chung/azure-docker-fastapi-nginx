from fastapi import FastAPI
import uvicorn
import os

# heroku only
PORT = os.environ.get('PORT', 8000)

app = FastAPI()


@app.get("/")
async def root():
    return {"Nginx": "I'm alive over TvT v9000 T.T nakimasu yametekudastop!!!"}


# heroku only
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
