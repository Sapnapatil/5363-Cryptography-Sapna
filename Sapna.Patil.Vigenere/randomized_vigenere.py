#----------------------------------------------------------------------------------------------------------
###############################################
# Name: Sapna Patil
# Class: CMPS 5363 Cryptography
# Date: 28 July 2015
# Program 2 - Randomized Vigenère Cipher
###############################################
import random
#----------------------------------------------------------------------------------------------------------
#Symbol string shows all 95 characters
symbols= """ !"#$%&'()*+,-./0123456789:;?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
vigenere = [[0 for i in range(len(symbols))] for i in range(len(symbols))]
#----------------------------------------------------------------------------------------------------------       
#----------------------------------------------------------------------------------------------------------
#Togetfunction is used to get random seed
def togetseed(seed):
	return random.seed(seed)
#----------------------------------------------------------------------------------------------------------    
    
	
#----------------------------------------------------------------------------------------------------------	
#setmessage is used to setmessage
def setMessage(message):
	return message
#----------------------------------------------------------------------------------------------------------
#Below function is used to Generate keyword from seed		
def keywordFromSeed(seed):
	Letters = []
	#seed=int(seed)
	while seed > 0:
		Letters.insert(0,chr((seed % 100) % 26 + 65))
		seed = seed // 100
		keyWord = "".join(Letters)
	return keyWord
#----------------------------------------------------------------------------------------------------------
#This function is used to generate vigenere matrix using 95*95 combination of Symbols
def buildVigenere(symbols,seed):
    #generate the seed using random function 
    random.seed(seed)
    #to get length of symbol 
    n = len(symbols)
    vigenere = [[0 for i in range(n)] for i in range(n)]
    symbols = list(symbols)
    random.shuffle(symbols)
    symbols = ''.join(symbols)
    print('new symbols:')
    print(symbols)
    print(' ')
    
    for sym in symbols:
        random.seed(seed)
        myList = []
    
        for i in range(n):
            r = random.randrange(n)
            
            if r not in myList:
                myList.append(r)
            else:
                while(r in myList):
                    r = random.randrange(n)
            
                myList.append(r)
                               
            while(vigenere[i][r] != 0):
                r = (r + 1) % n
            
            vigenere[i][r] = sym
            
    return vigenere
#----------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------- 
#To encrypt plainmessage i need to have seed and message by using seed i can generate the keyword and using
# keyword and the message i am getting through that it easy to encrypt message
#  
def encrypt(seed, message,mode):
         message=setMessage(message)
         ciphertext = ""
         vigenere=buildVigenere(symbols,seed)
         #print('seed value in rv',seed)
         keyWord=keywordFromSeed(seed)
         if(mode== 'encrypt'):
            for i in range(len(message)):
                mi = i
                ki = i % len(keyWord)
                l=len(symbols)
                row=col=0
                for r in range(l):
                    if(message[mi]==vigenere[0][r]):
                        col=r
                for c in range(len(symbols)):
                    if(keyWord[ki]==vigenere[c][0]):
                        row=c 
                vigvariable=vigenere[row][col]
                ciphertext = ciphertext + vigvariable
                #print(ciphertext)
         return ciphertext
#----------------------------------------------------------------------------------------------------------               
#----------------------------------------------------------------------------------------------------------
#To decrypt ciphertext i need to have seed and ciphertext by using seed i can generate the keyword and using
# keyword and the ciphertext i am getting throgh that it easy to decrypt ciphertext to get plaintext
# 
def decrypt(seed, message,mode):
        plaintext = ""
        message=setMessage(message)
        vigenere=buildVigenere(symbols,seed)
        #print('seed value in rv',seed)
        keyWord=keywordFromSeed(seed)
        for i in range(len(message)):
                mi = i
                ki = i % len(keyWord)
                n = len(symbols)
                r=c=0
                for c in range(len(symbols)):
                    if(keyWord[ki]==vigenere[c][0]):
                       row=c
                for r in range(n):
                    if(message[mi]==vigenere[row][r]):
                       col=r
                decryptChar=vigenere[0][col]   
                plaintext=plaintext+decryptChar;
        #print("The plain text is :",plaintext)
        return plaintext
#----------------------------------------------------------------------------------------------------------    