# GateKeeper

## Purpose
Project used to explore how you could store credentials using Pycrypto library

## Fucntionality
Use a key to hash and un-hash information.

## Installation
```bash
pip3 install pycrypto
```

## Sample Execution and Output
```bash
$ ./driver -h
usage: driver.py [-h] [-r] [-w] [-a] [-act ACCOUNT] [-usr USERNAME]
                 [-pwd PASSWORD]

Vault: Save and retieve account information. Data saved using AES hashing.

optional arguments:
  -h, --help            show this help message and exit
  -r, --read            Read record from vault
  -w, --write           Write record from vault
  -a, --all             Read all records in vault
  -act ACCOUNT, --account ACCOUNT
                        Name of the account
  -usr USERNAME, --username USERNAME
                        Username for account
  -pwd PASSWORD, --password PASSWORD
                        Password for account
```


