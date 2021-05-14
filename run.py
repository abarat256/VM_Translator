import sys
import os.path
import Translator

inputfile= sys.argv[1]
inputfile = inputfile.strip()
if os.path.isfile(inputfile)== False:
    print("File Not Found, Check Path");
    sys.exit()
size=len(inputfile)
if inputfile[size-2:size] != "vm":
    print("Wrong Format")
else:
    outputfile = inputfile.replace("vm","asm")
    Translator.translate(inputfile, outputfile)
    
