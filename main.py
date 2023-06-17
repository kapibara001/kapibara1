def palindrome(word):
    return word[::-1] == word

while True:
    word = input("Введите слово для проверки: ") 
    
    if word == "q":
        break
    
    print(f"{word} палиндром." if palindrome(word) else "не палиндром.")
