file = open('test.txt')
"""print(file.read())
##rint(file.readline())
#p#rint(file.readline())
                                         #using while and for loop method and result will be same
line = file.readline()
while line !="":

    print(line)
    line= file.readline()"""

for line in file.readlines():
    print(line)




file.close()