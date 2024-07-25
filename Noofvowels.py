s=input()
vowels=['a','e','i','o','u']
countofVowels=0
s=s.lower()
for i in range(len(s)):    #for i in s:
    if s[i] in vowels:
        countofVowels+=1
print(countofVowels)
