import csv


def wahana_search():
    batasan_umur = ['Anak-anak (<17 tahun)','Dewasa (>=17 tahun)', 'Semua umur']
    batasan_tinggi = ['Lebih dari 170 cm','Tanpa batasan']
    print("Jenis batasan umur: ")
    for i in range(3):
        print(str(i+1) + ".  " + str(batasan_umur[i]))
    print()
    print("Jenis batasan tinggi badan: ")
    for i in range(2):
        print(str(i+1) + ".  " + str(batasan_tinggi[i]))
    print()
    flag = True
    flags = True
    while flag:
        pilihan_umur = input("Batasan umur pemain: ")
        if pilihan_umur == '1' or pilihan_umur == '2' or pilihan_umur == '3':
            flag = False
        else:
            print("Batasan umur tidak valid!")
    
    while flags:
        pilihan_tinggi = input("Batasan tinggi badan: ")
        if pilihan_tinggi == '1' or pilihan_tinggi == '2':
            flags= False
            if pilihan_tinggi == '2':
                pilihan_tinggi = 'none'
        else:
            print("Batasan tinggi badan tidak valid!")

    with open("wahana.csv", 'r', newline='') as file:
        bound = csv.reader(file, delimiter=',')
        next(bound)
        count = 0
        data = [[] for i in range(100)]
        for baris in (bound):
            data[count] = baris
            count += 1

        wahana_found = [0 for i in range(count)]

        print("Hasil Pencarian:")
        pos = 0

        if pilihan_umur == '1' and pilihan_tinggi == '1':
            for i in range(count):
                if data[i][4] != 'none':
                    if int(data[i][3]) < 17 and int(data[i][4]) > 170 :
                        pos += 1
                        print(str(data[i][0]) + " | " + str(data[i][1]) + " | " + str(data[i][2]))
                else:
                    continue


        elif pilihan_umur == '1' and pilihan_tinggi == 'none':
            for i in range(count):
                if int(data[i][3]) < 17 and data[i][4] == 'none':
                    pos += 1
                    print(str(data[i][0]) + " | " + str(data[i][1]) + " | " + str(data[i][2]))


        elif pilihan_umur == '2' and pilihan_tinggi == '1':
            for i in range(count):
                if data[i][4] != 'none':
                    if int(data[i][3]) >= 17 and int(data[i][4]) > 170 :
                        pos += 1
                        print(str(data[i][0]) + " | " + str(data[i][1]) + " | " + str(data[i][2]))
                else:
                    continue
                    
        elif pilihan_umur == '2' and pilihan_tinggi == 'none':
            for i in range(count):
                if int(data[i][3]) >= 17 and data[i][4] == 'none':
                    pos += 1
                    print(str(data[i][0]) + " | " + str(data[i][1]) + " | " + str(data[i][2]))


        elif pilihan_umur == '3' and pilihan_tinggi == '1':
            for i in range(count):
                if data[i][4] != 'none':    
                    if int(data[i][4]) > 170 :
                        pos += 1
                        print(str(data[i][0]) + " | " + str(data[i][1]) + " | " + str(data[i][2]))
                else:
                    continue

        elif pilihan_umur == '3' and pilihan_tinggi == 'none':
            for i in range(count):
                if data[i][4] == 'none':
                    pos += 1
                    print(str(data[i][0]) + " | " + str(data[i][1]) + " | " + str(data[i][2]))
        
        if pos == 0:
            print("Tidak ada wahana yang sesuai dengan pencarian kamu.")

