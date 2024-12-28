
#encode() converts string to bytes for md5 function and then hexdigest() to hexadecimal

import hashlib

choice = input("Please type \n 1 for md5 \n 2 for sha1 \n 3 for sha256 \n 4 for sha512: ")
sometext = input("Please type your text to generate it's hash: ")

converted_txt = sometext.encode()

if(choice == "1"):
    print( hashlib.md5(converted_txt).hexdigest() )
elif(choice == "2"):
    print( hashlib.sha1(converted_txt).hexdigest() )
elif(choice == "3"):
    print( hashlib.sha256(converted_txt).hexdigest() )
elif(choice == "4"):
    print( hashlib.sha512(converted_txt).hexdigest() )
else:
    print("Error!")


