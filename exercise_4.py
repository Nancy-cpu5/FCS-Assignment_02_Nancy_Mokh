#Exercise 4
def Eliminateodd ():
 numbers=input('Enter the integers')
 list=numbers.split() 
 listOfnumbers=[int(num) for num in list]
 #here if we want to take the numbers separately we can make a while loop and tell the user to enter -1 when he wants to stop giving numbers
 i=0
 evenlist=[] 
 # we just introduced a new list to add the numbers in instead of eliminating the odd numbers from the old list and make a while loop

 for num in  listOfnumbers:
  if num  %2 == 0 :# which says that this number is even
    evenlist.append(num)
 return evenlist
no_odd=Eliminateodd()
print(no_odd)