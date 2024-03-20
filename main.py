from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def splash():
    return {"data": "Welcome"}


@app.get("/login")
def login():
    return {"data": {"Message":"Enter mobile number."}}

@app.get("/verify-otp")
def otpVerify ():
    return {"data": {"Message":"Enter otp number."}}