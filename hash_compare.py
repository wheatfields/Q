# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 10:18:53 2021

@author: adamw
"""
import hashlib


def hashfile(file):
    BUF_SIZE = 65536
    sha256 = hashlib.sha256()
    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

f1_hash = hashfile(r"C:\Users\adamw\Documents\GitHub\Q\read.csv")
f2_hash = hashfile(r"C:\Users\adamw\Documents\GitHub\Q\read2.csv")

if f1_hash==f2_hash:
    print("Both are the same")
    print(f"Hash: {f1_hash}")
else:
    print("Files are different")
    print(f"Hash of file 1: {f1_hash}")
    print(f"Hash of file 2: {f2_hash}")

