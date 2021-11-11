from flask_restful import Resource


class Discord(Resource):
    def post(self):
        print(self.post)
