file=open('testfile.txt','r')
print(file.read())
for i in file:
    print(i)
file2=open('write.txt','r+')
file2.write('meow')
file3=open('write.txt','+a')
file3.write('meow2')