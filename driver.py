"""
    driver.py
"""
import argparse
import vault as v


parser = argparse.ArgumentParser(description='Vault: Save and retieve account information. Data saved using AES hashing.')
parser.add_argument('-r', '--read', help='Read record from vault', action='store_true')
parser.add_argument('-w', '--write', help='Write record from vault', action='store_true')
parser.add_argument('-a','--all', help='Read all records in vault', action='store_true')

parser.add_argument('-act','--account', help='Name of the account', required=False)
parser.add_argument('-usr','--username', help='Username for account', required=False)
parser.add_argument('-pwd','--password', help='Password for account', required=False)

args = parser.parse_args()


if __name__ == '__main__':
    if (args.read):
        if (args.account == None):
            print(":> [ERROR] Params not correct. Expecting -act")
        else:
            key = ""

            act = v.getRecord(key, args.account)
            if (act != None):
                print(":> Information")
                print("\tAccount: " + act[0] + "\n\tUsername: " + act[1] + "\n\tPassword: " + act[2])
            else:
                print(":> Not found.")

    elif (args.write):
        if (args.account == None or args.username == None or args.password == None):
            print(":> [ERROR] Params not correct. Expecting -act && -usr && -pwd")
        else:
            print(":> Writting record " + args.account + " " + args.username + " " + args.password)

            key = ""

            data = v.encryptData(key, args.password) # encrypt the pass
            v.saveRecord(args.account, args.username, str(data)) # save record

    elif (args.all):
        acts = v.getAllRecords()
        print(":> Accounts")
        for act in acts:
            print("\t" + act)

    else:
        print(":> [ERROR] Invalid argument.")


