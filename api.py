from fastapi import FastAPI

app = FastAPI()

@app.get("/predict")
def predict(features: str):
    # Here you would call your predictive model
    return {"prediction": "your_prediction"}

# Example usage:
# Run the server and access the API at http://localhost:8000/predict?features=...
 
