def readFile():
    filename=input('enter file name')
    f=open(filename+".txt",'r')
    #data=f.read(10)#read()--> read one line at atime
    #print(data)
    data=f.readlines()
    for line in data:
        print(line)
        
    
    f.close()
    
readFile()
