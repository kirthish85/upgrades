from sequence import sequence

def perform_upgrade(present,next,file_name):
	
	for i in range(present,next+1):
		sequence[i](file_name)
		f=open('digest.txt','w')
		string=str(i+1)
		f.write(string)
		f.close()
def main():
	fp=open('digest.txt','r')
	file_name="share.csv"
	present_value=fp.readline()	
	fp.close()
	present_value=int(present_value)
	latest_upgrade=len(sequence)
	if latest_upgrade>=present_value:
		perform_upgrade(present_value,latest_upgrade,file_name)
	else:
		print("Nothing to upgrade")
main()
