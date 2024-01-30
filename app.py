from flask import Flask, request


# Creates and runs Flask App 
app = Flask(__name__)


stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]



# Get store object
@app.get("/store")
def get_store_object():
    return {"stores": stores}


# Get store 
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:                  
        if store["name"] == name:
            return store
        
    return {"message": "Store not found"}, 404


# Get store items
@app.get("/store/<string:name>/item")
def get_store_items(name):
    for store in stores:                  
        if store["name"] == name:
            return {"items": store["items"]}
        
    return {"message": "Store not found"}, 404



# Create store
@app.post("/store")
def create_store():
    request_data = request.get_json() # get data from request
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

# Create item in store
@app.post("/store/<string:name>")
def create_item(name):
    request_data = request.get_json()           # get data from request
    for store in stores:                        # iterate through list to find store then create/append item
        if store["name"] ==name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
        
    return {"message": "Store not found"}, 404