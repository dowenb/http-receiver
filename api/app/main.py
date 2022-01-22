from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse

description = """
http-receiver accepts and stores HTTP requests so you can read them back, for testing other applications.

## Items

Items are the stored http requests.

You can send requests by posting to /

You can get the count of items stored by getting /

You can get a specific item /item/\{id\}

You can get and remove the last item with /pop

You can get the /first and /list items, without removing them

And you can delete all items with /clear
"""

app = FastAPI(
    title="http-receiver",
    description=description,
    version="0.0.1",
    contact={
        "name": "Ben Dowen",
        "url": "https://www.fullsnacktester.com",
        "twitter": "@fullsnacktester",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# TODO(sometime): Use somthing more scalable then an array, maybe some database?
items: list = []


@app.post('/')
async def add_item(
        payload: dict = Body(...)
):
    items.append(payload)
    return {"Item received"}


@app.get('/')
async def get_items():
    return {"item count": len(items)}


@app.get('/item/{item_id}')
async def get_item(item_id: int):
    try:
        return {"item": items[item_id]}
    except IndexError:
        return JSONResponse(status_code=404, content={"message": "Item not found"})


@app.get('/pop')
async def pop_item():
    return {"item": items.pop()}


@app.get('/first')
async def first_item():
    try:
        return {"item": items[0]}
    except IndexError:
        return JSONResponse(status_code=404, content={"message": "Item not found"})


@app.get('/last')
async def last_item():
    try:
        return {"item": items[-1]}
    except IndexError:
        return JSONResponse(status_code=404, content={"message": "Item not found"})


@app.delete('/clear')
async def clear_items():
    items.clear()
    return {"message": "All items cleared"}
