def func(file_name):
	dig=open("digest.txt","w")
	dig.write("2")
	dig.close()
	suffix = ',None'

	with open(file_name, 'r+') as src:
	    with open(file_name, 'r+') as dest:
	       for line in src:
		   dest.write('%s%s\n' % ( line.rstrip('\n'), suffix))










