from flask import Flask, request, jsonify

from UserService import UserService

app = Flask(__name__)


@app.get("/users")
def get_users():
    return jsonify(UserService.get_all_users()), 200


@app.get("/users<id:int>")
def get_single_user(id):
    try:
        user = UserService.get_user(user_id=id)
        return jsonify(user), 202
    except NotImplementedError:
        return jsonify({"An error occurred": "User not found"}), 404


@app.post("/users")
def create_user():
    data = request.get_json()
    try:
        new_user = UserService.create_user(data=data)
        return jsonify(new_user), 202
    except NotImplementedError:
        return jsonify({"An error occurred": "Failed to create user"}), 401


@app.patch("/users<id:int>")
def patch_user(id):
    try:
        UserService.update_user(user_id=id)
        return jsonify({"message": "User updated successfully"}), 204
    except NotImplementedError:
        return jsonify({"An error occurred": "Invalid request"}), 400


@app.delete("/users<id:int>")
def delete_user(id):
    try:
        UserService.delete_user(user_id=id)
        return jsonify({"message": "User deleted successfully"}), 204
    except KeyError:
        return jsonify({"An error occurred": "User not found"}), 400



if __name__ == "__main__":
    app.run()
