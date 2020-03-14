import glob, os, subprocess
def main():
	start = str(input("This will run all of the ransomware in this folder! If you are not in a safe environment do not run this script.\nAre you ready to proceed? (yes/no) "))
	blocked = 0
	missed = 0
	current = 0
	
	if start == "yes":
		for fn in glob.glob("*.RANSOM"):
			print("Renaming " + fn + " to " + fn + ".exe")
			os.rename(fn, fn + '.exe')
			
		total = len(glob.glob("*.exe"))
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
				print("(" + str(current) + "/" + str(total) + ") " + fn + " blocked (" + str(round(((total - missed)/total) * 100, 2)) + "%)")
				blocked += 1
				pass
		print("\n\nResults:\n    Blocked: " + str(blocked) + "\n    Missed: " + str(missed) + "\n    Detection Score: " + str(round(((total - missed)/total) * 100, 2)) + "%.")
	else:
		return
main();