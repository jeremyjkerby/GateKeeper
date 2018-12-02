# GateKeeper

## Purpose
This is a passion project used to explore how someone could store random credentials using the pycrypto package. In addition, this project utilizes the argparse and csv packages.

## Installation
You may need to install the following packages.
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


