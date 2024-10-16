#exercise 6
def checkIPv4 ():
 code=input('Enter a code')
 list=code.split('.')
  for num in list:
     if( '0'<=num<='255' and len(list)=4):
       print('This code is IPv4')
checkCode=checkIPv4()
print(checkCode)