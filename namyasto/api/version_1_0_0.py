# -----------------------------------------------------------------------------------------------
#
#       Company:    Personal Research
#       By:         Fredrick Stakem
#       Created:    8.11.16   
#
# -----------------------------------------------------------------------------------------------


# Libraries
from flask import Blueprint
from flask_restful import Api, Resource, url_for


app_v1_0_0 = Blueprint('app_v1_0_0', __name__)

@app_v1_0_0.route('/')
def version_hello():
    return 'v1.0.0'


# RAILS
# GET /photos photos#index    display a list of all photos
# GET /photos/new photos#new  return an HTML form for creating a new photo
# POST    /photos photos#create   create a new photo
# GET /photos/:id photos#show display a specific photo
# GET /photos/:id/edit    photos#edit return an HTML form for editing a photo
# PATCH/PUT   /photos/:id photos#update   update a specific photo
# DELETE  /photos/:id photos#destroy  delete a specific photo

rest_api = Api(app_v1_0_0)

class People(Resource):

    def get(self, id):
        return 'person get'

    def put(self, id):
        pass

    def post(self, id):
        pass

    def delete(self, id):
        pass

    def update(self, id):
        pass

class PeopleList(Resource):

    def get(self):
        return 'people get'

rest_api.add_resource(People, '/people/<int:id>')
rest_api.add_resource(PeopleList, '/people/all')



# Restful
class RestfulHellos(Resource):

    def get(self):
        return 'Restful hello yall'


class RestfulHello(Resource):

    def get(self, id):
        return 'Restful hello {}'.format(id)

rest_api.add_resource(RestfulHellos, '/restful_hello')
rest_api.add_resource(RestfulHello, '/restful_hello/<int:id>')