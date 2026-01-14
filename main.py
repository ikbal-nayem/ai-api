from datetime import datetime
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from middlewares.CORS import origins

from services.bangladesh_holidays import getHolidaysJSON

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/get-bd-gov-holidays", status_code=status.HTTP_200_OK)
async def getGovHolidays(year: int = datetime.now().year):
    return getHolidaysJSON(year)