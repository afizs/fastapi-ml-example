# Importing Necessary modules 
from fastapi import FastAPI 
import uvicorn 

from model import Measurement
from controller import clf, iris

# Declaring our FastAPI instance 
app = FastAPI() 

# Defining path operation for root endpoint 
@app.get('/')
async def root(): 
	return {'message': 'Welcome to FastAPI!'} 

# Defining path operation for /name endpoint 
@app.get('/{name}') 
async def hello_name(name : str): 
	# Defining a function that takes only string as input and output the 
	# following message. 
	return {'message': f'Welcome to FastAPI!, {name}'}


# Creating an Endpoint to recieve the data 
# to make prediction on. 
@app.post('/predict') 
async def predict(data : Measurement): 
    # Making the data in a form suitable for prediction 
    test_data = [[ 
            data.sepal_length,  
            data.sepal_width,  
            data.petal_length,  
            data.petal_width 
    ]] 
      
    # Predicting the Class 
    class_idx = clf.predict(test_data)[0] 
      
    # Return the Result 
    return { 'class' : iris.target_names[class_idx]}