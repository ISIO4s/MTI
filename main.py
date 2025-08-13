from fastapi import FastAPI,Response
from fastapi.responses import RedirectResponse
from controller import router
import security


app = FastAPI(
    title='MTI PRB'
)
app.include_router(router)
app.include_router(security.rounter)