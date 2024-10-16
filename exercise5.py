#Exercise 5
"""password=input('Enter a password')
passworList=list(password)
if len(passwordList)<8 :
    print('This password is not strong')
elif
 i=0
 while i<n:"""

#Okay so in this exercise i was willing to use for loop to see the character is upper case by the function
#character.isupper but which will make the code a bit weeker due to the large numbers of loops that is why 
#i will use the flag, to be honest i took a small idea about the flag and the search of the 
#letter by the boolean and using the ascii code of each character and here is my code :

def IsstrongPassword ():
    password =input('Enter a password')
    
    uper_case= False
    lower_case= False
    digit= False
    special_character=False
    for char in password: 
     if 'A'<= char <= 'Z':
        uper_case=True
     elif 'a'<=char <='z':
        lower_case=True
     elif '0'<= char<='9':
        digit=True
     elif (char=='!' or char=='$' or char=='#' or char=='?'):
        special_character=True
    if (len(password)>=8 and uper_case and lower_case and digit and  special_character ):
       print("your password is strong")
    else :
       print("your password is not strong")
     
password_suggested=IsstrongPassword()
print(password_suggested)

        


