"""string = input("Enter any string: ")
c = input("Enter character to check frequency: ")
count = 0
for i in string:
    if i ==c:
        count+=1
print(c,"occurs", count, "time(s).")
# using count method
string_data = input("Enter a string:")
#using count method
for chr in string_data:
    print(chr,"occured",string_data.count(chr),"times")"""
#no repeation chr for using this formula
string_data = input("Enter a string:")
list1=[]
for chr in string_data:
    if chr not in list1:
        list1.append(chr)
        print(chr, "occured", string_data.count(chr), "times")


