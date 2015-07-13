###############################################
# Name: (Sapna Patil)
# Class: CMPS 5363 Cryptography
# Date: 13 July 2015
# Program 1 - Playfair Cipher
###############################################
 #------------------------------------------------------------------------------
 #---------------Directories----------------------------------------------------
import pprint
import re
import sys

 #--------------Class Defination------------------------------------------------
class StringManip:
    """
    Helper class to speed up simple string manipulation
    """
#--------------Defination to generate Alphabet----------------------------------
    def generateAlphabet(self):
        #Create empty alphabet string
        alphabet = ""

        #Generate the alphabet
        for i in range(0,26):
            alphabet = alphabet + chr(i+65)

        return alphabet
#-------------------------------------------------------------------------------        
#-------------Defination to clean the string------------------------------------

    def cleanString(self,s,options = {'up':1,'reNonAlphaNum':1,'reSpaces':'','spLetters':'X'}):
        """
        Cleans message by doing the following:
        - up            - uppercase letters
        - spLetters     - split double letters with some char
        - reSpaces      - replace spaces with some char or '' for removing spaces
        - reNonAlphaNum - remove non alpha numeric
        - reDupes       - remove duplicate letters
        @param   string -- the message
        @returns string -- cleaned message
        """
        if 'up' in options:
            s = s.upper()

        if 'spLetters' in options:
            #replace 2 occurences of same letter with letter and 'X'
            s = re.sub(r'([ABCDEFGHIJKLMNOPQRSTUVWXYZ])\1', r'\1X\1', s)

        if 'reSpaces' in options:
            space = options['reSpaces']
            s = re.sub(r'[\s]', space, s)

        if 'reNonAlphaNum' in options:
            s = re.sub(r'[^\w]', '', s)

        if 'reDupes' in options:
            s= ''.join(sorted(set(s), key=s.index))

        return s

 #-------------------------------------------------------------------------------
 #---------------Class defination PlayFair---------------------------------------
class PlayFair:
    """
    Class to encrypt via the PlayFair cipher method
    Methods:
    - generateSquare
    - transposeSquare
    -
    """
 
 #---------------defination for init function---------------------------------------
    def __init__(self,key,message):
        self.Key = key
        self.Message = message
        self.Square = []
        self.Transposed = []
        self.StrMan = StringManip()
        self.Alphabet = ""

        self.generateSquare()
        self.transposeSquare()

        self.Message = self.StrMan.cleanString(self.Message,{'up':1,'reSpaces':'','reNonAlphaNum':1,'spLetters':1})
        mess=self.Message
        lengg=len(mess)
        if(lengg%2==1):
            #print("the message is with x")
            mess=mess+'X'
        self.Message=mess
 #-------------------------------------------------------------------------------
 
 #---------------defination for generateSquare function----------------------------
        
    def generateSquare(self):
        """
        Generates a play fair square with a given keyword.
        @param   string   -- the keyword
        @returns nxn list -- 5x5 matrix
        """
        row = 0     #row index for sqaure
        col = 0     #col index for square

        #Create empty 5x5 matrix
        self.Square = [[0 for i in range(5)] for i in range(5)]

        self.Alphabet = self.StrMan.generateAlphabet()

        #uppercase key (it meay be read from stdin, so we need to be sure)
        self.Key = self.StrMan.cleanString(self.Key,{'up':1,'reSpaces':'','reNonAlphaNum':1,'reDupes':1})

        #Load keyword into square
        for i in range(len(self.Key)):
            self.Square[row][col] = self.Key[i]
            self.Alphabet = self.Alphabet.replace(self.Key[i], "")
            col = col + 1
            if col >= 5:
                col = 0
                row = row + 1

        #Remove "J" from alphabet
        self.Alphabet = self.Alphabet.replace("J", "")

        #Load up remainder of playFair matrix with
        #remaining letters
        for i in range(len(self.Alphabet)):
            self.Square[row][col] = self.Alphabet[i]
            col = col + 1
            if col >= 5:
                col = 0
                row = row + 1

 #-------------------------------------------------------------------------------
  #-------------------defination for transposeSquare function--------------------
    def transposeSquare(self):
        """
        Turns columns into rows of a cipher square
        @param   list2D -- playFair square
        @returns list2D -- square thats transposed
        """
        #Create empty 5x5 matrix
        self.Transposed = [[0 for i in range(5)] for i in range(5)]

        for col in range(5):
            for row in range(5):
               self.Transposed[col][row] = self.Square[row][col]

 #-------------------------------------------------------------------------------
  #-------------------defination for getCodedDigraph function--------------------
    def getCodedDigraph(self,digraph):
        """
        Turns a given digraph into its encoded digraph whether its on
        the same row, col, or a square
        @param   list -- digraph
        @returns list -- encoded digraph
        """
        newDigraph = ['','']

        #Check to see if digraph is in same row
        for row in self.Square:
            if digraph[0] in row and digraph[1] in row:
                newDigraph[0] = row[((row.index(digraph[0])+1)%5)]
                newDigraph[1] = row[((row.index(digraph[1])+1)%5)]
                return newDigraph

        #Check to see if digraph is in same column
        for row in self.Transposed:
            if digraph[0] in row and digraph[1] in row:
                newDigraph[0] = row[((row.index(digraph[0])+1)%5)]
                newDigraph[1] = row[((row.index(digraph[1])+1)%5)]
                return newDigraph


        #Digraph is in neither row nor column, so it's a square
        location1 = self.getLocation(digraph[0])
        location2 = self.getLocation(digraph[1])

        return self.Square[location1[0]][location2[1]] + self.Square[location2[0]][location1[1]] 
       
 #------------------------------------------------------------------------------- 
 #-------------------defination for getDecodedDigraph function-------------------- 
    def getDecodedDigraph(self,digraph):
        """
        Turns a given digraph into its encoded digraph whether its on
        the same row, col, or a square
        @param   list -- digraph
        @returns list -- encoded digraph
        """
        newDigraph = ['','']

        #Check to see if digraph is in same row
        for row in self.Square:
            if digraph[0] in row and digraph[1] in row:
                newDigraph[0] = row[((row.index(digraph[0])-1)%5)]
                newDigraph[1] = row[((row.index(digraph[1])-1)%5)]
                return newDigraph

        #Check to see if digraph is in same column
        for row in self.Transposed:
            if digraph[0] in row and digraph[1] in row:
                newDigraph[0] = row[((row.index(digraph[0])-1)%5)]
                newDigraph[1] = row[((row.index(digraph[1])-1)%5)]
                return newDigraph


        #Digraph is in neither row nor column, so it's a square
        location1 = self.getLocation(digraph[0])
        location2 = self.getLocation(digraph[1])

        return self.Square[location1[0]][location2[1]] + self.Square[location2[0]][location1[1]] 
       
 #-------------------------------------------------------------------------------
 #-------------------defination for getLocation function-------------------- ---
    def getLocation(self,letter):
        row = 0
        col = 0

        count = 0
        for list in self.Square:
            if letter in list:
                row = count
            count += 1

        count = 0
        for list in self.Transposed:
            if letter in list:
                col = count
            count += 1
        return [row,col]
