class Encipher(object):
	def __init__(self, data:str):
		self.memory = []
		self.data = data
	@property
	def encryptx(self):
		from Cryptodome.Cipher.AES import new, MODE_GCM; from base64 import b64encode, b64decode
		new = new(self.memory[0].encode("utf-8"), MODE_GCM, self.memory[0].encode("utf-8")).encrypt(self.data.encode("utf-8"))
		return b64encode(new).decode("utf-8")
	@encryptx.setter 
	def set_Memory(self, newval:list):
		if isinstance(newval, list) == False:
			exit()
		self.memory = newval