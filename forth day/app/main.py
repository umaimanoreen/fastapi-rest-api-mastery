from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
app = FastAPI()


class Item_not_found(Exception):
    def __init__(self, item_id):
        self.item_id = item_id


@app.exception_handler(Item_not_found)
def item_not_found_exception_handler(request: Request, exc: Item_not_found):
    return JSONResponse(
        status_code=404,
        content={"message": f"Item {exc.item_id} not found"}
    )


@app.get("/items/{item.id}")
def get_item(item_id: int):
    if item_id != 1:
        raise Item_not_found(item_id)
    return {"item_id ": item_id}

