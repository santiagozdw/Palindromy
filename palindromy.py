palindrom = '"U Gorgon" je loda Ikar. Bawi po balu car. Da łowy. Na lwicę troglodyta i "Rak", co ma moc kariatyd. Olgo - rtęci! Wlany woła Dracula, bo piwa braki. A dolej no grogu!'

palindrom_without_special_chars = ''.join(e for e in palindrom if e.isalnum())

letters = palindrom_without_special_chars.replace(" ","")[::-1]
if palindrom_without_special_chars.replace(" ","").lower() == letters.lower():
    print ("To jest palindrom")
else:
    print("Nie jest to palindrom")
