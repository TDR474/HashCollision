for x in range(2**k):
        for y in range(2**k):
            if hashlib.sha256(str(x).encode()).hexdigest()[-k:] == hashlib.sha256(str(y).encode()).hexdigest()[-k:]:
                return(str(x).encode(),str(y).encode())
    
