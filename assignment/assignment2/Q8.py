def write_file():
	w_write = open("testfile.txt", 'w')
	w_write.write(raw_input("enter u text here"))
	w_write.close()
write_file()
def read_file():
	r_read = open("testfile.txt", 'r')
	print_file  = r_read.read()
	print print_file
read_file()