# Ferientage aus dem Dashboard entnehmen
print(
    "Hier können wir abgleichen, ob ein angefragter Tag in die Ferienzeit fällt oder nicht."
)
print(" ")
date = input("Um welchen Tag geht es? (Eingabe bitte im Format YYYY.MM.DD) ")
print(" ")
is_winter = date >= "2024.12.24" and date <= "2025.01.01"  # Winterferien
is_easter = date >= "2025.04.18" and date <= "2025.04.21"  # Osterferien
is_summer = date >= "2025.08.11" and date <= "2025.08.19"  # Sommerferien
is_winter2 = date >= "2025.12.24" and date <= "2026.01.01"  # Winterferien2
is_workday = date == "2025.05.01"  # Tag der Arbeit
is_himmelfahrt = date == "2025.05.29"  # Christi Himmelfahrt
is_pfingsten = date == "2025.06.09"  # Pfingstmontag
is_unity = date == "2025.10.03"  # Tag der deutschen Einheit
is_reform = date == "2025.10.31"  # Reformationstag

if is_winter:
    print("Es sind Winterferien")
elif is_easter:
    print("Es sind Osterferien")
elif is_summer:
    print("Es sind Sommerferien")
elif is_winter2:
    print("Es sind Winterferien")
elif is_workday:
    print("Es ist Tag der Arbeit")
elif is_himmelfahrt:
    print("Es ist Christi Himmelfahrt")
elif is_pfingsten:
    print("Es ist Pfingsten")
elif is_unity:
    print("Es ist Tag der deutschen Einheit")
elif is_reform:
    print("Es ist Reformationstag")
else:
    print("Es ist eine normale Kurswoche")

print(" ")
# Wiederholung
# reset = input("Soll ein weiteres Datum abgefragt werden? (Y/N) ")
# is_yes = reset == "Y" #Eventuell eine Schleife?
# exit
