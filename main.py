from crypto_utils import encrypt_file, decrypt_file, generate_key

def main():
    while True:
        print("\n===== FILE ENCRYPTION TOOL =====")
        print("1. Generate Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_key()

        elif choice == "2":
            file_path = input("Enter file path to encrypt: ")
            encrypt_file(file_path)

        elif choice == "3":
            file_path = input("Enter encrypted file path: ")
            decrypt_file(file_path)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
