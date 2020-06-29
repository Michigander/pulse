from communicator import Communicator
from interpreter import Interpreter
from server import Server
from manager import Manager
from service import Service
from store import Store


async def apply(host='localhost', port='5432'):
    # this should be simplified into a one line declaration of Store or 
    # some subclass or composition, then pass the single arg to server
    store = Store()
    communicator = Communicator(store)
    interpreter = Interpreter(store)

    # this could probably be simplified by giving manager a default
    # value in Service
    server = Server(host, port, interpreter, communicator)
    manager = Manager()
    service = Service(manager, server)
    
    await service.run()

