import os
print(os.name)
#getcwcd() gives current directory
#
#os.chdir('d:\\')
#print(os.getcwd())

#os.chdir('slides\\')
print(os.getcwd())
#os.mkdir('superherro')
#os.mkdir('C:\R\\cod')
filename=input('enter file name')
extension=(input('enter extension'))
fname=filename+'.'+extension
#path='C:\Users\KIIT\Desktop\webandnote\6th semister\python\PythonFiles'
f=open(fname,'w')
data=input('enter data to write on file')
f.write(data)
f.flush()
f.close()

