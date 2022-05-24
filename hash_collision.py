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
    # x and y are two randomly generated variables
    # SHA256(x) and SHA256(y) should match on their final k bits 
    # k is the number of bits to be matched
    # The return variables, x and y, should be encoded as bytes.
    # iterate over 2^k possibilities of x and y

    # randomly generate a three-letter string (NOT bytes) x
    # randomly generate a three-letter string (NOT bytes) y
    # hash x and y using SHA256
    # check if the final k bits of the hash of x and y match
    # loop until the final k bits match
    # return x and y
    x = os.urandom(3)
    y = os.urandom(3)
    x_hash = hashlib.sha256(x).digest()
    y_hash = hashlib.sha256(y).digest()
    x_hash_final = x_hash[-k:]
    y_hash_final = y_hash[-k:]
    while x_hash_final != y_hash_final:
        x = os.urandom(3)
        y = os.urandom(3)
        x_hash = hashlib.sha256(x).digest()
        y_hash = hashlib.sha256(y).digest()
        x_hash_final = x_hash[-k:]
        y_hash_final = y_hash[-k:]
    return(x,y)


