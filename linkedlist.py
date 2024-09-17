class iniNode:  # analoginya ini adalah gerbong kereta
    def __init__(self, datanya):
        self.datanya = datanya  # variabel yang akan menyimpan data pada gerbong tersebut
        self.next = None    # pointer atau pengait antar gerbong ke gerbong lain

class iniLinkedListnya: # ini adalah wadah linkedlist nya atau keseluruhan kereta
    def __init__(self): # ini konstruksi awal yaitu kepala gerbong keretanya
        self.head = None  # bernilai kosong karena linkedlist nya baru buat
                            # sehingga perlu ditambahkan suatu data baru
    

    # fungsi / method untuk menambahkan data baru pada linkedlist
    def masukin_dong(self, baru):  # fungsi yang akan memasukan nilai pada data/gerbong
        data_baru = iniNode(baru)  # data baru ini akan masuk ke gerbong/datanya
        if self.head is None:
            self.head = data_baru
        else:
            dataTerkini = self.head
            while dataTerkini.next:
                dataTerkini = dataTerkini.next
            dataTerkini.next = data_baru
    
    # fungsi untuk menampilkan isi nilai pada setiap gerbong
    def infokanTugas(self):
        dataTerkini = self.head
        while dataTerkini:
            print('\n',dataTerkini.datanya)
            dataTerkini = dataTerkini.next
    
    # fungsi untuk menghapus isi nilai pertama atau gerbong pertama
    def hapus_data(self):
        if self.head is not None:
            print(f'\ndata -> {self.head.datanya} <- terhapus!')
            self.head = self.head.next
        else:
            print("Tidak ada data terkini!")


# membuat objek gerbong atau wujud aseli data untuk linkedlist nya
ini_data = iniLinkedListnya()

# membuat fungsi untuk user mengisi data yang diinginkan
def inputin_dong():
    while True:
        print('\npilih yang mana syg?')
        print('1 -> isi data')
        print('2 -> hapus data')
        print('3 -> aku keluarr')
        y = input('?-> ')
        if y == '1':
            print('\nMasukin sesuatu ya...')
            x = input('-> ')
            ini_data.masukin_dong(x)

        elif y == '2':
            print('\nyang akan dihapus adalah data pertama!')
            ini_data.infokanTugas()
            ini_data.hapus_data()
            ini_data.infokanTugas()
        elif y == '3':
            ini_data.infokanTugas()
            break
        else:
            print('opsi tidak valid!')
            continue

inputin_dong()


