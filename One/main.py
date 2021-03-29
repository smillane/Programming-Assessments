from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

user_post_args = reqparse.RequestParser()
user_post_args.add_argument("name", type=str, help="your name", required=True)
user_post_args.add_argument("age", type=int, help="your age", required=True)
user_post_args.add_argument("email", type=str, help="your email", required=True)
user_post_args.add_argument("parentOrGuardian", type=str, help="your parent or guardian", required=False)

userDirectory = {1: {"name": "sean", "age": 28, "email": "testemail@email.com", "parentOrGuardian": "myself"}, 2: {"name": "john", "age": 28, "email": "testemail@email.com", "parentOrGuardian": "myself"}, 3: {"name": "vaughan", "age": 28, "email": "testemail@email.com", "parentOrGuardian": "myself"}}


def abort_if_no_user(user_id):
    if user_id not in userDirectory:
        abort(404, message="User does not exist")


class userId(Resource):
    def post(self):
        counter = 1
        while counter in userDirectory:
            counter +=1
        args = user_post_args.parse_args()
        userDirectory[counter] = args
        return counter, 201


class returnAllUsers(Resource):
    def get(self):
        allofdictionary = list(userDirectory.items())
        return allofdictionary, 201


class returnExistingUser(Resource):
    def get(self, user_id):
        abort_if_no_user(user_id)
        return user_id, 201


api.add_resource(returnExistingUser, "/api/user/<int:user_id>")
api.add_resource(userId, "/api/user")
api.add_resource(returnAllUsers, "/api/users")

if __name__ == "__main__":
    app.run(debug=True)
