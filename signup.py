import csv
from koleksi.getpass_ak import getpass
from koleksi.hashing import *

#perhatian: kami menggunakan import 'lain' bertujuan agar pengisian password di cmd dalam bentuk asterisk
#hal ini semata-mata hanya untuk keindahan. Mengenai spesifikasi tidak menggunakan library lain
#sudah dilakukan seutuhnya pada keseluruhan program yang "fungsional" selain "tujuan keindahan".
# Semoga dapat dimaklumi dan dimengerti terima kasih :) .


#inisialisasi list user
users = [['','','',0,'','','',0] for i in range(100)]


def find(username):
    i = 0
    while i<100:
        if users[i][3] == username:
                print("Username sudah terpakai. Silahkan mencoba username lain.")
                return True
        else:
                i += 1
    if i==100:
        return False
    

def newUser():
        global counter
        counter = 0
        nama = input("Masukkan nama pemain: ")
        ttl = input("Masukkan tanggal lahir pemain (DD/MM/YY): ")
        tinggi = int(input("Masukkan tinggi badan pemain (cm): "))
        username = input("Masukkan username pemain: ")
        while find(username):
            username = input("Masukkan username pemain: ")
        password = getpass(prompt="Masukkan password pemain: ")
        saldo = 0
        users[counter][:] = [nama,ttl,tinggi,username,(hashing(password)),'pemain',saldo]
        
        

def signup():
    newUser()

    with open("bayangan.csv", 'a',newline='') as file:
        writer = csv.writer(file,delimiter=',')
        writer.writerow(users[counter])

