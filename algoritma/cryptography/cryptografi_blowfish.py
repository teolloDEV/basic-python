from Crypto.Cipher import Blowfish
from struct import pack

key = b'this is a very secret key'
data = b'This data will be encrypted'

bs = Blowfish.block_size
chiper = Blowfish.new(key, Blowfish.MODE_CBC)

plen = bs - len(data) % bs
padding = [plen] * plen
padding = pack('b' * plen, * padding)
msg = chiper.encrypt(data + padding)

print(msg)