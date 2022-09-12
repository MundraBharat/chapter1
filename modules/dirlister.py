import os

def run(**args):

    print ("[*] In dirlister module.")
    for i in range(1,500):
        print ("BHARAT MATA ki Jai")
    files = os.listdir(".")

    return str(files)
