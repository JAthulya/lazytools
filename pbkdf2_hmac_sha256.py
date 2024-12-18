from hashlib import pbkdf2_hmac
import sys
import string

hash_to_crack = sys.argv[1]
salt_p = sys.argv[2]
iter_p = sys.argv[3]
key_len = sys.argv[4]
wordlist_loc = sys.argv[5]

iterations = int(iter_p)
salt = bytes.fromhex(str(salt_p))
key_len = int(key_len)

if len(sys.argv) != 6:
    print(f"Add arguments as follows\n\rscript.py hash_val_to_crack salt iteration_count key_length word_list")
    quit()

def converting_hash(word, iterations, salt, key_len):
    hash = pbkdf2_hmac('sha256',bytes(word,'utf-8'), salt, iterations, dklen=key_len)
    return(hash.hex())

with open(wordlist_loc, 'r') as file:
    for line in file:
        line = line.rstrip()
        chash = converting_hash(line, iterations, salt, key_len)
        #print(f"{line}:{chash}")
        if hash_to_crack == chash:
            print(f"{line}:{chash}")
            break
            
        


