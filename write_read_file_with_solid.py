
#defining a parent File class
class File:

    def __init__(self,filename):
        self.filename = filename

#defining a class to write a text to file

class File_writing(File):

    def __init__(self,filename):
        super().__init__(filename)

    #defining a method write in the file
    def write_in_file(self):
        try:
            with open(self.filename,'w') as file:
                print("enter text (to quit type 'quit'): ")
                while True:
                    str=input()
                    if str=='quit':
                        break
                    else:
                        file.write(str+"\n")
        except FileNotFoundError: 
            print("couldn't open the file")

class File_reading(File):
    
    def __init__(self,filename):
        super().__init__(filename)

    #defining a method read the given file
    def read_the_file(self):
        try:
            print(f'\n\n file:{self.filename}-----> \n\n')
            with open(self.filename,'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("Couldn't found the file. please try again")


#creating an object for File_writing
writeTheFile=File_writing('first.txt')

writeTheFile.write_in_file() #calling the write_in_file method

#creating an object for file_reading
readTheFile=File_reading('first.txt')

readTheFile.read_the_file() #calling the read_the_file method