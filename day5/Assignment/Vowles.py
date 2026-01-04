#Vowels

s = "Bspark Software technologies"
count = 0
vowels = "aeiouAEIOU"

for ch in s:
    if ch in vowels:
        count += 1

print("Vowel count:", count)
