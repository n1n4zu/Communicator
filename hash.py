import hashlib


def Hash(hash_text):
    sha256 = hashlib.sha256()

    bajty_text = hash_text.encode('utf-8')

    sha256.update(bajty_text)

    zahashowany_tekst = sha256.hexdigest()

    return zahashowany_tekst
