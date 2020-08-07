from flask import Flask
from flask_restplus import Api, Resource, fields
from tododao import TodoDAO

app = Flask(__name__)
api = Api(app, version='1.0', title='Todo API Demo', description='Perform the operations for ToDo API')

ns = api.namespace('todos', description='todo operations')

DAO = TodoDAO()

todo_model = api.model('ToDoModel', {
    'id': fields.Integer(readonly=True, description='Todo task unique identifier', example=9999),
    'task': fields.String(required=True, description='Todo task details', example='some sample task description')
})

@ns.route('/')
class ToDoList(Resource):

    @ns.expect(todo_model, validate=True)
    @ns.marshal_with(todo_model, code=201)
    @ns.response(code=500, description= 'Unable to create a todo task')
    def post(self):
        return DAO.create(api.payload), 201

    @ns.response(code=500, description= 'Unable to get all the tasks')
    @ns.marshal_list_with(todo_model, code=200)
    def get(self):
        return DAO.todos, 200

@ns.route('/<int:id>')
class ToDo(Resource):

    @ns.response(code=404, description= 'Todo task not found')
    @ns.response(code=500, description= 'Unable to get task details')
    @ns.marshal_with(todo_model, code=200)
    def get(self, id):
        return DAO.get(id), 200


if __name__=='__main__':
    app.run(debug=True)