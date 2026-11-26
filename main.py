from fastapi import FastAPI,Path

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
# Dynamic Path
@app.get('/users/{user_id}')
def get_users(user_id:int):
    return {"user ID":user_id}


# Path Parameters
# Path Parameter with String
@app.get('/products/{product_name}')
def get_product(product_name:str):
    return {"Product Name":product_name}

# Multiple Path Parameter
@app.get('/students/{student_id}/marks/{marks}')
def get_marks(student_id:int,marks:float):
    return {'Student ID':student_id,
            'Marks:':marks
            }
# Path Parameters with Validation

@app.get('/students/{student_id}/marks/{marks}')
def get_marks(student_id:int=Path(gt=0,max_length=12,min_length=12),
              marks:float=Path(ge=0,le=100)):
    return {'Student_ID':student_id,
            'Marks':marks}
