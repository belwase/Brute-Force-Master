import sys

try:
	from paramiko import SSHClient
	from paramiko import AutoAddPolicy
except ImportError:
	print 'Missing Paramiko library'
	sys.exit(0)

class SSH():

	def __init__(self,username,password,host,port,timeout):
		self.username = username
		self.password = password
		self.host = host
		self.port = port
		self.timeout = timeout
		self.connection = ''


	def connect(self):
		client = SSHClient()
		#client.load_system_host_keys()
		client.set_missing_host_key_policy(AutoAddPolicy())
		try:
			client.connect(self.host,port=int(self.port),username=self.username,password=self.password,timeout=self.timeout, allow_agent=False,look_for_keys = False)
			self.connection = 'Success'
			print 'connected'
			stdin, stdout, stderr = client.exec_command('ls')
			print stdout.read()
			client.close()
		except Exception as e:
			self.connection = 'Failed'
			print 'failed',e.message
		return self.connection
