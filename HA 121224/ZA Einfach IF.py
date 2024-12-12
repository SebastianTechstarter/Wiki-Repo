# Einfache IF-Funktion

# Ein einfaches Programm, was vom User eine Zahl erfragt
# und dann abgleicht, ob diese negativ, positiv oder null ist.

print("Wir entscheiden nun, ob eine eingegebene Zahl positiv oder negativ ist")
print("")
zahl=input("Welche Zahl soll überprüft werden? ")
x=float(zahl)

print(" ")

# Einsatz der Funktion mit if, elif und else
if x<0:
    print("Die Zahl ist negativ")
elif x==0:
    print("Die Zahl ist Null")
else:
    print("Die Zahl ist positiv")

# Leerzeile aus optischen Gründen
print(" ")