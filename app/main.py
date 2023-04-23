from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/vegetables/{name}")
def get_vegetables(name: str):
    vegetables = ["onion", "garlic", "potato"]
    if name in vegetables:
        return {"vege_name": name}
    else:
        return {"error": f"There is no {name} in the store"}