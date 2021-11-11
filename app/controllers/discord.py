from flask_restful import Resource


class Discord(Resource):    
    def get(self):
        return {
            "message": "get: hello from the testcontroller"
        }
