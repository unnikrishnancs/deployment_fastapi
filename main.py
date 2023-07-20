from fastapi import FastAPI
from typing import Union
import uvicorn
from pydantic import BaseModel
from predict_simple_interest import *


'''
----------START ------------------------
Self-hosting JavaScript and CSS for docs
----------------------------------------
'''



from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.staticfiles import StaticFiles


app = FastAPI(docs_url=None, redoc_url=None)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )



''' 
---------------------  END ------------------------
---------------------------------------------------
'''


# define name and type for calculating simple interest
class intrest_input(BaseModel):
 principle:float
 rate:float
 no_of_yrs:int


@app.get("/")
def index():
 return {"Index Page!!! Add /docs in url to get Swagger UI"}


@app.post("/api/predict/")
def predict_interest(intrest:intrest_input):
 
 p=float(intrest.principle)
 r=float(intrest.rate)
 t=float(intrest.no_of_yrs)
 
 i=predict_si(p,r,t)
 return {"simple interest":"{:.2f}".format(i)}



if __name__=="__main__":
 uvicorn.run(app,port=8000)

