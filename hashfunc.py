import hashlib


def calculate_file_hash(file_path, hash_algorithm="sha256", bufsize=1024):
    hash_object = hashlib.new(hash_algorithm)
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(bufsize), b''):
            hash_object.update(chunk)
    return hash_object.hexdigest()
