import random

cisloPocitace = random.randrange(3)
tahPocitace = "Ahoj"
kamen = "Kamen"
nuzky = "Nuzky"
papir = "Papir"

tahHrace = input("Zadej svuj tah ")

if tahHrace != "Nuzky" and tahHrace != "Kamen" and tahHrace != "Papir":
    print("Tak znovu")
    quit()


if cisloPocitace == 0:
    tahPocitace = kamen
elif cisloPocitace == 1:
    tahPocitace = nuzky
elif cisloPocitace == 2:
    tahPocitace = papir

print("Pocitaci si vybral ", tahPocitace)

if tahHrace == tahPocitace:
    print("Plichta")
elif tahHrace == kamen and tahPocitace == papir:
    print("Vyhral pocitac")
elif tahHrace == kamen and tahPocitace == nuzky:
    print("Vyhral si")
elif tahHrace == nuzky and tahPocitace == papir:
    print("Vyhral si")
elif tahHrace == nuzky and tahPocitace == kamen:
    print("Vyhral pocitac")
elif tahHrace == papir and tahPocitace == kamen:
    print("Vyhral si")
elif tahHrace == papir and tahPocitace == nuzky:
    print("Vyhral pocitac")
