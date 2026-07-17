from fastapi import FastAPI
# create FastAPI object
app = FastAPI()
#yeh ek GET request hai
@app.get("/")
def read_root():
    return{"message": "Mlops Server is Live!"}
#yeh ek ML model jaisa dummy endpoint hai
@app.get("/predict")
def predict_score(hours_studied:int):
    #yahan ML ka logic aayegam abhi simple math hai
    score = hours_studied * 10
    return {"Predicted_score": score}
