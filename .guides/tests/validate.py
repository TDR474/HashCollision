#!/usr/bin/env python3
import random
import hashlib

def validate():
    try:
        import hash_collision
    except ImportError:
        raise ImportError("Could not import homework file 'hash_collision.py'")

    required_methods = ["hash_collision"]
    for m in required_methods:
        if m not in dir(hash_collision):
            print( "%s not defined"%m )
            return 0

    num_tests = 5
    num_passed = 0
    for i in range(num_tests):
            print("=========== Running test %d ==========="%(i+1))
            numbits = random.SystemRandom().randint(10,20)
            try:
                x,y = hash_collision.hash_collision(numbits)
            except Exception as e:
                print( "hash_collision failed" )
                continue
            print( "hash_collision ran successfully" )
            
            if not isinstance(x,bytes) or not isinstance(y,bytes):
                print( "hash_collision should return bytes" )
                continue
            print( "hash_collision returned byte strings (as it should)" )
            
            h_hex = hashlib.sha256( x ).hexdigest()
            xh_bin = bin( int( h_hex, base=16 ) )[2:]
            h_hex = hashlib.sha256( y ).hexdigest()
            yh_bin = bin( int( h_hex, base=16 ) )[2:]
            if xh_bin [-numbits:] == yh_bin[-numbits:] and x != y:
                num_passed = num_passed + 2
                print( "SUCCESS: You created a collision" )
            else:
                print( "ERROR: You failed to create a collision" )

    return num_passed


