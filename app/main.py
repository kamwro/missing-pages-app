from fastapi import FastAPI
from starlette.responses import JSONResponse
from . import functions


app = FastAPI(
    title="Missing pages and duplicates",
    description="To get started you need to have installed python and docker, check the README file for the commands.",
)

origins = ["http://localhost"]


@app.get(
    "/", summary="Click to show the missing page numbers and duplicates", tags=["Start with CSV file"]
)
async def get_the_results() -> JSONResponse:
    numbers: list = functions.get_list_from_csv()
    numbers = functions.get_page_numbers(numbers)
    numbers_info = functions.get_sorted_numbers_and_duplicates_info(numbers)
    sorted_and_unique_numbers = numbers_info["numbers"]
    duplicates = numbers_info["duplicates"]
    missing_numbers = functions.get_missing_numbers(sorted_and_unique_numbers)
    return JSONResponse(
        status_code=200,
        content={"Missing numbers": missing_numbers, "Duplicates": duplicates}
    )

