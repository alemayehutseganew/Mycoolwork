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

  
  import os
import pickle as p
import random as r
import datetime as t

path = 'C:\Users\KIIT\Desktop\ATMtemam'
os.mkdir('atmInfo')

acctinfo = {}

#function to perform all the operation
def register():
  print("enter your account Detail.....")
  name = input("enter your name=>")
  acctno = int(input('enter your 4 digit account number=>'))
  amount = int(input('enter your first time deposit=>'))
  newpin = r.randint(100,999)
  print("Registration successfull!!")
  print("Note your new pin=>",newpin)
  acctinfo = {'name':name,'acctno':acctno,'pin':newpin,'amount':amount}
  filename = open('atmInfo/'+str(acctno)+'.pkl','wb+')
  p.dump(acctinfo,filename)
  filename.close()
  print("your acct detail has saved")
  ATM()

def deposit():
  acctno = int(input('please enter your acount number=>'))
  try:
    readfile = open('atmInfo/'+str(acctno)+'.pkl','rb+')
    data = p.load(readfile)
    def pinRequest():
      upin = int(input('enter your pin=>'))
      if(upin!=data['pin']):
        print("Invalid pin please enter valid pin!!")
        pinRequest()
    pinRequest()

    damt = int(input('enter amount to deposit=>'))
    if(damt%100==0 and damt>=100):

      data['amount'] = data['amount']+damt
      writefile = open('atmInfo/'+str(acctno)+'.pkl','wb+')
      p.dump(data,writefile)
      print("your deposit amount is:",damt)
      print('your current balance:',data['amount'])
    else:
      print("deposit amount should be multiple of 100!!")
    #store the transaction history of respective account
    history = 'Deposit Amount:'+str(damt)+' Time:'+str(t.datetime.now())+'\n'
    writehistory = open('atmInfo/'+str(acctno)+'_review''.txt','a+')
    writehistory.write(history)
  except:
    print("Invalid acount number or pin")
  
def withdraw():
  try:
    acctno = int(input('please enter your acount number=>'))
    readfile = open('atmInfo/'+str(acctno)+'.pkl','rb+')
    data = p.load(readfile)
    def pinRequest():
      upin = int(input('enter your pin=>'))
      if(upin!=data['pin']):
       print("Invalid pin please enter valid pin!!")
       pinRequest()
    pinRequest()
    
    wamt = int(input('enter amount to withdraw=>'))
    if(wamt%100==0 and wamt<=data['amount'] and wamt>=100):
      data['amount'] = data['amount']-wamt
      writefile = open('atmInfo/'+str(acctno)+'.pkl','wb+')
      p.dump(data,writefile)
      writefile.close()
      readfile.close()
      print("Your withdrawal amount:",wamt)
      print("your Remaining Balance:",data['amount'])
    else:
      print("Insufficent fund or Invalid amount!!")
      #store the transaction history of respective account
    history = 'withdraw Amount:'+str(wamt)+' Time:'+str(t.datetime.now())+'\n'
    writehistory = open('atmInfo/'+str(acctno)+'_review''.txt','a+')
    writehistory.write(history)
  except:
    print("invalid account number or pin!!")
  
def checkBalance():
    try:
      acctno = int(input('please enter your acount number=>'))
      readfile = open('atmInfo/'+str(acctno)+'.pkl','rb+')
      data = p.load(readfile)
      def pinRequest():
        upin = int(input('enter your pin=>'))
        if(upin!=data['pin']):
          print("Invalid pin please enter valid pin!!")
          pinRequest()
      pinRequest()
      print("Your Current Balance is=>",data['amount'])
      readfile.close()
    except:
      print("Invalid acount number or pin!!")
   
def transactionHistory():
  #try:
    acctno = int(input("enter your acount Number=>"))
    readfile1 = open('atmInfo/'+str(acctno)+'.pkl','rb+')
    data1=p.load(readfile1)

    readfile2 = open('atmInfo/'+str(acctno)+'_review'+'.txt','r+')
    data2 = readfile2.readlines()

    def pinRequest():
      upin = int(input('enter your pin=>'))
      if(upin!=data1['pin']):
        print("Invalid pin please enter valid pin!!")
        pinRequest()
    pinRequest()
    print("your last 5 transaction history is:")
    for i in range(-1,-len(data2),-1):
      print('transaction',-1*i,'=>',data2[i])
      if(i==-5):
        break
  #except:
    #print("no transaction history!!")
