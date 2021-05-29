from pydantic import BaseModel 

# Creating class to define the request body 
# and the type hints of each attribute 
class Measurement(BaseModel): 
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float