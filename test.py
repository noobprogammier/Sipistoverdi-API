from utls.sipistoAPIFormCreator import *
from utls.sipistoAPIFormGetter import *
class LoadDocs(get_Items):
	def __init__(self):
		self.docs = ""
	@property
	def results(self):
		get = get_Items(document=self.docs, verbose=False, lod=[]).ToDict
		print(get)
	@results.setter
	def set_Document(self, new:str) -> str:
		self.docs = new
class CreateDocs(CreateDocument):
	def __init__(self):
		root = CreateDocument()
		"""
addExplain -  will create an attribute for basically explaining a specific object. Naming the actual
context, like a title.
addRoot  - will create the root heading, which is important!
add_Element - will create a variable.
add_SubDesc - will create a focus attribute, which will focus in a variable in the context.
	"""
		root.addExplain(element="Information", description="Hello, from Sipistoverdi. Greetings, Github user!")
		root.addRoot(function="open")
		root.add_Element(element="Github", value="Github is the best platform!")
		root.add_SubDesc(focus="Github", description="Github has many users, and they are thankful!")
		root.add_Element(element="Test", value="That is other variable")
		root.add_SubDesc(focus="Test", description="A description for Test.")
		root.addRoot(function="closed")
		self.docs = root.ToStr
	@property
	def results(self):
		return self.docs.clear()
if __name__ == "__main__":
	created = CreateDocs().results
	print(created)
	#print(created)
	getter = LoadDocs()
	getter.set_Document = created
	getter.results
	