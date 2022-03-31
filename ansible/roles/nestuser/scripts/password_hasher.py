#!/usr/bin/env python3

# Import the SHA256 Hash Algorithm
import sys
from passlib.hash import sha256_crypt

password = sys.argv[1]
# Generate a new salt and hash the provided password
hash = sha256_crypt.hash(password);
# Output
print (hash)

