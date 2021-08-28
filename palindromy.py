palindrom = input("Podaj palindrom: ")
letters = palindrom.replace(" ","")[::-1]
if palindrom.replace(" ","").lower() == letters.lower():
    print ("To jest palindrom")
else:
    print("Nie jest to palindrom")
