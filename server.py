import socket
import subprocess
import _thread
from PyBot import PyBot

class Server:
	
	def __init__(self):
		self.bot = PyBot()
		self.shouldDisconnectClient = False
	
	def start(self):
		# Connect a client socket to my_server:8000 (change my_server to the
		# hostname of your server)
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
			server_socket.bind(('0.0.0.0', 8000))
			server_socket.listen(0)

			# Make a file-like object out of the connection
			try:
				print("waiting for connection")
				connection, addr = server_socket.accept()
				print("connected!")
				with connection:
					_thread.start_new_thread(self.listenForCommands, (connection, 0))
					# Run a viewer with an appropriate command line. Uncomment the mplayer
					# version if you would prefer to use mplayer instead of VLC
					cmdline = ['vlc', '--demux', 'h264', '-']
					#cmdline = ['mplayer', '-fps', '25', '-cache', '1024', '-']
					player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
					while True:
						# Repeatedly read 1k of data from the connection and write it to
						# the media player's stdin
						data = connection.read(1024)
						#if not data:
						#	break
					player.stdin.write(data)
			except KeyboardInterrupt:
				connection.close()
				self.bot.shutdown()
				player.terminate()
				#break
			finally:
				server_socket.close()
	
	def listenForCommands(self, client, ran):
		while True:
			print("waiting for message")
			data = client.recv(1024)
			print("from client %s", data)
	
if __name__ == "__main__":
	# execute only if run as a script
	server = Server()
	server.start()
