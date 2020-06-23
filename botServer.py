import asyncio
from PyBot import PyBot

class PyBotServer:
	def __init__(self):
		self.bot = PyBot()
	async def handleConnection(reader, writer):
		data = await reader.read(1024)
		message = data.decode()
		print("from client %s", message)

	async def start(self):
		server = await asyncio.start_server(
			handleConnection, '0.0.0.0', 9000)

		addr = server.sockets[0].getsockname()
		print(f'Serving on {addr}')

		async with server:
			await server.serve_forever()

if __name__ == "__main__":
	server = PyBotServer()
	asyncio.run(server.start())
