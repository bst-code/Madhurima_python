'''
ch = 'a'
while(ch<='z'):
    print(ch)
    if ch>='a' and ch <='e':
        ch = chr(ord(ch)+1)
    else:
        break
'''


Text1 = "AISSCE 2025"
Text2 =""

i = 0
while(i<=len(Text1)+1):
    print(i ,type(Text1[i]), Text1[i])
    if  Text1[i]>="0" and Text1[i]<="9":
        val = int(Text1[i])
        val = val +1
        Text2 = Text2 + str(val)
        print('Text2',Text2)
    elif str(Text1[i])>="A" and str(Text1[i]) <="Z":
        Text2 = Text2 + (str(Text1[i+1]))
        print('Text2',Text2)
    else:
        Text2 = Text2+"*"
    i = i+1
print(Text2)

