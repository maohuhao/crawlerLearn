from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import base64
import binascii

def get_encrypt_pwd(pwd):
    key = b'abcd1234'
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(pwd.encode(), DES.block_size, style='pkcs7')
    encrypted_text = des.encrypt(padded_text)
    return base64.b64encode(encrypted_text).decode('utf-8')


if __name__ == "__main__":
    pass
