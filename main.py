from koleksi import *





print("*********")
print("<Pilihan>\t\t\t" + "<(L) Login>")
print("*********\t\t\t" + "<(E) Exit >")
print()

x=3
while x==3:
    choice = (input("\t\t\t\tL or E:  "))
    if choice.lower() == 'l' or choice.lower() == 'e':
        x = 5
        
    else:
        continue

if choice.lower() == 'l':
    login()
    








else:
    jaw = input("Apakah Anda yakin akan keluar? (y/n): ")
    if jaw == 'y':
        exit()
        file1.close()
        file2.close()
        file3.close()
        file4.close()
        file5.close()
        file6.close()
        file7.close()
    
    else:
        main()

    
        
            
