from cryptography.fernet import Fernet
import os

KEY_FILE = "key.key"


def generate_key():
    """
    🔐 Generates a new encryption key and saves it.
    """
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

    print("🔐 Encryption key generated and saved as key.key ✅")


def load_key():
    """
    📂 Loads the encryption key.
    If not found, generates a new one.
    """
    if not os.path.exists(KEY_FILE):
        print("⚠️ Key not found. Generating new key...")
        generate_key()

    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


def encrypt_file(file_path):
    """
    🔒 Encrypts a file and stores it in the 'encrypted' folder.
    """
    if not os.path.exists(file_path):
        print("❌ File does not exist!")
        return

    key = load_key()
    fernet = Fernet(key)

    print("🔄 Encrypting file...")

    with open(file_path, "rb") as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)

    os.makedirs("encrypted", exist_ok=True)

    encrypted_path = os.path.join(
        "encrypted",
        os.path.basename(file_path) + ".enc"
    )

    with open(encrypted_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"✅ File encrypted successfully → {encrypted_path}")


def decrypt_file(file_path):
    """
    🔓 Decrypts a .enc file and restores original file.
    """
    if not os.path.exists(file_path):
        print("❌ Encrypted file does not exist!")
        return

    key = load_key()
    fernet = Fernet(key)

    print("🔄 Decrypting file...")

    with open(file_path, "rb") as enc_file:
        encrypted_data = enc_file.read()

    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except Exception:
        print("🚫 Invalid key or corrupted file!")
        return

    decrypted_path = os.path.splitext(file_path)[0]

    with open(decrypted_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"🎉 File decrypted successfully → {decrypted_path}")
