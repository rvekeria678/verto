from fastapi import FastAPI, Response, status, HTTPException
import pint as pt

app = FastAPI()

@app.get('/')
async def root():
    return {"message":"Hello World"}

@app.get('/tool', status_code=200)
def convert(value: int, unit1: str, unit2: str, response: Response):
    try:
        ureg = pt.UnitRegistry()
        quantity = value * ureg(unit1)
        converted_quanitity = quantity.to(unit2)
    except HTTPException:
        response.status_code= status.HTTP_404_NOT_FOUND
        return {"error":"Resource not Found"}

    return {"message": f'Converted {quantity} to {converted_quanitity}'}
