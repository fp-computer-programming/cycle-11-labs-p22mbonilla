# Author MB 02/08/2022

my_file = open("alma_mater.txt")
while True:
    line = my_file.readline()
    line.reverse()
    for x in line:
        print(x)
        print("-")
my_file.close()
