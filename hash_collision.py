# Write a brute-force algorithm to find a partial collision 

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
    # SHA256(x) and SHA256(y) shoul match on their final k bits 
    # x and y are the two strings to be hashed
    # k is the number of bits to be matched
    # The return variables, x and y, should be encoded as bytes.
    # iterate over 2^k possibilities of x and y
    for x in range(2**k):
        x_hash = hashlib.sha256(str(x).encode('utf-8')).hexdigest()
        for y in range(2**k):
            y_hash = hashlib.sha256(str(y).encode('utf-8')).hexdigest()
            if x_hash[-k:] == y_hash[-k:]:
                return(str(x).encode('utf-8'),str(y).encode('utf-8'))
