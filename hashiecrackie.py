import hashlib
import sys
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Welcome  to: \n HashieCrackie \n HASH CRACKER for \nMD-5 \nWritten_by_:\nGreatOverlordX")
print(ascii_banner)

wordlist_location = str(input('Enter wordlist file location: '))
hash_input = str(input('Enter hash to be cracked: '))

with open(wordlist_location, 'r') as file:
    for line in file.readlines():
        hash_ob = hashlib.md5(line.strip().encode()) # md5 hash by default // Change this if needed
        HASHED_PASS = hash_ob.hexdigest()
        if HASHED_PASS == hash_input:
            print('Yay! Found cleartext password :D! HERE: ' + line.strip())
            sys.exit(0)


# /usr/share/wordlists/PythonForPentesters/wordlist2.txt
