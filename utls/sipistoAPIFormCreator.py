from logging import warning as warn
class errorssip(Exception):
	error_tab = {"rootntf":"Make sure you've created the root attribute!", "inctype":"Incorrect type provided!", "errtype":"Item error!", "itemnotfn":"Item was not found in the current context!", "found":"There is already a root defined or closed!", "adefined":"There is an already defined element with this name!"}
class LoadAttributes():
	def __init__(self, item:str) -> str:
		tags = ["<root-open>"]
		items = [bob for bob in item.split("\r\x0A")]
		if tags[0] not in items:
			raise errorssip(errorssip.error_tab["rootntf"])
		self.obj = items
		self.item_to_look = []
	@property
	def returns(self):
		for items in self.item_to_look:
			if items not in self.obj:
				raise errorssip(errorssip.error_tab["rootntf"] + "\x20Item %s is missing!"%(items))
	@returns.setter
	def set_item_to_look(self, types:list) -> str:
		self.item_to_look = types
	def previousRoot(self):
		loads = [bob for bob in self.obj if bob == "<root-closed>"]
		if len(loads) != 0:
			raise errorssip("Root-closed is already defined - cannot proceed!")
class CreateDocument(LoadAttributes):
	def __init__(self, verbose=False):
		if isinstance(verbose, bool) == False:
			verbose = False
		else:
			verbose = verbose
		if verbose != False:
			warn(">> * WARNING * Created an instance document. . .")
		pass
		self.document = "<sipistoverdi version='0.1'>\r\x0A"
		self.encoding = "utf-8"
	def addExplain(self, element:str, description:str) -> str:
		items = [items for items in self.document.split("\r\x0A") if "INFO-TYPE" in items]
		rips = {True:"Object cannot be satisfied, because it was already satisfied!", False:"no"}
		obj = rips[len(items) > 0]
		if obj != "no":
			raise errorssip(errorssip.error_tab["errtype"] + "<\x20- -\x20>" + obj)
		if self.document.split("\r\x0A")[0] != "<sipistoverdi version='0.1'>":
			raise errorssip(errorssip.error_tab["errtype"] + "\r\x0A%s only can be set only under or defined type of the document!"%(element))
		self.document += '''<INFO-TYPE name="%s"> %s </name="%s"-closed>\r\x0A'''%(element, description, element)
	def add_Element(self, element:str, value:str) -> str:
		items = [bob for bob in self.document.split("\r\x0A") if "<name" in bob]
		for item in items:
			if element == item.split("=")[1].split(">")[0].replace('"', ""):
				raise errorssip(errorssip.error_tab["adefined"])
		rp = LoadAttributes(item=self.document)
		rp.previousRoot()
		LoadAttributes.__init__(self, item=self.document)
		self.document +=  "\r\x0A" + "\x20" * 5 + '''<name="%s">\x20%s\x20</name-closed="%s">'''%(element, value, element)
	def add_SubDesc(self, focus:str, description:str) -> str:
		if isinstance(focus, str) == False or isinstance(description, str) == False:
			raise errorssip(errorssip.error_tab["inctype"])
		item_need = [bob for bob in self.document.split("\r\x0A")]
		if "-closedINF>" in item_need[len(item_need)-2]:
			warn(">> *WARNING* %s is trying to enter after %s!"%(focus + "-ADD", item_need[len(item_need)-2]))
		item_req = [bob for bob in self.document.split("\r\x0A") if focus in bob and "<name" in bob]
		item_req = [bob.strip() for bob in item_req if focus in bob]
		required = []
		for items in item_req:
			if items.split("=")[1].split(">")[0].replace('"', "") == focus:
				required.append(items)
		if len(required) == 0:
			raise errorssip(errorssip.error_tab["itemnotfn"])
		self.document = self.document.replace(required[0], required[0] + "\r\x0A" + "\x20" * 10 + '''<description name="%s"> %s </description-closed>'''%(required[0].split(" ")[0].split("=")[1].replace('"', "").replace(">", ""), description))
	def addRoot(self, function="open") -> str:
		items = [bob for bob in self.document.split("\r\x0A")]
		if "<root-%s>"%(function) in items:
			raise errorssip(errorssip.error_tab["found"])
		attributeToStr = {"open":"\r\x0A<root-open>\r\x0A", "closed":"\r\x0A\r\x0A<root-closed>\r\x0A"}
		self.document += attributeToStr[function]
	def addDocumentRelativeOfRoot(self, optional_name:str, function:str) -> str:
		if isinstance(optional_name, str) == False or isinstance(function, str) == False:
			raise errorssip(errorssip.error_tab["inctype"])
		attributeSelector = {"open":"\r\x0A<%s-openINF>\r\x0A"%(optional_name), "close":"\r\x0A\r\x0A<%s-closedINF>\r\x0A"%(optional_name)}
		if function == "close":
			modules = [bob for bob in self.document.split("\r\x0A") if optional_name in bob]
			if modules == []:
				raise errorsip(errorssip.error_tab["rootntf"] + "\r\x0AItem: '%s' is not opened in the current instance!"%(optional_name))
		self.document += attributeSelector[function]
	def add_Logic(self, variables:list, function:str) -> str:
		items = [bob for bob in self.document.split("\r\x0A")]
		if items[len(items)-2].strip() == "<root-closed>":
			raise errorssip(errorssip.error_tab["found"])
		ItemsIferorrs = {isinstance(variables, list):"List is required as a type!", len(variables) >= 2:"At least 2 items are required!"}
		for items in ItemsIferorrs:
			if items == False:
				raise errorssip(ItemsIferorrs[items])
		notations = []
		for items in self.document.split("\r\x0A"):
			if "<name=" in items:
				impitem = items.strip().split("=")[1].split(">")[0].replace('"', "")
				for itemsx in variables:
					if itemsx == impitem:
						notations.append(items)
		if len(notations) == 0:
			raise errorssip(errorssip.error_tab["itemnotfn"] + "\x20 Make sure that you've created these items %s!"%(variables))
		paydex = "%s"%(function).join(bob for bob in variables)
		context = []
		for ims in notations:
			self.document = self.document.replace(ims, ims + "\r\x0A" + "\x20" * 20 + "<logic> '%s' </logic>\r\x0A"%(paydex))
	@property
	def ToStr(self, display=False):
		if display == True:
			print(">> Outputting current instance. . . \r\x0A\r\x0A")
		rp = LoadAttributes(item=self.document)
		rp.set_item_to_look = ["<root-open>", "<root-closed>"]
		rp.returns
		return self
	@ToStr.setter
	def set_encoding(self, arg:str):
		if isinstance(arg, str) == False:
			raise errorssip["inctype"]
		self.encoding = arg
	def clear(self):
		return self.document
	def write_file(self, file_name="test.sml") -> str:
		warn(">> Creating a file. . .")
		self.document = "\x0A".join(bob for bob in self.document.split("\r\x0A"))
		open(file_name, "w", encoding=self.encoding).write(self.document.strip())
		warn(">> File created, written lines '%d'b !"%(len(self.document)))
