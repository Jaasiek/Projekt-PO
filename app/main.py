from flask import Flask, request


app = Flask(__name__)

@app.get("/users")
def get_users():
    pass

@app.get("/users<id:int>")
def get_single_user():
    pass

@app.post("/users")
def create_user(id):
    pass

@app.patch("/users<id:int>")
def patch_user(id):
    pass

@app.delete("/users<id:int>")
def delete_user(id):
    pass

