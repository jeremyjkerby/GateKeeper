""" 
    vault.py
"""
from Crypto.Cipher import AES
import base64
import csv

def getRecord(key, a):
    """ Get record from CSV file """
    with open("vault.csv") as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            if row[0] == a:
                return (row[0], row[1], str(decryptData(key, row[2])))

    return None

def getAllRecords():
    """ Get all records from CSV file """
    acts = []

    with open("vault.csv") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            acts.append(row[0])

    return acts

def saveRecord(act, usr, pwd):
    """ Save record to CSV file """
    with open('vault.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([act, usr, pwd])

    return None

def encryptData(key, data):
    """ Encrypt data using key """
    obj = AES.new(key, AES.MODE_CBC, 'This is an IV456')
    ciphertext = obj.encrypt(data)

    return base64.b64encode(ciphertext).decode('utf-8')

def decryptData(key, data):
    """ Encrypt data using key """
    obj2 = AES.new(key, AES.MODE_CBC, 'This is an IV456')
    decipheredtext = obj2.decrypt(base64.b64decode(data)).decode('utf-8')

    return decipheredtext


