import glob, os, subprocess
def main():
	start = str(input("This will run all of the ransomware in this folder! If you are not in a safe environment do not run this script.\nAre you ready to proceed? (yes/no) "))
	blocked = 0
	missed = 0
	
	if start == "yes":
		for fn in glob.glob("*.RANSOM"):
			print("Renaming " + fn + " to " + fn + ".exe")
			os.rename(fn, fn + '.exe')
		print("Running " + str(total) + " samples.")
		
		total = len(glob.glob("*.exe"))
		for fn in glob.glob("*.exe"):
			try:
				p = subprocess.Popen([fn])
				result = p.wait()
				print(result)
				if result == 1:
					print(fn + " missed")
					missed += 1
				else:
					print(fn + " blocked (" + str(round(((total - missed)/total) * 100, 2)) + "%)")
					blocked += 1
			except:
				print(fn + " blocked (" + str(round(((total - missed)/total) * 100, 2)) + "%)")
				blocked += 1
				pass
		print("Results:\nBlocked: " + str(blocked) + "\nMissed: " + str(missed) + "\nDetection Score: " + str(round(((total - missed)/total) * 100, 2)) + "%.")
	else:
		return
main();