def acountDetail():
  try:
    acctno = int(input('enter your acount number=>'))
    #read file to display account detail
    readfile = open('atmInfo/'+str(acctno)+'.pkl','rb+')
    data = p.load(readfile)
    def pinRequest():
      upin = int(input('enter your pin=>'))
      if(upin!=data['pin']):
        print("invalid pin please enter valid pin!!")
        pinRequest()
    pinRequest()
    print('your name is:',data['name'])
    print('your acctno is:',data['acctno'])
      #print('your pin is:',data['pin'])
    print('your balance :',data['amount'])
    readfile.close()
  except:
    print("Invalid Pin!!!")


def pinChange():
  choice = input("are you sure you want to change your pin? yes|no=>")
  try:
    if(choice=='yes'):
      acctno = int(input("enter your acount number=>"))
      readfile = open('atmInfo/'+str(acctno)+'.pkl','rb+')
      data = p.load(readfile)
      def pinRequest():
        prevPin = int(input("enter your old pin:"))
        if(prevPin!=data['pin']):
          print("Invalid pin please enter valid pin!!")
          pinRequest()
      pinRequest()
      newPin = int(input("enter 3 digit new pin=>"))
      data['pin'] = newPin
      writefile = open('atmInfo/'+str(acctno)+'.pkl','wb+')
      p.dump(data,writefile)
      print("your pin is changed successfully")
      
    elif(choice=='no'):
      ATM()
  except:
    print("no data belogs to this acount")

def transfer():
  try:
    senderAcctno = int(input("enter your acount number=>"))
    #open sender file and load
    senderfile = open('atmInfo/'+str(senderAcctno)+'.pkl','rb+')
    senderdata = p.load(senderfile)
    def pinRequest():
      senderpin = int(input("enter your pin=>"))
      if(senderpin != senderdata['pin']):
        print("Invalid pin please try again")
        pinRequest()
    pinRequest()
    reciverAcctno = int(input("enter acount to transfer to=>"))
    #open reciver file and load
    with open('atmInfo/'+str(reciverAcctno)+'.pkl','rb+') as reciverfile:
      reciverdata = p.load(reciverfile)
    # enter transfer amount
    transferAmount = int(input("enter amount to transfer=>"))
    if(transferAmount<=senderdata['amount'] and transferAmount%100==0 and transferAmount>=100):
      senderdata['amount'] = senderdata['amount']-transferAmount
      senderfile.close()
        #write back sender file
      senderfile = open('atmInfo/'+str(senderAcctno)+'.pkl','wb+')
      p.dump(senderdata,senderfile)
      senderfile.close()

      #add amount transfered to reciver file
      reciverdata['amount'] = reciverdata['amount']+transferAmount
      reciverfile.close()
      #write back reciver file
      with open('atmInfo/'+str(reciverAcctno)+'.pkl','wb+') as reciverfile:
        p.dump(reciverdata,reciverfile)

      #print confirmation
      print("transaction successful!!")
      print("you transfered",transferAmount,"to acount number",reciverAcctno)
      print("your remaining Balance:",senderdata['amount'])
    else:
      print("Invalid amount or Insufficent Fund!!")
        #store the transaction history of respective account
    history1 = 'transferAmount:'+str(transferAmount)+' transferedTo:'+str(reciverAcctno)+' time'+str(t.datetime.now())+'\n'
    history2 = 'transferAmount:'+str(transferAmount)+' transferedFrom:'+str(senderAcctno)+' time'+str(t.datetime.now())+'\n'

    writehistory1 = open('atmInfo/'+str(senderAcctno)+'_review''.txt','a+')
    writehistory2 = open('atmInfo/'+str(reciverAcctno)+'_review''.txt','a+')
    writehistory1.write(history1)
    writehistory2.write(history2)
  except:
    print("operation failed due to Invalid input!!!")

def Quit():
  choice = input("Are you sure You want to Quit? yes|no=>")
  if(choice=='yes'):
    exit()
  elif(choice=='no'):
    ATM()
  else:
    print("Invalid choice!!")

#access atm
def ATM():
  print("====Enter Operation to perform====")
  print("  Enter 1 for Registration=>")
  print("  Enter 2 for Deposit=>")
  print("  Enter 3 for Withdrawal=>")
  print("  Enter 4 for Balance Check=>")
  print("  Enter 5 for to check last five transaction=>")
  print("  Enter 6 for Acount Datail=>:")
  print("  Enter 7 for Pin Change=>:")
  print("  Enter 8 for Transfer=>:")
  print("  Enter 9 to Exit the window=>:")

  op = int(input("Enter your operation=>"))

  if(op==1):
    register()
  elif(op==2):
    deposit()
  elif(op==3):
    withdraw()
  elif(op==4):
    checkBalance()
  elif(op==5):
    transactionHistory()
  elif(op==6):
    acountDetail()
  elif(op==7):
    pinChange()
  elif(op==8):
    transfer()
  elif(op==9):
    Quit()
  else:
    print("invalid operation please choose no from 1 to 9.")


ATM()

  
