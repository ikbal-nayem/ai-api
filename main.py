from datetime import datetime
from fastapi import FastAPI, status

from services.bangladesh_holidays import getHolidaysJSON

app = FastAPI()


@app.get("/api/get-bd-gov-holidays", status_code=status.HTTP_200_OK)
async def getGovHolidays(year: int = datetime.now().year):
    return getHolidaysJSON(year)