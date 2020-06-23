import asyncio
from PyBot import PyBot

class PyBotServer:
	def __init__(self):
		self.bot = PyBot()
	async def handleConnection(self, reader, writer):
		print("connected!")
		while True:
			try:
				if self.bot == 0:
					self.bot = PyBot()
				data = await reader.readline()
				message = data.decode()
				if not message or message == '':
					continue
				print(message)
				if message == 'forward\n':
					self.bot.forward()
				elif message == 'left\n':
					self.bot.left()
				elif message == 'backward\n':
					self.bot.backward()
				elif message == 'right\n':
					self.bot.right()
				elif message == 'stop\n':
					self.bot.stop()
				elif message == 'disconnect\n':
					writer.close()
					self.bot.stop()
					break
			except asyncio.IncompleteReadError:
				continue
			except KeyboardInterrupt:
				print("exception")
				self.bot.shutdown()
				self.bot = 0
				writer.close()
				break

	async def start(self):
		print("waiting...")
		server = await asyncio.start_server(
			self.handleConnection, '0.0.0.0', 9000)

		addr = server.sockets[0].getsockname()
		print(f'Serving on {addr}')

		async with server:
			await server.serve_forever()

if __name__ == "__main__":
	server = PyBotServer()
	asyncio.run(server.start())
