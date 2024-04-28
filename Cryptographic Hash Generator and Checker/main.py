import hashlib
import os

def generate_hash(data, algorithm='sha256'):
    try:
        hash_obj = hashlib.new(algorithm)
        hash_obj.update(data)
        return hash_obj.hexdigest()
    except ValueError:
        print(f"Unsupported hash algorithm: {algorithm}")
        return None

def hash_string():
    input_string = input("Enter the string to generate hash: ")
    algorithm = input("Enter the hashing algorithm (default is sha256): ")
    print("Hash:", generate_hash(input_string.encode(), algorithm))

def hash_file():
    file_path = input("Enter the path of the file to generate hash: ")
    algorithm = input("Enter the hashing algorithm (default is sha256): ")
    
    if not os.path.exists(file_path):
        print("File not found.")
        return

    with open(file_path, 'rb') as file:
        print("Hash:", generate_hash(file.read(), algorithm))

def compare_hashes():
    file_path1 = input("Enter the path of the first file: ")
    file_path2 = input("Enter the path of the second file: ")
    algorithm = input("Enter the hashing algorithm (default is sha256): ")

    if not (os.path.exists(file_path1) and os.path.exists(file_path2)):
        print("One or both files not found.")
        return

    hash1 = generate_hash(open(file_path1, 'rb').read(), algorithm)
    hash2 = generate_hash(open(file_path2, 'rb').read(), algorithm)

    if hash1 is not None and hash2 is not None:
        if hash1 == hash2:
            print("Hashes match: Files have not been tampered with.")
        else:
            print("Hashes do not match: Files may have been altered.")

def main():
    print("1. Generate hash for a string")
    print("2. Generate hash for a file")
    print("3. Compare hashes of two files")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        hash_string()
    elif choice == '2':
        hash_file()
    elif choice == '3':
        compare_hashes()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
