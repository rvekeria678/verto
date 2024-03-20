from fastapi import FastAPI, Response
import pint

app = FastAPI()

@app.get('/')
async def root():
    return {"message":"Hello World"}

@app.get('/tool')
def convert(value: int, unit1: str, unit2: str):

    try:
        ureg = pint.UnitRegistry()
        quantity = value * ureg(unit1)
        converted_quanitity = quantity.to(unit2)
    except AttributeError:
        print("invalid inputs")
        return {"message": f'Invalid Inputs'}

    return {"message": f'Converted {quantity} to {converted_quanitity}'}
