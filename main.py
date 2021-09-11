from fastapi import FastAPI, Request, Form, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse,HTMLResponse
from pydantic import EmailStr
from deta import Deta
from typing import Optional

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

deta = Deta()
sub_db = deta.Base('opemosco_subscribers')

@app.get('/', response_class=HTMLResponse)
def index(request:Request):
    return templates.TemplateResponse('index.html', {'request': request})


#@app.get('/gallery', response_class=HTMLResponse)
#def index(request:Request):
 #   return templates.TemplateResponse('grid.html', {'request': request})

@app.post('/subscribe')
def Courses(request:Request, EMAIL: Optional[EmailStr] = Form(...)):
    user = ({
            'email':EMAIL,
            })
    sub_db.put(user)
    resp = RedirectResponse(url="/",status_code=status.HTTP_302_FOUND)
    return resp