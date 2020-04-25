# slot = [[] for i in range(1000)]
def hashing(password):
    new = "STEI"
    for i in range(len(str(password))):
        hashed = str(((ord(str(password)[i]) * 7) % 10 + i))
        new += hashed[-1]
    return new

# def key(password):
#     hash_key = ord(str(password)[0]) * 2020 % 1000
#     return hash_key

# print(slot)
