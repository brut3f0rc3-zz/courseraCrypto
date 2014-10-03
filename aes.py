from binascii import hexlify, unhexlify
from Crypto.Cipher import AES
from Crypto.Util import Counter

def aes_cbc(key, cipher, mode):

    print "The length of key is %d" %(len(key))
    print "The length of cipher is %d" %(len(cipher))
    key = unhexlify(key)
    cipher = unhexlify(cipher)
    if mode == "CBC":
        aes = AES.new(key,AES.MODE_CBC,cipher[0:16])
    elif mode == "CTR":
        ctr = Counter.new(128, initial_value=long(cipher[:16].encode('hex'), 16))
        aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    else:
        print "Mode couldn't be detected!"

    plain = aes.decrypt(cipher[16:])
    print plain


def main():
    while True:
        cipher = raw_input("Enter the cipher string :: ")
        key =  raw_input("Enter the key string :: ")
        mode = raw_input("Enter the mode :: ")
        aes_cbc(key, cipher, mode.upper())
        reply = raw_input("Continue? ")
        if reply <> "Y" or reply <> "y":
            break


if __name__=="__main__":
    main()