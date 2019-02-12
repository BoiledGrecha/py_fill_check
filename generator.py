import os
count = 0
def go_check(list, number):
	os.system("cat /dev/null > lol.txt ")
	for i in list:
		os.system("cat tetraminos/{}.txt >> lol.txt".format(i))
		if number > 0:
			os.system("cat tetraminos/0.txt >> lol.txt")
		number -= 1
	os.system("./fillit_check* lol.txt > out_1.txt")
	os.system("./fillit_obrazech* lol.txt > out_2.txt")
	os.system("diff out_1.txt out_2.txt > difference.txt")
	fd = os.open("difference.txt", os.O_RDONLY)
	str = os.read(fd, 2)
	os.close(fd)
	if len(str) > 0:
		global count
		count += 1
		if count < 10:
			os.system("cat lol.txt >> difference2.txt")
			os.system("echo _________ >> difference2.txt")
		os.system("""echo "{}" > count_fails.txt """.format(count))

def recurs(list, num, number):
	num -= 1
	for i in range(1, 20):
		list[number - num] = i
		if num > 0:
			recurs(list, num, number)
		else:
			go_check(list, number)

def main():
	number = int(input("dai mne kolichestvo tetrimin!!!!!\n"))
	k = 0
	list = [0] * number
	number -= 1
	os.system("cat /dev/null > difference2.txt")
	os.system("cat /dev/null > count_fails.txt")
	for i0 in range(1,20):
		list[0] = i0
		recurs(list, number, number)

main()
