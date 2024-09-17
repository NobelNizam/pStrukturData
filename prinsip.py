############################ enkapsulasi ##########################
class Laptop:
    # membuat private atribut
    def __init__(self, merk, ram, penyimpanan):
        self.__merk = merk
        self.__ram = ram
        self.__penyimpanan = penyimpanan

    # membuat fungsi atau metode private untuk private atribut ram

    def akses_ram(self):      # ini adalah metode untuk mengakses private atribut ram
        return self.__ram
    def edit_ram(self, ram):  # ini adalah metode untuk mengubah private atribut ram
        self.__ram = ram
    def akses_merk(self):     # ini adalah metode untuk mengakses private atribut merk
        return self.__merk

# fungsi untuk menjalankan tampilan pembuktian enkapulasi
def pembuktian():
    x = input("\nMasukan brand laptop anda: ")
    y = int(input("\nMasukan ram laptop anda: "))
    z = input("\nMasukan storage laptop anda: ")
    laptop1 = Laptop(x,y,z)     # membuat objek dengan class Laptop

    print(f"""
Brand   :{laptop1.akses_merk()}  # ini akan menyebabkan Atribut Error dikarenakan tidak ada metode private khusus
RAM     :{laptop1.akses_ram()}  # bisa diakses karena menggunakan metode private untuk atribut tersebut
Storage :{laptop1._Laptop__penyimpanan} # bisa diakses langsung dikarenakan menggunakan syntax _NamaClass__namaAtribut
""")
    print("\nApakah anda ingin Upgrade RAM anda menjadi 2x lipatnya? (Y/N)")
    jwb = input()
    if jwb == 'Y':
        laptop1.edit_ram(y*2)   # harus menggunakan metodenya agar bisa merubah nilai dari atribut tesebut
        print("RAM telah upgrade! -> ", laptop1.akses())    # demikian juga mengakses nilai dari atribut
    elif jwb == 'N':
        print("Baiklah...")
    else:
        print("Opsi tidak valid, gunakan kapital!")
# pembuktian()

############################ inheritance #########################
class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
# ----------------------------------------------------------------
class Mahasiswa(Manusia):
    def __init__(self, nama, umur, perguruan, nim):
        super().__init__(nama, umur)
        self.perguruan = perguruan
        self.nim = nim

    # ini adalah metode sederhana untuk objek dari class ini
    def otw(self):
        print("Aktivitas Terkini:\n")
        return f"{self.nama} sedang otw {self.perguruan}"
    
    # ini adalah fungsi untuk memperlihatkan informasi atribut objek
    def infokan(self):
        info = f"""\n
{self.perguruan}
nama : {self.nama}
umur : {self.umur}
nim  : {self.nim}
"""
        return info
# ----------------------------------------------------------------
# objek
mahasiswa1 = Mahasiswa('Nobel Nizam F', '20', 'ITERA', '123450117')
# menampilkan objek
# print(mahasiswa1.infokan())
# print(mahasiswa1.otw())

############################ Abstraksi ###########################
from abc import ABC, abstractclassmethod
class BinatangBuas():
    def __init__(self, makanan):
        self.makanan = makanan

    @abstractclassmethod
    def memangsa(self):
        pass

class Harimau(BinatangBuas):
    def __init__(self, makanan, spesies, domisili):
        super().__init__(makanan)
        self.spesies = spesies
        self.domisili = domisili

    def memangsa(self):
        return f"Harimau sedang menerkam mangsa!"

harimau1 = Harimau('Karnivora', 'Benggala', 'Sumatera')
# print(harimau1.memangsa())

########################## Polimorfisme ###########################
class Mesin:
    def mulai(self):
        return "Mesin dinyalakan."

class MesinMobil(Mesin):
    def mulai(self):
        return "Mesin mobil dinyalakan."

class MesinMotor(Mesin):
    def mulai(self):
        return "Mesin motor dinyalakan."

def jalankan_mesin(mesin):
    print(mesin.mulai())

mobil = MesinMobil()
motor = MesinMotor()

jalankan_mesin(mobil)
jalankan_mesin(motor)





