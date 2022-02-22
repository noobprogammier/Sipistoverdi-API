from socket import AF_INET, SOCK_STREAM, getprotobyname, socket, SOL_SOCKET, SO_REUSEADDR, gethostbyname, gethostname
from logging import info as inf, warning as warn, error as err
import ssl # A little bit slowlier will be
"""
But I had a little problem with the ssl library - I will try to solve it."""
class errors(Exception):
	errorsx = {}
	errorsx["Incorrect call!"] = "Incorrect call!"; errorsx["Incorrect call #2 !"] = "Incorrect call!"; errorsx["ONOPT"] = ">> One only option is *recommended* !"; errorsx["TYPN"] = ">> Type not found!"; errorsx["ITYPE"] = ">> Invalid type!"
	pass 
class create_socks():
	def __init__(self, cabundle:str,defcont:bool, sslx:bool, port:int):
		inf("[DATA] >> Creating socket. . .")
		self.sock = socket(AF_INET, SOCK_STREAM, 6)
		if cabundle == "" and defcont == False:
			"""
We also implemented the port trick here, which allows you to set a custom port and connect to the service/server with it!
"""
			if port == 0:
				"""
Here it will by default set you a connectivity port.
For this option, it is advised to disable adapters which might lead to collisions!
"""
				self.sock.connect(("sipistoverdi.viewdns.net", 8080))
			else:
				self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
				try:
					self.sock.bind((gethostbyname(gethostname()), port))
					self.sock.connect(("sipistoverdi.viewdns.net", 8080))
				except:
					err(">> We encountered and error, while doing this option! Please make sure that everything is correct. . . Setting port to automatic by default (0).  . .")
					new_sock = socket(AF_INET, SOCK_STREAM, 6)
					new_sock.connect(("sipistoverdi.viewdns.net", 8080))
					self.sock = new_sock
			inf("Successfully connected to sipistoverdi.viewdns.net!")
		else:
			scenario = {">> Incorrect call!":cabundle == "" and defcont == False, "ONOPT":cabundle != "" and defcont == True}
			for items in scenario:
				if scenario[items] == True:
					raise errors(errors.errorsx[items])
			if sslx != True and cabundle != "" or defcont != False:
				warn(">> This option will be soon depracated, and you should and will provide correct calls. . .")
			self.sock.connect(("sipistoverdi.viewdns.net", 8443))
			def_cont = ssl.SSLContext()
			"""
sipistoverdi.viewdns.net:443, fully supports only TLS version 1.3, we do not support any versions below 1.3 !
"""
			def_cont.minimum_version = ssl.TLSVersion.TLSv1_3; def_cont.maximum_version = ssl.TLSVersion.TLSv1_3; def_cont.verify_mode = ssl.CERT_REQUIRED; ssl.check_hostname = True; def_cont.load_default_certs()
			self.sock = def_cont.wrap_socket(self.sock, server_hostname="sipistoverdi.viewdns.net")
	@property
	def getItem(self):
		return self.sock

