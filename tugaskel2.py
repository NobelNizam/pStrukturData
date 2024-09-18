class Node:
    def __init__(self, name=None, id=None):
        self.name = name  # Nilai untuk nama
        self.id = id      # Nilai untuk id
        self.prev = None  # Pointer ke node sebelumnya
        self.next = None  # Pointer ke node berikutnya

class DoubleLinkedList:
    def __init__(self):
        self.head = None  # Awal linked list
        self.tail = None  # Akhir linked list

    # Fungsi untuk menambah node di depan (bisa nama atau id)
    def add_front(self, name=None, id=None):
        new_node = Node(name=name, id=id)
        if self.head is None:  # Jika list kosong
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Fungsi untuk menambah node di belakang (bisa nama atau id)
    def add_back(self, name=None, id=None):
        new_node = Node(name=name, id=id)
        if self.tail is None:  # Jika list kosong
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # Fungsi untuk menghapus node berdasarkan nama
    def remove_by_name(self, name):
        current = self.head
        while current:
            if current.name == name:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  # Jika node adalah head
                    self.head = current.next
                if current == self.tail:  # Jika node adalah tail
                    self.tail = current.prev
                print(f"Data dengan nama '{name}' berhasil dihapus.")
                return
            current = current.next
        print(f"Nama '{name}' tidak ditemukan.")

    # Fungsi untuk menghapus node berdasarkan id
    def remove_by_id(self, id):
        current = self.head
        while current:
            if current.id == id:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  # Jika node adalah head
                    self.head = current.next
                if current == self.tail:  # Jika node adalah tail
                    self.tail = current.prev
                print(f"Data dengan id '{id}' berhasil dihapus.")
                return
            current = current.next
        print(f"ID '{id}' tidak ditemukan.")

    # Fungsi untuk menampilkan isi linked list
    def display(self):
        current = self.head
        while current:
            print(f"Nama: {current.name}, ID: {current.id}")
            current = current.next

# Fungsi untuk menerima input dari user
def user_input():
    dll = DoubleLinkedList()
    
    while True:
        print("\nMenu:")
        print("1. Tambah nama di depan")
        print("2. Tambah ID di belakang")
        print("3. Tambah ID di depan")
        print("4. Tambah nama di belakang")
        print("5. Hapus berdasarkan nama")
        print("6. Hapus berdasarkan ID")
        print("7. Tampilkan data")
        print("8. Keluar")
        
        choice = input("Pilih opsi (1-8): ")
        
        if choice == "1":
            num = int(input("Berapa banyak nama yang ingin ditambahkan di depan? "))
            for _ in range(num):
                name = input("Masukkan nama: ")
                dll.add_front(name=name)
        
        elif choice == "2":
            num = int(input("Berapa banyak ID yang ingin ditambahkan di belakang? "))
            for _ in range(num):
                id = int(input("Masukkan ID: "))
                dll.add_back(id=id)
        
        elif choice == "3":
            num = int(input("Berapa banyak ID yang ingin ditambahkan di depan? "))
            for _ in range(num):
                id = int(input("Masukkan ID: "))
                dll.add_front(id=id)
        
        elif choice == "4":
            num = int(input("Berapa banyak nama yang ingin ditambahkan di belakang? "))
            for _ in range(num):
                name = input("Masukkan nama: ")
                dll.add_back(name=name)
        
        elif choice == "5":
            num = int(input("Berapa banyak nama yang ingin dihapus? "))
            for _ in range(num):
                name = input("Masukkan nama yang ingin dihapus: ")
                dll.remove_by_name(name)
        
        elif choice == "6":
            num = int(input("Berapa banyak ID yang ingin dihapus? "))
            for _ in range(num):
                id = int(input("Masukkan ID yang ingin dihapus: "))
                dll.remove_by_id(id)
        
        elif choice == "7":
            print("Data dalam linked list:")
            dll.display()
        
        elif choice == "8":
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid, coba lagi.")

# Jalankan fungsi untuk input user
user_input()
