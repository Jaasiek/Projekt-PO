from flask import Flask, request, jsonify
from controllers import UserService
from repository import UserRepository

app = Flask(__name__)


@app.get("/users")
def get_users():
    repo = UserRepository()
    controller = UserService(repository=repo)
    return jsonify(controller.get_all_users()), 200


@app.get("/users/<int:id>")
def get_single_user(id):
    repo = UserRepository()
    try:
        user = UserService(repository=repo).get_user(user_id=id)
        return jsonify(user), 200
    except NotImplementedError:
        return jsonify({"An error occurred": "User not found"}), 404


@app.post("/users")
def create_user():
    data = request.get_json()
    repo = UserRepository()
    try:
        new_user = UserService(repository=repo).create_user(data=data)
        return jsonify(new_user), 201
    except NotImplementedError:
        return jsonify({"An error occurred": "Failed to create user"}), 400


@app.patch("/users/<int:id>")
def patch_user(id):
    repo = UserRepository()
    data = request.get_json()
    try:
        UserService(repository=repo).update_user(user_id=id, data=data)
        return jsonify({"message": "User updated successfully"}), 200
    except NotImplementedError:
        return jsonify({"An error occurred": "Invalid request"}), 400


@app.delete("/users/<int:id>")
def delete_user(id):
    repo = UserRepository()
    try:
        UserService(repository=repo).delete_user(user_id=id)
        return jsonify({"message": "User deleted successfully"}), 202
    except KeyError:
        return jsonify({"An error occurred": "User not found"}), 400


if __name__ == "__main__":
    app.run()
