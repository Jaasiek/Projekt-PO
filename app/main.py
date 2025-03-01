from flask import Flask, request, jsonify

import UserService


app = Flask(__name__)

@app.get("/users")
def get_users():
    return jsonify(UserService.get_all_users()), 200

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

