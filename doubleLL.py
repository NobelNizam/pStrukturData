class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    # Menambahkan node baru di akhir double linked list
    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:  # Jika list kosong, jadikan node sebagai head
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse sampai ke node terakhir
                current = current.next
            current.next = new_node
            new_node.prev = current

    # Menampilkan data dari depan ke belakang
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
    
    # Menampilkan data dari belakang ke depan
    def display_backward(self):
        current = self.head
        if current is None:
            return
        while current.next:  # Cari node terakhir (tail)
            current = current.next
        while current:  # Traverse dari tail ke head
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")
    
    # Menghapus node berdasarkan indeks
    def delete_at_index(self, index):
        if self.head is None:  # Jika list kosong
            print("List kosong, tidak ada yang dapat dihapus.")
            return
        
        current = self.head
        
        # Jika node yang dihapus adalah head
        if index == 0:
            print(f'Menghapus node dengan data: "{current.data}" di indeks {index}')
            self.head = current.next
            if self.head is not None:
                self.head.prev = None
            return
        
        # Traverse untuk menemukan node di indeks yang diinginkan
        count = 0
        while current is not None and count != index:
            current = current.next
            count += 1

        # Jika indeks melebihi jumlah node
        if current is None:
            print(f"Tidak ada node di indeks {index}.")
            return
        
        print(f'Menghapus node dengan data: "{current.data}" di indeks {index}')
        
        # Jika node yang dihapus bukan head atau tail
        if current.next is not None:
            current.next.prev = current.prev
        if current.prev is not None:
            current.prev.next = current.next

# Membuat double linked list dan menambahkan node
dllist = DoubleLinkedList()
dllist.add_node(10)
dllist.add_node(20)
dllist.add_node(30)
dllist.add_node(40)

# Menampilkan linked list dari depan ke belakang
print("Double Linked List (Forward):")
dllist.display_forward()

# Menampilkan linked list dari belakang ke depan
print("\nDouble Linked List (Backward):")
dllist.display_backward()

# Menghapus node pada indeks 2
dllist.delete_at_index(2)

# Menampilkan linked list setelah penghapusan
print("\nDouble Linked List Setelah Penghapusan (Forward):")
dllist.display_forward()


'''
-Penjelasan Proses Penghapusan!
-Traversal Node: 
Sama seperti single linked list, kita melakukan traversal dari head
untuk menemukan node di indeks tertentu.

-Memperbarui Pointer: 
Untuk menghapus node, kita perlu memperbarui pointer next dari node
sebelumnya dan pointer prev dari node setelahnya, sehingga mereka melewati node yang dihapus.

-Penghapusan Node Pertama atau Terakhir:
Jika node yang dihapus adalah head atau tail, kita memperbarui pointer dari head atau tail.

-Kelebihan Double Linked List!
Traversal Dua Arah: 
Anda dapat menjelajahi linked list baik dari depan ke belakang maupun dari belakang ke depan.

-Penghapusan dan Penambahan Lebih Mudah: 
Karena setiap node memiliki pointer ke node sebelumnya,
kita dapat dengan mudah mengakses node sebelumnya tanpa harus melakukan traversal dari head 
seperti pada single linked list.

-Kekurangan Double Linked List!
Penggunaan Memori Lebih Besar:
Karena setiap node memiliki dua pointer (next dan prev), 
double linked list memerlukan lebih banyak memori dibanding single linked list.

-Implementasi Lebih Rumit: 
Kode untuk menambahkan dan menghapus node sedikit lebih rumit karena kita harus menangani 
dua pointer (next dan prev).
Double linked list sangat berguna ketika Anda perlu melakukan operasi traversal dua arah atau 
sering menambah dan menghapus elemen di posisi acak dalam list, seperti pada sistem navigasi 
(sejarah browser) atau struktur data yang memerlukan efisiensi dalam penghapusan dan penambahan
di kedua ujung list.
'''