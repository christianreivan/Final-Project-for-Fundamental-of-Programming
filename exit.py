from koleksi.save import *

def exit():
    choice = input("Apakah Anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? : ")
    if choice=='Y':
        save()
        print()
        print("^_^")
        print("Save berhasil. Terima kasih telah bermain, Willy Wangky!")
    elif choice=='N':
        print("Anda tidak melakukan save. Terima kasih telah bermain, Willy Wangky!")
