class TodoDAO(object):
    def __init__(self):
        self.counter = 0
        self.todos = []

    def create(self, data):
        todo = data
        todo['id'] = self.counter = self.counter + 1
        self.todos.append(todo)
        return todo

    def get(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                return todo