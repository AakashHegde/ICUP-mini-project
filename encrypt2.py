import io


#This function generates a number randomly and increments the ASCII value of every character of the input by that number
def encrypt1(filename):
   l=[]
   fileobj=open(filename,"r+")   #Opens the file for reading
   s=fileobj.read() #Stores the contents of the file to s
   import random
   k=random.randrange(50) #Generates a random number
   for i in s:
      l.append(chr(ord(i)+k)) #Increments the ASCII value of every character of the input by the random number and appends to list l
   str_encrypt = ''.join(l) #Converts the list l to a string
   fileobj.close() #Closes the file
   fileobj=open("filename1","w+") #Opens another file to store the encrypted text
   fileobj.write(str_encrypt)
   fileobj.close()
   return (str_encrypt,1,k)

#This function takes encrypted text returned by encrpyt1 function along with the key(random number) and decrements the ASCII value by the key
def decrypt1(filename,key):
   fileobj=open(filename,"r+")   
   s=fileobj.read() 
   l1=[]
   for i in s:
      l1.append(chr(ord(i)-key)) #Decrements the ASCII value of every character of the encrypted text by the key
   str_decrypt = ''.join(l1) 
   fileobj.close()
   return str_decrypt   

def encrypt2(filename):
   l=[]
   fileobj=open(filename,"r+") 
   s=fileobj.read() 
   for i in s:
      l.append(chr(ord(i)+5)) #Increments the ASCII value of every character of the input by 5 and appends to list l
      for j in range(3):
         import random
         k=random.randrange(120)
         l.append(chr(k)) #Generates 3 random ASCII values and appends their corresponding characters to the list l
   str_encrypt = ''.join(l) 
   fileobj.close()
   fileobj=open("filename1","w+")
   fileobj.write(str_encrypt)
   fileobj.close()
   return (str_encrypt,2)

def decrypt2(filename):
   l1=[]
   fileobj=open(filename,"r+")
   s=fileobj.read() 
   for i in range(len(s)):
      if(i%4==0): #Considering only the positions that are divisible by 4(where the required text is present)
         l1.append(chr(ord(s[i])-5)) #Decrements the ASCII value of every character of the encrypted text by 5
   str_decrypt = ''.join(l1) 
   fileobj.close()
   return str_decrypt

def encrypt3(filename):
   l=[]
   fileobj=open(filename,"r+")
   s=fileobj.read()
   for i in range(len(s)):
      if(i%2==0):
         l.append(chr(ord(s[i])+3)) #Increments the ASCII value by 3 for every even character and appends to list l
      else:
         l.append(chr(ord(s[i])-3)) #Decrements the ASCII value by 3 for every odd character and appends to list l
   str_encrypt = ''.join(l)
   fileobj.close()
   fileobj=open("filename1","w+")
   fileobj.write(str_encrypt)
   fileobj.close()
   return (str_encrypt,3)

def decrypt3(filename):
   l1=[]
   fileobj=open(filename,"r+")
   s=fileobj.read()
   for i in range(len(s)):
      if(i%2==0):
         l1.append(chr(ord(s[i])-3)) #Decrements the ASCII value by 3 for every odd character and appends to list l1	 
      else:
         l1.append(chr(ord(s[i])+3)) #Increments the ASCII value by 3 for every even character and appends to list l1
   str_decrypt = ''.join(l1)
   fileobj.close()
   return str_decrypt
   

#------------------ADDITIONS--------------------

#Generates a single random number, multiplies whole text with it and reverses it
#key is one single number generated


def encrypt4(filename):
   l=[]
   with io.open(filename, "r", encoding="utf-8") as my_file:
      s=my_file.read()
   import random
   k=random.randrange(5,20)
   for i in range(len(s)):
      l.append(chr(ord(s[i])*k))
   str_encrypt = ''.join(l)
   my_file.close()
   str_encrypt=str_encrypt[::-1]
   with io.open("encrypted.txt", "w", encoding="utf-8") as my_file:
      my_file.write(str_encrypt)
   return (str_encrypt,4,k)

def decrypt4(filename,k):
   l1=[]
   with io.open(filename, "r", encoding="utf-8") as my_file:
      s=my_file.read()
   s=s[::-1]
   for i in range(len(s)):
      l1.append(chr(ord(s[i])//k))
   str_decrypt = ''.join(l1)
   my_file.close()
   return str_decrypt

#-----------------------------------------------

#generates a random number each letter of the text, and multiplies
#key is the sequnce of random numbers that was generated

def encrypt5(filename):
   l=[]
   key=[]
   with io.open(filename, "r", encoding="utf-8") as my_file:
      s=my_file.read()
   import random
   for i in range(len(s)):
      k=random.randrange(5,20)
      key.append(k)
      l.append(chr(ord(s[i])*k))
   str_encrypt = ''.join(l)
   my_file.close()
   with io.open("encrypted.txt", "w", encoding="utf-8") as my_file:
      my_file.write(str_encrypt)
   return (str_encrypt,4,key)

def decrypt5(filename,key):
   l1=[]
   with io.open(filename, "r", encoding="utf-8") as my_file:
      s=my_file.read()
   for i in range(len(s)):
      k=key[i]
      l1.append(chr(ord(s[i])//k))
   str_decrypt = ''.join(l1)
   my_file.close()
   return str_decrypt

#-----------------------------------------------

#generates a random number for each letter, squares it and adds to it
#key is the sequnce of random numbers that was generated

def encrypt6(filename):
   l=[]
   key=[]
   with io.open(filename, "r", encoding="utf-8") as my_file:
      s=my_file.read()
   import random
   for i in range(len(s)):
      k=random.randrange(5,50)
      k=k**2
      key.append(k)
      l.append(chr(ord(s[i])+k))
   str_encrypt = ''.join(l)
   my_file.close()
   with io.open("encrypted.txt", "w", encoding="utf-8") as my_file:
      my_file.write(str_encrypt)
   return (str_encrypt,4,key)

def decrypt6(filename,key):
   l1=[]
   with io.open(filename, "r", encoding="utf-8") as my_file:
      s=my_file.read()
   for i in range(len(s)):
      k=key[i]
      l1.append(chr(ord(s[i])-k))
   str_decrypt = ''.join(l1)
   my_file.close()
   return str_decrypt

if __name__ == "__main__":
   ''' 
   x=input("Enter file name : ")
   encr=encrypt4(x)
   print(encr[0]) 
   dec=decrypt4("encrypted.txt",encr[2])
   print(dec)
   t=encrypt3('text.txt')
   print(t[0])
   print(decrypt3('file.txt'))
   '''
