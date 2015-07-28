###############################################
# Name: Sapna Patil
# Class: CMPS 5363 Cryptography
# Date: 28 July 2015
# Program 2 - Randomized Vigenère Cipher
###############################################
#---------------------Directories-------------------------------------------------------------------
#It imports directories those are required in function
import argparse
import randomized_vigenere as rv
#-------------Main Function-------------------------------------------------------------------------
#starting point of program is an main function
def main():
    #The argparse module makes it easy to write user-friendly command-line interfaces
    parser = argparse.ArgumentParser()
    #Filling an ArgumentParser with information about program arguments is done by making calls to the add_argument() method.
    parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
    parser.add_argument("-i", "--inputfile", dest="inputFile", help="Input Name")
    parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
    parser.add_argument("-s", "--seed", dest="seed", help="Integer seed")
    #calling parse_args() will return an object
    args = parser.parse_args()
    
    #to check whether mode is encrypt
    if(args.mode == 'encrypt'):
        #to get seed from args parameter
        seed = args.seed
        seed=int(seed)
        print("the seed value is ",seed)
        #following fuction is used to open file and read message
        f = open(args.inputFile,'r')
        message = f.read()
        #call function from other file to pass the parameter using object of that file
        Vigmat=rv.encrypt(seed,message,'encrypt')
        #below function is used to write output to file
        print("Encrypted Message is:",Vigmat)
        o = open(args.outputFile,'w')
        o.write(str(Vigmat))
        
        #below else part wil be decrypt function
    else:
        seed = args.seed
        seed=int(seed)
        f = open(args.inputFile,'r')
        message = f.read()
        Vigmat=rv.decrypt(seed,message,'decrypt')
        #below function is used to write output to file
        print("Decrypted Message is:",Vigmat)
        o = open(args.outputFile,'w')
        o.write(str(Vigmat))
#----------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
#----------------------------------------------------------------------------------------------------------------

        
        
        
        
    
    