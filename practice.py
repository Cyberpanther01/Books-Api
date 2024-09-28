from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def myFirstFastApi():
    return{'putput': 'My first Api'}