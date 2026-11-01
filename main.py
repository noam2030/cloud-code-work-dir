from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

app = FastAPI(title="Hello App with UI")

# Serve static assets (CSS, images, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates setup
templates = Jinja2Templates(directory="templates")


# Web UI at root
@app.get("/", response_class=HTMLResponse)
async def ui_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# JSON API endpoint retained for programmatic access
@app.get("/api/hello")
async def api_hello():
    return {"message": "Hello, world!"}
