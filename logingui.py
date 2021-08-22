import tkinter as tk
import os

# membuat halaman register


def register():
    global halaman_register

    halaman_register = tk.Toplevel(halaman_awal)
    halaman_register.title('Register')
    halaman_register.geometry('350x250')

    global username
    global password
    global username_entry
    global password_entry

# membuat variabel teks
    username = tk.StringVar()
    password = tk.StringVar()

# membuat label judul
    tk.Label(halaman_register, text='Silahkan isi data dibawah ini',
             bg='green', fg='white').pack()
    tk.Label(halaman_register, text='').pack()

# membuat label username
    user_label = tk.Label(halaman_register, text='Username *')
    user_label.pack()

# membuat entry username
    username_entry = tk.Entry(halaman_register, textvariable=username)
    username_entry.pack()

# membuat label password
    password_label = tk.Label(halaman_register, text='Password *')
    password_label.pack()

# membuat entry password
    password_entry = tk.Entry(
        halaman_register, textvariable=password, show="*")
    password_entry.pack()
    tk.Label(halaman_register, text=('')).pack()

# membuat tombol daftar
    tk.Button(halaman_register, text='Register', width=10, height=1,
              bg='green', fg='white', command=register_user).pack()

# menyimpan data register


def register_user():
    username_info = username.get()
    password_info = password.get()

# membuka file dan mengisi user dan pass
    file = open(username_info, 'w')
    file.write(username_info + '\n')
    file.write(password_info)
    file.close()

    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# membuat label regis berhasil
    tk.Label(halaman_register, text='Registrasi Berhasil!',
             fg='green', font='calibri 14').pack()

# membuat halaman login


def login():
    global halaman_login
    halaman_login = tk.Toplevel(halaman_awal)
    halaman_login.geometry('350x250')
    halaman_login.title('Halaman Login')

    tk.Label(halaman_login, text='Masukkan username dan password anda').pack()
    tk.Label(halaman_login, text='').pack()

    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry

    username_verify = tk.StringVar()
    password_verify = tk.StringVar()

    tk.Label(halaman_login, text='Username :').pack()
    tk.Label(halaman_login, text='').pack()

    username_login_entry = tk.Entry(
        halaman_login, textvariable=username_verify)
    username_login_entry.pack()

    tk.Label(halaman_login, text='Password :').pack()
    tk.Label(halaman_login, text='').pack()

    password_login_entry = tk.Entry(
        halaman_login, textvariable=password_verify, show="*")
    password_login_entry.pack()

    tk.Button(halaman_login, text='Login', width=10,
              height=1, command=login_verification).pack()

# membuat verifikasi login


def login_verification():
    username1 = username_verify.get()
    password1 = password_verify.get()
# menghapus data
    username_login_entry.delete(0, tk.END)
    password_login_entry.delete(0, tk.END)

    list_of_files = os.listdir()

    if username1 in list_of_files:
        file1 = open(username1, 'r')  # membuka file dengan mode read
        verify = file1.read().splitlines()
        if password1 in verify:
            login_berhasil()
        else:
            password_not_recognised()
    else:
        user_not_found()

# membuat popup login berhasil


def login_berhasil():
    global halaman_login_berhasil
    halaman_login_berhasil = tk.Toplevel(halaman_login)
    halaman_login_berhasil.geometry('150x100')
    halaman_login_berhasil.title("Berhasil")

    tk.Label(halaman_login_berhasil, text='Login Berhasil!').pack()

    tk.Button(halaman_login_berhasil, text='OK',
              command=delete_login_berhasil).pack()


def delete_login_berhasil():
    halaman_login_berhasil.destroy()
    halaman_login.destroy()


def password_not_recognised():
    global halaman_pass_not_recog
    halaman_pass_not_recog = tk.Toplevel(halaman_awal)
    halaman_pass_not_recog.geometry('150x100')
    halaman_pass_not_recog.title('Password Salah')

    tk.Label(halaman_pass_not_recog, text='Password Salah').pack()
    tk.Button(halaman_pass_not_recog, text='OK',
              command=delete_pass_not_recog).pack()


def delete_pass_not_recog():
    halaman_pass_not_recog.destroy()

# membut popup user not found


def user_not_found():
    global halaman_user_not_found
    halaman_user_not_found = tk.Toplevel(halaman_login)
    halaman_user_not_found.geometry('300x100')
    halaman_user_not_found.title('Not Found')

    tk.Label(halaman_user_not_found,
             text='Pengguna tidak ditemukan, Silahkan register').pack()
    tk.Button(halaman_user_not_found, text='OK',
              command=delete_user_not_found).pack()


def delete_user_not_found():
    halaman_user_not_found.destroy()

# Membuat halaman awal


def halaman_akun_awal():
    global halaman_awal

    halaman_awal = tk.Tk()
    halaman_awal.geometry('350x250')
    halaman_awal.title('Login Akun')

# membuat label
    tk.Label(text='Pilih Login atau Register', bg='cyan',
             width=300, height=2, font='calibri 13').pack()
    tk.Label(text='').pack()

# membuat tombol login
    tk.Button(text='Login', height=2, width=30, command=login).pack()
    tk.Label(text='').pack()

# membuat tombol daftar
    tk.Button(text='Register', height=2, width=30, command=register).pack()
    halaman_awal.mainloop()


halaman_akun_awal()
