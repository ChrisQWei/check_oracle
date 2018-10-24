#author: Chris
#email: christopherqiwei@gmail.com
#Encrypt & Decrypt using PyCrypto AES 256 From http://stackoverflow.com/a/12525165/119849
#coding: utf8

import base64
from Crypto import Random
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]


class AESCipher:

    def __init__(self, key):
        self.key = key

    def encrypt(self, raw):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt( self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[16:]))



if __name__ == '__main__':
    cipher = AESCipher('mysecretpassword')
    encrypted = cipher.encrypt('1231231231231')
    decrypted = cipher.decrypt(encrypted)
    print(encrypted)
    print(decrypted)