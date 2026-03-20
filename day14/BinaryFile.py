l = [['Bala', 20, 'Yellow'], ['shivya', 7, 'pink']]

print("List printed maually",l)

import pickle

f = open('bspark1.dat','wb')
pickle.dump(l, f)
f.close()

l.append(['John', 99, 'Black'])

print("List printed -->",l)

f = open('bspark1.dat','ab')
pickle.dump(l, f)
f.close()

f = open('bspark1.dat','rb')
content = pickle.load(f)
print("content---->",content)
