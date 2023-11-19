def hash_1(string):
    return 1


def hash_2(string):
    lenght = len(string)
    return lenght


def hash_3(string):
    if ord(string[0]) >= ord("a"):
        return (ord(string[0]) - ord("a") + 1) % 10
    else:
        return (ord(string[0]) - ord("A") + 1) % 10


def hash_4(string):
    prime_numbers = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29,
                     'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71,
                     'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}
    string = string.lower()
    total_sum = sum(prime_numbers[char] for char in string if char in prime_numbers)
    hash_value = total_sum % 10
    return hash_value


def hashtable(mas, hash, name, value):
    match hash:
        case 1:
            mas[hash_1(name)] = value
        case 2:
            mas[hash_2(name)] = value
        case 3:
            mas[hash_3(name)] = value
        case 4:
            mas[hash_4(name)] = value


mass = [""] * 10
hashtable(mass, 1, "Esther", "88005553535")
hashtable(mass, 1, "Ben", "88005552525")
hashtable(mass, 1, "Bob", "88005551515")
hashtable(mass, 1, "Dan", "88005550505")
print("Хэш функция 1, имена 5.5", mass)
mass = [""] * 10
hashtable(mass, 2, "Esther", "88005553535")
hashtable(mass, 2, "Ben", "88005552525")
hashtable(mass, 2, "Bob", "88005551515")
hashtable(mass, 2, "Dan", "88005550505")
print("Хэш функция 2, имена 5.5", mass)
mass = [""] * 10
hashtable(mass, 3, "Esther", "88005553535")
hashtable(mass, 3, "Ben", "88005552525")
hashtable(mass, 3, "Bob", "88005551515")
hashtable(mass, 3, "Dan", "88005550505")
print("Хэш функция 3, имена 5.5", mass)
mass = [""] * 10
hashtable(mass, 4, "Esther", "88005553535")
hashtable(mass, 4, "Ben", "88005552525")
hashtable(mass, 4, "Bob", "88005551515")
hashtable(mass, 4, "Dan", "88005550505")
print("Хэш функция 4, имена 5.5", mass)
mass = [""] * 10
hashtable(mass, 1, "A", "1.5")
hashtable(mass, 1, "AA", "1.5")
hashtable(mass, 1, "AAA", "1.5")
hashtable(mass, 1, "AAAA", "9")
print("Хэш функция 1, имена 5.6", mass)
mass = [""] * 10
hashtable(mass, 2, "A", "1.5")
hashtable(mass, 2, "AA", "1.5")
hashtable(mass, 2, "AAA", "1.5")
hashtable(mass, 2, "AAAA", "9")
print("Хэш функция 2, имена 5.6", mass)
mass = [""] * 10
hashtable(mass, 3, "A", "1.5")
hashtable(mass, 3, "AA", "1.5")
hashtable(mass, 3, "AAA", "1.5")
hashtable(mass, 3, "AAAA", "9")
print("Хэш функция 3, имена 5.6", mass)
mass = [""] * 10
hashtable(mass, 4, "A", "1.5")
hashtable(mass, 4, "AA", "1.5")
hashtable(mass, 4, "AAA", "1.5")
hashtable(mass, 4, "AAAA", "9")
print("Хэш функция 4, имена 5.6", mass)
mass = [""] * 10
hashtable(mass, 1, "Maus", "Art Spiegelman")
hashtable(mass, 1, "Fun Home", "Alison Bechdel")
hashtable(mass, 1, "Watchmen", "Alan Moore")
print("Хэш функция 1, имена 5.7", mass)
mass = [""] * 10
hashtable(mass, 2, "Maus", "Art Spiegelman")
hashtable(mass, 2, "Fun Home", "Alison Bechdel")
hashtable(mass, 2, "Watchmen", "Alan Moore")
print("Хэш функция 2, имена 5.7", mass)
mass = [""] * 10
hashtable(mass, 3, "Maus", "Art Spiegelman")
hashtable(mass, 3, "Fun Home", "Alison Bechdel")
hashtable(mass, 3, "Watchmen", "Alan Moore")
print("Хэш функция 3, имена 5.7", mass)
mass = [""] * 10
hashtable(mass, 4, "Maus", "Art Spiegelman")
hashtable(mass, 4, "Fun Home", "Alison Bechdel")
hashtable(mass, 4, "Watchmen", "Alan Moore")
print("Хэш функция 4, имена 5.7", mass)
