from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get("/")
def root_path(request: Request) -> dict:
    return {
        "message": "Welcome to fastapi"
    }


if __name__ == "__main__":
    uvicorn.run("root:app", host="0.0.0.0", port= 8080, reload=True)