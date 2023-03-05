# Pre-requisities

### Create new virtual environment and install the requirements
1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

## To test additional questions
1. `python additional_question.py`
2. You can see the output in the console

## To run FastAPI application
1. Goto the project directory
2. `uvicorn main:app --reload`
3. You can use the swagger UI to test the API's `http://localhost:8000/docs`
