import hashlib
import os

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    #Collision finding code goes here
    # x and y are two randomly generated variables as strings
    # SHA256(x) and SHA256(y) should match on their final k bits 
    # k is the number of bits to be matched
    # The return variables, x and y, should be encoded as bytes in the end.
    # if the hash of x and y match, return x and y

    for x in range(2**k):
        for y in range(2**k):
            if hashlib.sha256(str(x).encode()).hexdigest()[-k:] == hashlib.sha256(str(y).encode()).hexdigest()[-k:]:
                return(str(x).encode(),str(y).encode())
    

    
