from fastapi import FastAPI,Path


app=FastAPI()

@app.get('/users')
def get_name(name):
    return {'Name':name}
