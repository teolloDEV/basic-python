from Crypto.Cipher import AES


data = b'This is the data I will encrypt'
key = b'th1s1smyk3yh3h3h'

#Encrypt

chiper = AES.new(key, AES.MODE_EAX)
nonce = chiper.nonce
chiper_text, tag = chiper.encrypt_and_digest(data)

print(chiper_text, '\n', tag, '\n', nonce, '\n')

#Description

key = b'th1s1smyk3yh3h3h'
chiper = AES.new(key, AES.MODE_EAX, nonce)
plaintext = chiper.decrypt(chiper_text)
try:
    chiper.verify(tag)
    print(plaintext.decode())
except ValueError:
    print('the key you entered is wrong')

