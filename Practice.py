# Task 1 — Student Marks API
# Create a FastAPI endpoint with the following requirements:
# - Endpoint: GET /students/{student_id}/marks/{marks}
# - student_id must be an integer greater than 0.
# - marks must be between 0 and 100 (inclusive).
# - Add an optional query parameter subject (string).
# - If the subject isn't provided, it should return null (or None in Python)


# from fastapi import FastAPI,Path,Query

# app=FastAPI()

# @app.get('/students/{student_id}/marks/{marks}')
# def get_details(student_id:int=Path(gt=0),marks:float=Path(le=100,ge=0),subject:str|None= Query(default=None)):
#     return(
#         {
#             'Student ID':student_id,
#             'Marks':marks,
#             'subject':subject
#         }
#     )



# Task 2 — Product Filtering API
# Difficulty: Intermediate
# Create an endpoint for filtering products.
# Requirements
# - Endpoint: GET /products/{product_id}
# - product_id must be greater than 0.
# - category is an optional query parameter.
# - price is an optional query parameter.
# - If price is provided, it must be greater than 0.
# - Return all three values in JSON.


# from fastapi import FastAPI,Path,Query


# app=FastAPI()

# @app.get('/products/{product_id}')
# def get_details(product_id:int=Path(gt=0),category:str|None=Query(default=None),price:float|None=Query(default=0,gt=0)):        
#     return {
#         'Product ID':product_id,
#         'Category':category,
#         'Price':price
#     }



# Create an endpoint:

# GET /employees/{employee_id}

# Requirements:
# - employee_id: integer, greater than 0.
# - department: optional string query parameter, maximum 20 characters.
# - salary: optional float query parameter, minimum 1000 and maximum 100000.
# - experience: optional integer query parameter, minimum 0.
# - Return all four values as JSON.

from fastapi import FastAPI,Path,Query

app=FastAPI()

@app.get('/employees/{employee_id}')
def get_details(employee_id:int=Path(gt=0),department:str|None=Query(default=None,max_length=20),salary:float|None=Query(default=None,ge=1000,le=100000),experience:int|None=Query(default=None,ge=0)):
    return{
        'Employee ID':employee_id,
        'Department':department,
        'Salary':salary,
        'Experience':experience
    }