"""
    vault.py
    Little secrets keeper that utilizes base64, csv, and crypto packages. Encrypt and Decrypt data using SHA256.
"""
from Crypto.Cipher import AES
import base64
import csv


'''get record from file'''
def getRecord(key, a):
    with open("vault.csv") as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            if row[0] == a:
                return (row[0], row[1], str(decryptData(key, row[2])))

    return None

'''get all records from file'''
def getAllRecords():
    acts = []

    with open("vault.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            acts.append(row[0])

    return acts

'''save record to file'''
def saveRecord(act, usr, pwd):
    with open('vault.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([act, usr, pwd])

    return None

""" encrypt data using the key """
def encryptData(key, data):
    obj = AES.new(key, AES.MODE_CBC, 'This is an IV456')
    ciphertext = obj.encrypt(data)

    return base64.b64encode(ciphertext).decode('utf-8')

""" decrypt data using the key """
def decryptData(key, data):
    obj2 = AES.new(key, AES.MODE_CBC, 'This is an IV456')
    decipheredtext = obj2.decrypt(base64.b64decode(data)).decode('utf-8')

    return decipheredtext


