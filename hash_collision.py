# Write a brute-force algorithm to find a partial collision 

import hashlib
import os
import random

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
    
    # randomly generate a integer x 
    x = random.randint(0,2**k)
    y = random.randint(0,2**k)

    # while SHA256(x) and SHA256(y) do not match on their final k bits, increment x and y
    while hashlib.sha256(str(x).encode()).hexdigest()[-k:] != hashlib.sha256(str(y).encode()).hexdigest()[-k:]:
        x = x+1
        y = y+1
  
    # break the while loop when SHA256(x) and SHA256(y) match on their final k bits
    # return x and y
    return(str(x).encode(),str(y).encode())
    
