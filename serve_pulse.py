import asyncio

import application


if __name__ == "__main__":    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(application.apply())
