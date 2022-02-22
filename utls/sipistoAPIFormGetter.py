from threading import Thread as newthread
from time import sleep
from sys import stdout
from itertools import cycle
from utls.tempfiles import *
from logging import warning as warn
global lod
lod = "No current items"
class errors(Exception):
	error_tab = {"VERFAIL":"Failure. Make sure that your version is <sipistoverdi version='0.1'> in order to proceed, otherwise remote server might not respond correctly!",
	"INCUSG":"Incorrect usage!"}
	notify = {}
	notify["missing '<' (INF)"] = "Please make sure nex time that INFO-TYPE has '<' (usually described as left-arrow) before defining the actual function! This is a warning. We are fixing it right away!"
class get_Items(errors):
	def __init__(self, document:str, verbose=False, lod=lod) -> str:
		def load_cycle_start():
			subs = ""
			items = 0
			while len(decent) == 0:
				for blob in cycle(["|", "/", "-", "\\"]):
					if items >= prepare[0]:
						decent.append("1")
						break 
					stdout.write("\r[DATA] Loading items [%s] "%(lod) + blob + " !\r")
					stdout.flush()
					items += 1
					sleep(1)
		lines = 0
		loaded_attributes = {}
		for items in document.split("\n"):
			lines += 1
			loaded_attributes[lines] = items
		self.fetched_in_lines = loaded_attributes
		if verbose == True:
			print("[DATA] Total lines gathered %d! [%s]"%(len(self.fetched_in_lines), ",".join('"' + str(bob) + '"' for bob in self.fetched_in_lines)))
			print("\r\x0A[DATA] Preparing to make checks. . .")
			prepare.append(len(self.fetched_in_lines))
			for io in range(1):
				xz_ = newthread(target=load_cycle_start)
				off.append(xz_)
				xz_.start()
		enumerated = []
		for items in [("<sipistoverdi", "<sipistoverdi version='0.1'>", None, errors.error_tab["VERFAIL"]), ("INFO-TYPE", "<INFO-TYPE", "starts", errors.error_tab["INCUSG"])]:
			#exact_line = 0
			reps = items[0]
			exact_line = [bob for bob in self.fetched_in_lines if reps in self.fetched_in_lines[bob]][0]
			enumerated.append(exact_line)
			rip = "Checking for line '%d'. . . - "%(exact_line)
			if items[0] in self.fetched_in_lines[exact_line] and exact_line != 0:
				oldx = self.fetched_in_lines[exact_line]
				if items[2] != "starts":
					rope = {"x":items[1] == oldx}
					if rope["x"] == False:
						if verbose == True:
							rip += " Failure! %s - Problem Fixed [+]"%(items[3])
							self.fetched_in_lines[exact_line] = self.fetched_in_lines[exact_line].replace(self.fetched_in_lines[exact_line], items[1])
							stdout.flush()
							off[0].join(timeout=5)
					else:
						if verbose == True:
							rip += " OK"
							stdout.flush()
							off[0].join(timeout=5)
				else:
					rope = {"x":oldx.startswith(items[1])}
					if rope["x"] == False:
						if verbose == True:
							rip += " Failure! %s - Problem Fixed [+] "%(items[3])
							stdout.flush()
							self.fetched_in_lines[exact_line] = self.fetched_in_lines[exact_line].replace(self.fetched_in_lines[exact_line], items[1])
							off[0].join(timeout=5)
					else:
						if verbose == True:
							rip += "OK"
							stdout.flush()
							off[0].join(timeout=5)
				if verbose == True:
					print(rip)
					stdout.flush()
		"""
These are string formatting tests, in order to see if there are any errors and to try to fix them."""
		old_stack = {}
		for items in self.fetched_in_lines:
			old_stack[items] = self.fetched_in_lines[items]
		del self.fetched_in_lines[enumerated[0]]; del self.fetched_in_lines[enumerated[1]]
		cleaned_up = {}
		for items in self.fetched_in_lines:
			if self.fetched_in_lines[items] != "":
				cleaned_up[items] = self.fetched_in_lines[items].strip()
		all_map = []
		other_stuff = []
		for checks in ["<root-open>", "<root-closed>"]:
			exct = [bob for bob in cleaned_up if checks in cleaned_up[bob]]
			if exct == [] or len(exct) == 0:
				line = "?"
				if verbose == True:
					rip = "Checking for line '%s'. . . - Failed! Adding root attribute now (%s). . . "%(line, checks)
					off[0].join(timeout=5)
				else:
					warn("Adding root attribute now (%s). . .."%(checks))
				cleaned_up[enumerated[1]+1] = checks
			else:
				all_map.append((checks, exct[0]))
		for items in cleaned_up:
			if items != all_map[0][1] and items != all_map[1][1]:
				other_stuff.append((cleaned_up[items], items))
		targets = {}
		counter = 0
		for cleansie in other_stuff:
			if cleansie[0].startswith("<name") == True:
				if cleansie[1] not in targets:
					targets[cleansie[1]] = (cleansie[0].split("=")[1].split(">")[0].replace('"', ""), cleansie[0].split(">")[1].split("<")[0])
				else:
					targets[cleansie[1] + str(counter)] = (cleansie[0].split("=")[1].split(">")[0].replace('"', ""), cleansie[0].split(">")[1].split("<")[0])
				if verbose == True:
					print("Checking for line '%s' . . . - Item :: %s, Variable :: %s, type of item :: %s. . ."%(cleansie[1], cleansie[0].split(">")[1].split("<")[0], cleansie[0].split("=")[1].split(">")[0].replace('"', ""), cleansie[0].split("=")[0].split("<")[1]))
					off[0].join(timeout=5)
			elif cleansie[0].startswith("<description") == True:
				if cleansie[1] not in targets:
					targets[cleansie[1]] = (cleansie[0].split("=")[1].split(">")[0].replace('"', ""), cleansie[0].split(">")[1].split("<")[0])
				else:
					targets[cleansie[1] + str(counter)] = (cleansie[0].split("=")[1].split(">")[0].replace('"', ""), cleansie[0].split(">")[1].split("<")[0])
				if verbose == True:
					print("Checking for line '%s' . . . - Item :: %s, Variable :: %s, type of item :: %s. . ."%(cleansie[1], cleansie[0].split(">")[1].split("<")[0], cleansie[0].split("=")[1].split(">")[0].replace('"', ""), cleansie[0].split("=")[0].split("<")[1]))
					off[0].join(timeout=5)
			counter += 1
		rips = {}
		counter = 0
		for itemx in targets:
			if targets[itemx][0] not in rips:
				rips[targets[itemx][0]] = targets[itemx][1].strip()
			else:
				rips[targets[itemx][0] + "-" + str(counter)] = targets[itemx][1].strip()
			counter += 1
		if verbose == True:
			print("\r\x0A\r\x0A" + "\x2D"*30 + "\r\x0A" + "|\x20" + "Reading process completed!" + "\x20"*2  + "|"  + "\r\x0A" + "\x2D"*30 + "\r\x0A" + "\r\x0A" + "\r\x0ALegend" + "\r\x0A"  + "\r\x0A"+ "| Variables" + "\x20" * 19 + "|"  + "\r\x0A" + "\x2D"*30  + "\r\x0A" + "|" + "Total variables read: %s "%(lines) + "\x20"*4 + "|" + "\r\x0A\r\x0A")
		self.items = rips
	@property
	def ToDict(self):
		return self.items
"""data = get_Items(document='''
<sipistoverdi version='0.1'>
<INFO-TYPE name="info"> This is for API. </name="info"-closed>

<root-open>

     <name="requestDesc"> Q9BwBA8eJ//6/3Icp+ogEsLjln9k5ihe9iYCyDu8SmlSMMfp6PfjZzyXKH10olEAK/0GLV6wFwl7NHdx9t8ivdPKoYeLMA== </name-closed="requestDesc">
     <name="Platform"> b5tqCQ0Mdujr7QtY8ugwepa4hmNk4ls89A== </name-closed="Platform">
     <name="Username"> aod3AQMV </name-closed="Username">

<root-closed>''', verbose=True)
print(data.ToDict)
"""

