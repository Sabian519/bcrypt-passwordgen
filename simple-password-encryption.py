import bcrypt

def encrypt_password():
    """
    Fungsi untuk menerima input password dari user,
    mengenkripsi password tersebut, dan menampilkan hasilnya
    """
    # Menerima input password dari user
    password = input("Masukkan password Anda: ")
    
    # Mengenkripsi password
    if isinstance(password, str):
        password_bytes = password.encode('utf-8')
    
    # Generate salt dan hash password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    
    # Mengkonversi bytes ke string untuk tampilan yang lebih rapi
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
        
        # Verifikasi password
        is_valid = bcrypt.checkpw(test_password_bytes, hashed_password)
        
        if is_valid:
            print("Verifikasi berhasil! Password cocok.")
        else:
            print("Verifikasi gagal! Password tidak cocok.")

# Jalankan program
if __name__ == "__main__":
    print("Program Enkripsi Password dengan Bcrypt")
    print("====================================")
    
    while True:
        encrypt_password()
        
        # Tanya apakah ingin mencoba lagi
        again = input("\nApakah ingin mencoba password lain? (y/n): ")
        if again.lower() != 'y':
            print("Terima kasih telah menggunakan program ini!")
            break
