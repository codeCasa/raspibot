import asyncio
from PyBot import PyBot

class PyBotServer:
	def __init__(self):
		self.bot = PyBot()
	async def handleConnection(self, reader, writer):
		while True:
			try:
				data = await reader.readline()
				if not data:
					continue
				message = data.decode()
				print(message)
				if message == 'forward':
					self.bot.forward()
				elif message == 'left':
					self.bot.left()
				elif message == 'backward':
					self.bot.backward()
				elif message == 'right':
					self.bot.right()
				elif message == 'stop':
					self.bot.stop()
				elif message == 'disconnect':
					writer.close()
					self.bot.stop()
					break
			except KeyboardInterrupt:
				writer.close()
				break

	async def start(self):
		print("wating...")
		server = await asyncio.start_server(
			self.handleConnection, '0.0.0.0', 9000)

		addr = server.sockets[0].getsockname()
		print(f'Serving on {addr}')

		async with server:
			await server.serve_forever()

if __name__ == "__main__":
	server = PyBotServer()
	asyncio.run(server.start())