#-------------------------------------------------------------------------------
    #############################################
    # Helper methods just to see whats going on
    #############################################

#-------------------------------------------------------------------------------    
    def printNewKey(self):
        #print(self.Key)
        return(key)

    def printNewMessage(self):
        #print(self.Message)
        return self.Message

    def printSquare(self):
        for list in self.Square:
            #print(list)
            c=0
        print('')

    def printTransposedSquare(self):
        for list in self.Transposed:
            #print(list)
            c=0
        print('')
#-------------------------------------------------------------------------------
#------------Variable declaration and Main Menu function------------------------
lencount=0 
Var = ""
Var1=''
messagestring= ""
#-------------------------------------------------------------------------------
print ('playfair Encryption Tool (P.E.T)' )
print ('Written By: (Sapna Patil) ')
print ('********************************************************')
print ('1. Encipher')
print ('2. Decipher')
print ("3. Quit")
print ('=>')
ch = input()
print ('********************************************************')
flag = 1
while(flag == 1):
    if(ch == '1'):
        #-------------------------------------------------------------------------------
        print ('Enter the Message for Encryption')
        message = input()
        print (' ')
        print ('Enter the Keyword for Encryption')
        key = input()
        print (' ')
        #-------------------------------------------------------------------------------
        myCipher = PlayFair(key,message)
        myCipher.printNewKey()
        newMessage = myCipher.printNewMessage()
        myCipher.printSquare()
        myCipher.printTransposedSquare()
        while(lencount<len(newMessage)):
            Diagraph = myCipher.getCodedDigraph([newMessage[lencount],newMessage[lencount+1]])
            Var = Var + messagestring.join(Diagraph)
            lencount=lencount+2
        #-------------------------------------------------------------------------------
        print ('The Encrypted Message :')
        print(Var)
        flag = 1
    #-------------------------------------------------------------------------------
    elif(ch=='2'):
        #-------------------------------------------------------------------------------
        print ('Enter the Encrypted Message ')
        message = input()
        print (' ')
        print ('Enter the Keyword for Decryption')
        key = input()
        print (' ')
        #-------------------------------------------------------------------------------
        myCipher = PlayFair(key,message)
        myCipher.printNewKey()
        newMessage = myCipher.printNewMessage()
        myCipher.printSquare()
        myCipher.printTransposedSquare()
        lencount=0 
        while(lencount<len(newMessage)):
            Diagraph = myCipher.getDecodedDigraph([newMessage[lencount],newMessage[lencount+1]])
            Var1 = Var1 + messagestring.join(Diagraph)
            lencount=lencount+2
        #-------------------------------------------------------------------------------    
        print ('The Decrypted Message is :')
        print(Var1)
        flag = 1
    else:
        sys.exit()
    print ('********************************************************')
    print ('playfair Encryption Tool (P.E.T)' )
    print ('Written By: (Sapna Patil) ')
    print ('********************************************************')
    print ('1. Encipher')
    print ('2. Decipher')
    print ("3. Quit")
    print ('=>')
    ch = input()

         #-------------------------------------------------------------------------------