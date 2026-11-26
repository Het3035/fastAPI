from fastapi import FastAPI

app=FastAPI()


# Home Route 
@app.get('/')
def Home():
    return {'message':'Welcome to fastAPI'}

#About Route
@app.get('/about')
def About():
    return {'message':'This is About Page'}

#User Route
@app.get('/users')
def User():
    return {'users':['Het','Xyz','Pqr']}
