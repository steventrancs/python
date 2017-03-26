import os
import sys
import shutil

src  = sys.argv[1]
dest = sys.argv[2]

print src, dest

def cp_file(src, dest):
	if not os.path.isfile(src):
		print src + " isn't file or don't exists!!!"
	elif not os.path.exists(dest):
		print dest + " not exists!!!"
	else:
		shutil.copy2(src, dest)
		print "cp {0} {1} \n*******************\n**   DONE !!!!   **\n*******************".format(src, dest)   
cp_file(src, dest) # main process