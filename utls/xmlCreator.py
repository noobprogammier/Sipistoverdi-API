from xml.dom import minidom
from os import getlogin, listdir
from platform import platform
from utls.encipher import Encipher as enc
class create_XMLObject(object):
	def __init__(self, name="requestId", value="", mem=[]) -> str:
		if type(name) != str or type(value) != str or type(mem) != list:
			self.name, self.value, self.mem = str(name), str(value), list(mem)
		else:
			self.name = name
			self.value = value
			self.mem = mem
		self.name, self.value, self.mem = self.name, self.value, self.mem
	def returnToString(self):
		root = minidom.Document()
		xml = root.createElement("root")
		rps = root.createElement("requestDesc")
		root.appendChild(xml)
		platf = enc(data=platform())
		platf.set_Memory = self.mem
		platf = platf.encryptx
		lognm = enc(data=getlogin())
		lognm.set_Memory = self.mem
		lognm = lognm.encryptx

#*WARNING*
#We'll not do anyhing HARMFULL with this information!
		"""
This information is specifically to help us recognize you!"""
		literie = [(root.createElement(self.name), self.value), (root.createElement("os-info"), platf), (root.createElement("login-name"), lognm), (root.createElement("current-count-dir"), str(len(listdir()))), (root.createElement("server"), "sipistoverdi.viewdns.net")]
		itemsx = []
		for items in literie:
			varibl = items[0]
			itemsx.append(varibl)
			varibl.setAttribute("name", items[1])
		for iss in itemsx:
			xml.appendChild(iss)
		return root.toprettyxml(indent="\t")