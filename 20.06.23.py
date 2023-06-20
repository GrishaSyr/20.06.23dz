def palindrome(s): 
return s[::-1] == s 

while True: 
s = input("введите слово: ") 
print(f"{s} это слово палиндром" if 
palindrome(s) else "это слово не палиндром")
