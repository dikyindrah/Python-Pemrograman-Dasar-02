import csv
import os
import platform

my_file_path = 'D:/Programming/web/Python/Python-Basic-02/143-Latihan Membuat Program CRUD Dengan File CSV/myfile.csv'

def show_menu():
    print(f"{'='*5}Buku Telepon{'='*5}")
    print('[1] Lihat Daftar Kontak')
    print('[2] Tambah Kontak')
    print('[3] Ubah Kontak')
    print('[5] Hapus Kontak')
    print('[6] Cari Kontak')
    print('[0] Keluar')

    selected_menu = str(input('\nPilih menu : '))
    if selected_menu == '1':
        show_contact()
    elif selected_menu == '2':
        add_contact()
    elif selected_menu == '3':
        update_contact()
    elif selected_menu == '4':
        pass
    elif selected_menu == '5':
        pass
    elif selected_menu == '6':
        pass
    elif selected_menu == '0':
        pass
    else:
        print('\nMenu yang anda pilih tidak diketahui.')
        back_to_menu()

def clear_screen():
    if platform.system() == 'Windows': 
        os.system('cls')
    else: 
        os.system('clear')

def back_to_menu():
    input('\nTekan enter untuk kembali...')
    clear_screen()
    show_menu()

def add_contact_to_temporary():
    contact = []
    with open(my_file_path, mode='r', encoding='UTF-8', newline='\n') as my_csv_file:
        file = csv.DictReader(my_csv_file)
        for data in file:
            contact.append(data)
    
    return contact

def show_contact_from_temporary():
    all_contact = add_contact_to_temporary()
    field = list(all_contact[0].keys())
    
    print(f"{field[0]}\t{field[1]}\t\t{field[2]}")
    for contact in all_contact:
        print(f"{contact['No']}\t{contact['Nama']}\t{contact['Kontak']}")

def show_contact():
    clear_screen()

    print(f"{'='*5}Lihat Daftar Kontak{'='*5}")
    show_contact_from_temporary()

    back_to_menu()

def add_contact():
    clear_screen()
    print(f"{'='*5}Tambah Kontak{'='*5}")
    with open(my_file_path, mode='a', encoding='UTF-8', newline='\n') as my_file_csv:
        fieldnames = ['No','Nama','Kontak']
        file = csv.DictWriter(my_file_csv, fieldnames=fieldnames)
        
        No = str(input('No \t: '))
        Nama = str(input('Nama \t: '))
        Kontak = str(input('Kontak \t: '))

        file.writerow({'No':No,'Nama':Nama,'Kontak':Kontak})
        print('\nKontak berhasil ditambahkan.')
    
    back_to_menu()

def update_contact():
    clear_screen()
    all_contact = add_contact_to_temporary()
    
    print(f"{'='*5}Ubah Kontak{'='*5}")
    show_contact_from_temporary()

    No = str(input('\nPilih nomor data yang ingin anda ubah : '))
    for i in range(len(all_contact)):
        if all_contact[i]['No'] == No:
            clear_screen()
            print(f"{'='*5}Ubah Kontak{'='*5}")
            field = list(all_contact[i].keys())
            print(f"{field[0]}\t{field[1]}\t\t{field[2]}")
            print(f"{all_contact[i]['No']}\t{all_contact[i]['Nama']}\t{all_contact[i]['Kontak']}")

            Nama = str(input('\nNama \t: '))
            Kontak = str(input('Kontak \t: '))
            all_contact[i]['Nama'] = Nama
            all_contact[i]['Kontak'] = Kontak
    
    with open(my_file_path, mode='w', encoding='UTF-8', newline='\n') as my_file_csv:
        fieldnames = ['No', 'Nama', 'Kontak']
        file = csv.DictWriter(my_file_csv, fieldnames=fieldnames)
        file.writeheader()
        file.writerows(all_contact)
    
    back_to_menu()

def delete_contact():
    pass


show_menu()