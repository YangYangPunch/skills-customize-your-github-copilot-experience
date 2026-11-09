from fastapi import FastAPI

app = FastAPI(title="Task API")

items = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build a REST API", "done": True},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API"}


# TODO: Add endpoints for listing items, getting one item, and creating items
