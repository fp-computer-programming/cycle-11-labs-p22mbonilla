# Author MB 02/08/2022

my_file = open("alma_mater.txt", "r")
while True:
     line = my_file.readline()
     if len(line) == 0:
           break
     print (line, end="")
my_file.close()