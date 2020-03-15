import glob, os, subprocess
def main():
	start = str(input("This will run all of the ransomware in this folder! If you are not in a safe environment do not run this script.\nAre you ready to proceed? (yes/no) "))
	blocked = 0
	missed = 0
	current = 0
	
	if start == "yes":
		print("--------------------------------------------------------------")
		total = len(glob.glob("*.RANSOM"))
		print("Renaming " + str(total) + " samples (in some cases the AV will block renames here).")
		for fn in glob.glob("*.RANSOM"):
			try:
				current += 1
				os.rename(fn, fn + '.exe')
				print("Renamed " + fn + " to " + fn + ".exe")
			except:
				blocked += 1
				print("Rename (" + str(current) + "/" + str(total) + ") " + fn + " blocked (" + str(round(((total - missed)/total) * 100, 2)) + "%)")
				pass
		print("--------------------------------------------------------------")
		if (len(glob.glob("*.exe")) == 0):
			print("No executables to run, they've been deleted!")
			print("--------------------------------------------------------------")
			print("Results:\n    Blocked: " + str(blocked) + "\n    Missed: " + str(missed) + "\n    Detection Score: " + str(round(((total - missed)/total) * 100, 2)) + "%.")
			print("--------------------------------------------------------------")
		else:
			total = len(glob.glob("*.exe"))
			blocked = 0
			missed = 0
			current = 0
			print("Running " + str(total) + " samples.")
			for fn in glob.glob("*.exe"):
				try:
					current += 1
					p = subprocess.Popen([fn])
					result = p.wait()
					if result == 1:
						missed += 1
						print("(" + str(current) + "/" + str(total) + ") " + fn + " missed (" + str(round(((total - missed)/total) * 100, 2)) + "%)")
					else:
						blocked += 1
						print("(" + str(current) + "/" + str(total) + ") " + fn + " blocked (" + str(round(((total - missed)/total) * 100, 2)) + "%)")
				except:
					blocked += 1
					print("(" + str(current) + "/" + str(total) + ") " + fn + " blocked (" + str(round(((total - missed)/total) * 100, 2)) + "%)")
					pass
			print("--------------------------------------------------------------")
			print("Results:\n    Blocked: " + str(blocked) + "\n    Missed: " + str(missed) + "\n    Detection Score: " + str(round(((total - missed)/total) * 100, 2)) + "%.")
			print("--------------------------------------------------------------")
	else:
		return
main();