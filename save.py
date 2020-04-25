def load():
    daftar = ['File User','File Daftar Wahana','File Pembelian Tiket','File Penggunaan Tiket','File Kepemilikan Tiket','File Refund Tiket','File Kritik dan Saran']
    global array
    array = ['' for i in range(7)]
    for i in range(7):
        nama_file = input("Masukkan nama " + str(daftar[i]) + ": ")
        array[i] = (nama_file)

    print("File perusahaan Willy Wangky's Chocolate Factory telah diload")
