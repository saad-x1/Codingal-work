with open('codingal.txt','w') as file:
file.write("hi i am student i like coding\n i like php \n i like python \n i like javascript"
file.close()
with open("codingal.txt", 'r') as file:
print(file.read())
file.close()
with open("codingal.txt", 'r') as file:
data=file.readlines()
print("the words are in file are")

newfile= open('newfile.txt', 'x')
newfile.close()
import os
print("checking my file exits or not")
if os.path.exists("newfile.txt"):
os.remove("fruits.txt")
else:
print("the file does not exists")
mynewfile=open("fruits.txt", "w")
mynewfile.write("\nthis is new file here")
mynewfile.write("\nthis is new file here")
mynewfile.write("\nthis is new file here")

outputfile= open("fruits.txt", 'r')
inputfile= open("newfile.txt", 'w')
line_seen_so_far=set()
for line in outputfile:
  if line not in line_seen_so_far:
    inputfile.write(line)
    line_seen_so_far.add(line)

print(line_seen_so_far)
inputfile.close()
outputfile.close()

{'\n', 'this is new line', 'this is new file here\n'}
with open("newfile.txt", 'r') as fp:

data1=fp.read()
with open("fruits.txt") as fp:
data2=fp.read()
data1+='\n'
data1+=data2
with open("mergedfile.txt", 'w') as fw:
fw.write(data1)
with open("mergedfile.txt", 'r')as fp:
print(fp.read())


