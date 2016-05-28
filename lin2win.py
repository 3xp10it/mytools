#换行转换
#linux下\n转换成windows下\r\n
def main():
    import sys
    input_file=sys.argv[1]
    f=open(input_file,"r+")
    urls=f.readlines()
    f.close()
    f1=open("outfile","a+")
    for url in urls:
    	print url[0:-1]
    	#print url is different with print url[0:-1]
    	#print url[0:-1] can get the pure string
    	#while print url will get the "unseen \n"
    	#this script can turn a file with strings
    	#end with \n into a file with strings end
    	#with \r\n to make it comfortable move the
    	#txt file from *nix to win,coz the file with
    	#strings end with \n in *nix is ok for human
    	#to see "different lines",but this kind of file
    	#will turn "unsee different lines" in win
    	f1.write(url[0:-1]+"\r\n")
    f1.close()

if __name__=='__main__':
    main()

