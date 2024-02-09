from random import randint
from mainhelper import anonymiserer
# sei hallo te brukern
print("hello")

# må finne et ord som brukeren skal gjette
ordliste = ("chamber", "omen", "skye", "jett", "neon", "iso", "harbor", "killjoy", "raze", "cypher", "viper", "brimstone", "sage", "phoenix", "yoru")
ord_index = randint(0, 14)
ord = ordliste[ord_index]

# la brukeren gjette bokstaver til han har fullført ordet
# lage en loop som lar brukeren gjette flere ganger
# vis hva brukeren har gjettet
feil_bokstaver = []
riktige_bokstaver = []
antall_liv = 5
while True:
    if antall_liv <= 0:
        print("Game Over")
        break
    bokstav = input("Gjett en bokstav")
    if bokstav.lower() == ord:
        print("Du har gjettet riktig, yaaaay")
        break
    if len(bokstav) != 1:
        print("Kun 1 bokstav pls")
        continue
    if bokstav in ord:
        if bokstav in riktige_bokstaver:
            print("du har allerede gjettet herre bokstaven")
        else:
             riktige_bokstaver.append(bokstav)
             print("Riktig!")
             print (anonymiserer(ord, riktige_bokstaver))
    else:
        feil_bokstaver.append(bokstav)
        antall_liv -= 1
        print("feil, du har " + str(antall_liv) + " liv igjen.")
        print (anonymiserer(ord, riktige_bokstaver))
        

        


# si ifra om bokstaven er riktig eller feil

# hold styr på mengde liv

