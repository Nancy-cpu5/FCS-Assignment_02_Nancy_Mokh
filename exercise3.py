#Exercise 3
def reverseString():
    word=input('Enter a word')
    inverse=list(word)
    i=0
    j=len(inverse)-1
    while i<j:
               m=inverse[i] ; n=inverse[j]
               inverse[j]=m ; inverse[i]=n #here we can also use tuple unpacking swapping but i am trying this
               i+=1
               j-=1
    return ''.join(inverse)
 
   

reverse_word=reverseString()
print(reverse_word)