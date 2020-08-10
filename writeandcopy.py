filename=input('enter file name')
orgFile=open(filename+".txt",'r+')

filename2=input('enter file name to copy')
copyfile=open(filename2,'w')
data=orgFile.read()
copyfile.write(data)
copyfile.read(data)
f.flush()
f.close()
from random import randint
rand=randint(0,2)
l=['rock','paper','scissors']
computer=l[rand]
player=False
playerwins=0
computerwins=0
while 1:
  print(rand,' ',computer)
  player=input('choose from rock ,paper,scissors')
  if player==computer:
    print('game is tie')
  elif player=='rock':
    if computer=='paper':
      print('player loose',computer,'wraps',player)
      computerwins+=1
    else:
      print('computer loose',player,'wraps',computer)
      playerwins+=1
  elif player=='paper':
    if computer=='scissors':
      print('player loose',computer,'cuts',player)
      computerwins+=1
    else:
      print('computer loose',player,'smashes',computer)
      playerwins+=1
  elif player=='scissors':
    if computer=='rock':
        print('computer loos',player,'cuts',computer)
        playerwins+=1
    else:
      print('player loose',computer,'smashes',player)
      computerwins+=1
  else:
    print('invalid option')
  playe=False
  computer=l[randint(0,2)]
  print('number of players wins',playerwins)
  print('number of computer wins',computerwins)

  
