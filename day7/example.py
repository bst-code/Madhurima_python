#Dict Example

name = "BBalaaaa"
D ={}

for ch in name:
    if ch in D:
        D[ch] = D.get(ch) + 1  # Key present so, value incremented by 1
    else:
        D[ch] = 1 # new key added with value = 1

print(D)
    
