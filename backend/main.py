import logging
import uvicorn
from fastapi import FastAPI, Depends
from additional_question import fetch_additional_questions
from auth import get_api_key

app = FastAPI()

app.get("/health")(lambda: {"status": "success", "msg": "OK"})


@app.post("/questions")
async def additional_questions(job_link, api_key: str = Depends(get_api_key)):
    return fetch_additional_questions(job_link)


if __name__ == "__main__":
    logging.basicConfig(
        format="{asctime} - {levelname:7} - {name} {message}",
        style="{",
        level=logging.DEBUG,
    )

    PORT = 8000
    uvicorn.run(app, host="0.0.0.0", port=PORT, log_config=None)
