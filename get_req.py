from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow React app to talk to backend
app = FastAPI(
    title="Code Review Platform",
    description="Analyze code for bugs and security issues",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to Code Review Platform"}

@app.get("/health")
def health():
    return {"status": "alive"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}!"}
