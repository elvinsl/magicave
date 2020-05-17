from cryptography.fernet import Fernet
import argparse


def banner():
    print('''
+-----------------------------------------------+
| magicave file encryptor                       | 
| magicave v.0.1                                |
| Author: Elvin --> 'elvinsl'                   |
| Github: https://github.com/elvinsl/magicave   |
+-----------------------------------------------+  
    ''')


class EncDec:
    @classmethod
    def generate(cls, file):
        f = Fernet.generate_key()
        with open(file, 'wb') as key_file:
            key_file.write(f)

    @classmethod
    def encrypt(cls, file, key_file):
        key = open(key_file, 'rb').read()
        f = Fernet(key)
        with open(file, 'rb') as normal_file:
            file_data = normal_file.read()
        enc_data = f.encrypt(file_data)
        with open(file, 'wb') as normal_file:
            normal_file.write(enc_data)

    @classmethod
    def decrypt(cls, file, key_file):
        key = open(key_file, 'rb').read()
        f = Fernet(key)
        with open(file, 'rb') as enc_file:
            enc_data = enc_file.read()
        dec_data = f.decrypt(enc_data)
        with open(file, 'wb') as enc_file:
            enc_file.write(dec_data)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='file',
                        help='File to encrypt or decryp')
    parser.add_argument('-k', '--key', dest='key',
                        help='Key to encrypt or decrypt')
    parser.add_argument('-e', '--encrypt', dest='enc',
                        help='Encrypt the file with given key', action='store_true')
    parser.add_argument('-d', '--decrypt', dest='dec',
                        help='Decrypt the file with given key', action='store_true')
    parser.add_argument('-g', '--generate', dest='generate',
                        help='Generate new key file')
    dest_value = parser.parse_args()
    return dest_value


args = get_args()
banner()

if args.generate:
    EncDec().generate(args.generate)
elif args.dec and args.file and args.key:
    EncDec().decrypt(args.file, args.key)
elif args.enc and args.file and args.key:
    EncDec().encrypt(args.file, args.key)
else:
    print('''
Usage: '--help' for more info
Generate Key: python3 magicave.py --generate key.txt
Encrypt File: python3 magicave.py --encrypt --file <file> --key <key>
Encrypt File: python3 magicave.py --decrypt --file <file> --key <key>
    ''')
