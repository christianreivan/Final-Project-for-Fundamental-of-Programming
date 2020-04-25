import csv
from koleksi.getpass_ak import getpass
from koleksi.hashing import *

def isUsernameRight(username):
    global data
    global count
    data = [[] for i in range(100)]
    with open("bayangan.csv", 'r', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        count = 0
        for line in (reader):
            data[count] = line
            count += 1
    i = 0
    while i < count:
        if username == data[i][3]:
            return True
        else:
            i += 1
    if i == count:
        return False


def isPasswordRight(password):
    global data
    global count
    i = 0
    while i < count:
        if(hashing(password) == data[i][4]):
            return True
        else:
            i += 1
    return False
    # if hashing(password) in slot[key(password)]:
    #     print(hashing(password))
    #     return True
    # else:
    #     return False

def login():
    with open("bayangan.csv", 'r') as file:
        username = input("Masukkan username: ")
        password = getpass(prompt="Masukkan password: ")
        if isUsernameRight(username) and isPasswordRight(password):
            print("Selamat bersenang-senang, Willy Wangky!")
        else:

            while True:
                print("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
                username = input("Masukkan username: ")
                password = getpass(prompt="Masukkan password: ")
                a = isUsernameRight(username)
                b = isPasswordRight(password)
                if a == True and b == True:
                    break
            if isUsernameRight(username) and isPasswordRight(password):
                print("Selamat bersenang-senang, Willy Wangky!")
