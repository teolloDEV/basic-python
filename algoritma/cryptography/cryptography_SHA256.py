from Crypto.Hash import SHA256

data = b'I will encrypt this data'
hasher = SHA256.new()
hasher.update(data)
result = hasher.hexdigest()

print(result)