from __init__ import *
from json import dumps
class requestAPI(create_socks):
	def __init__(self, cabundle="", default_contextx=False, buffer=4096, ssl=False, port=0) -> str:
		self.inh = create_socks(cabundle=cabundle, defcont=default_contextx, sslx=ssl, port=port).getItem
		self.option = ""
		self.verbose = False
		self.account = ""
		self.password = ""
		self.creat = [default_contextx, cabundle, ssl]
	@property
	def postReqSML(self):
		def createObjects(value:str, mem:list) -> str:
			from os import getlogin, listdir
			from platform import platform
			modules = []
			root = CreateDocument()
			root.addExplain(element="info", description="This is for API.")
			root.addRoot(function="open")
			root.add_Element(element="requestDesc", value=value)
			platform = Encipher(data=platform())
			platform.set_Memory = mem
			getlogin = Encipher(data=getlogin())
			getlogin.set_Memory = mem
			root.add_Element(element="Platform", value=platform.encryptx)
			root.add_Element(element="Username", value=getlogin.encryptx)
			root.addRoot(function="closed")
			text = root.ToStr
			return text.clear()
		memory = []
		options_known = {"myInfo":"myInformation", "delAcc":"deleteAnAccount", "getHash":"getHashfromFile", "crtAcc":"createAcc"} # The second key is the directory in the URL.
		months = {1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun", 7:"Jul", 8:"Aug", 9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"}
		weekday = {1:"Mon", 2:"Tue", 3:"Wed", 4:"Thur", 5:"Fri", 6:"Sat", 7:"Sun"}
		if self.option not in options_known:
			raise errors(errors.errosx["ITYPE"])
		datx = date(datetime.now().year, datetime.now().month, datetime.now().day)
		ksock = create_socks(cabundle=self.creat[1], defcont=self.creat[0], sslx=self.creat[2], port=0).getItem
		ksock.send(b"POST /getCipherKey HTTP/1.1\r\x0AHost: sipistoverdi.viewdns.net\r\x0AConnection: close\r\x0AUser-Agent: APISipistoverdiAutomatic-CRAWL\r\x0A\r\x0Adata=<json attribute>\r\x0A{'action':'GetCKey32bytes'}")
		data = ksock.recv(12418).decode("utf-8").split("\r\x0A\r\x0A")[1]
		main_stream_data = loads(data)["key"]
		memory.append(main_stream_data)
		rcrd = Encipher(data=dumps({"time":"%s, %s (%s) %s - %s:%s:%s GMT", "requestType":"getallinfo"})%(weekday[datx.isoweekday()], months[datetime.now().month], datetime.now().month, datetime.now().day, datetime.now().hour, datetime.now().minute, datetime.now().second))
		rcrd.set_Memory = memory
		rcrd = rcrd.encryptx
		if options_known[self.option] == "deleteAnAccount":
			road = {"no-usr":self.account == "", "no-psw":self.password == ""}
			for items in road:
				if road[items] == True:
					raise Exception("%s"%(items))
			rcrd = Encipher(data=dumps({"creds":"%s:%s"%(self.account, self.password), "requestType":"deleteAnAccount"}))
			rcrd.set_Memory = memory
			rcrd = rcrd.encryptx
		elif options_known[self.option] == "createAcc":
			creatable = {"no-username":self.account == "", "no-psw":self.password == ""}
			for items in creatable:
				if creatable[items] == True:
					raise Exception("%s"%(items))
			rcrd = Encipher(data=dumps({"creds":"%s:%s"%(self.account, self.password), "requestType":"createAcc"}))
			rcrd.set_Memory = memory
			rcrd = rcrd.encryptx
		templates = {"myInformation":createObjects(value=rcrd, mem=memory),"deleteAnAccount":createObjects(value=rcrd, mem=memory), "createAcc":createObjects(value=rcrd, mem=memory)}[options_known[self.option]]
		if self.verbose == True:
			print("[DATA] Sending data. . . | Bytes: %d!. . ."%(len(templates)))
		self.inh.send(("POST /%s HTTP/1.1\r\x0AHost: sipistoverdi.viewdns.net\r\x0AConnection: close\r\x0AUser-Agent: APISipistoverdiAutomatic-CRAWL\r\x0A\r\x0Aaction=%s"%(options_known[self.option], templates)).encode("utf-8"))
		data = self.inh.recv(214212).decode("utf-8")
		print(data)
	@postReqSML.setter
	def set_account(self, acc):
		self.account = acc[0]
		self.password = acc[1]
	@postReqSML.setter
	def set_verbose(self, newvalue_Verbose:bool):
		if type(newvalue_Verbose) != bool or isinstance(newvalue_Verbose, bool) == False:
			raise errors(errors.errorsx["ITYPE"])
		self.verbose = newvalue_Verbose
	@postReqSML.setter
	def set_option(self, newvalue_Option:str):
		if type(newvalue_Option) != str or isinstance(newvalue_Option, str) == False:
			raise errors(errors.errorsx["ITYPE"])
		self.option = newvalue_Option
