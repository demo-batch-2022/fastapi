from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data = {
    "vineeth" : "fintelix",
    "venkat" : "bootlabs",
    "nivi" : "itc"
}


@app.get("/{name}")
def getUser(name):
    company_name = data[name]
    return {"message": company_name}
