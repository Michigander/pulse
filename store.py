from observable import Observable


class Store(Observable):
    def __init__(self):
        super().__init__()
        self.state = {'users': []}
        
    def send(self, message, connection_id):
        if message['type'] == 'connected':
            self.state = {
                'users': [*self.state['users'], connection_id]
            }

        self.notify(self.state)
