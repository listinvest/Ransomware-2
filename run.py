import glob, os
def main():
	start = bool(input("This will run all of the ransomware in this folder! If you are not in a safe environment do not run this script.\nAre you ready to proceed? (yes/no)")
	if start:
		for fn in glob.glob("*.RANSOM"):
			os.rename(fn, fn + '.exe')
			print("Renaming " + fn + " to " + fn + ".exe")
		for fn in glob.glob("*.exe"):
			os.startfile(fn)
			print("Running " + fn)
	else:
		return
main();