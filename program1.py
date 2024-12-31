# Funkce pro filtrování čísel větších než limit
def filtruj_cisla(numbers, limit):
    
    return [number for number in numbers if number > limit]

# Funkce pro vrácení délek řetězců
def delky_retezcu(strings):

    return [len(string) for string in strings]

# Testování funkcí
if __name__ == "__main__":
    # Test 1: Filtrace čísel
    cisla = [3, 10, 7, 20, 15]
    limit = 10
    vysledek_cisla = filtruj_cisla(cisla, limit)
    print("Čísla větší než limit:", vysledek_cisla)

    retezce = ["ahoj", "programování", "Python", "zábava"]
    vysledek_delky = delky_retezcu(retezce)
    print("Délky řetězců:", vysledek_delky)
