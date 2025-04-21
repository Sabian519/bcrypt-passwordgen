import bcrypt

def encrypt_password():
    """
    Fungsi untuk menerima input password dari user,
    mengenkripsi password tersebut, dan menampilkan hasilnya
    """
    # input password
    password = input("Masukkan password Anda: ")
    
    # fungsi encrypt ygy
    if isinstance(password, str):
        password_bytes = password.encode('utf-8')
    
    # ini fungsi generate
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
  
    hashed_password_str = hashed_password.decode('utf-8')
    
    # Menampilkan hasil
    print("\nHasil Enkripsi:")
    print("--------------")
    print(f"Password asli: {password}")
    print(f"Password terenkripsi: {hashed_password_str}")
    
    # Opsi untuk mencoba verifikasi password
    verify = input("\nApakah ingin mencoba verifikasi password? (y/n): ")
    if verify.lower() == 'y':
        test_password = input("Masukkan password untuk diverifikasi: ")
        test_password_bytes = test_password.encode('utf-8')
      
        is_valid = bcrypt.checkpw(test_password_bytes, hashed_password)
        
        if is_valid:
            print("Verifikasi berhasil! Password cocok.")
        else:
            print("Verifikasi gagal! Password tidak cocok.")
if __name__ == "__main__":
    print("Program Enkripsi Password dengan Bcrypt")
    print("====================================")
    
    while True:
        encrypt_password()
        again = input("\nApakah ingin mencoba password lain? (y/n): ")
        if again.lower() != 'y':
            print("Terima kasih telah menggunakan program ini!")
            break
