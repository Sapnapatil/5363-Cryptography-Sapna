import argparse
import sys
import randomized_vigenere as rv

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
    parser.add_argument("-i", "--inputfile", dest="inputFile", help="Input Name")
    parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
    parser.add_argument("-s", "--seed", dest="seed",help="Integer seed")

    args = parser.parse_args()

    #f = open(args.inputFile,'r')
    f = open(Inputfile.txt,'r')
    message = f.read()
    if(args.type == 'add'):
        data = rv.encrypt(message,args.mode,args.seed)
    else:
        data = rv.decrypt(message,args.mode,args.seed)
    o = open(args.outputFile,'w')
    o.write(str(data))


if __name__ == '__main__':
    main()
