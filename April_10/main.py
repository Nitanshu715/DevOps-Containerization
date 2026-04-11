from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "name": "Nitanshu Tak",
        "sapid": "500121943",
        "Location": "Dehradun"
    }

@app.get("/{data}")
def read_data(data: str):
    return {
        "data": data,
        "Location": "Dehradun"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80)