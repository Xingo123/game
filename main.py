import turtle
import random

henk = turtle.Turtle()
screen = turtle
screen.bgcolor("white")
henk.pendown()
henk.speed(5)

def goed():
  for i in range(3):
      henk.color("green")
      henk.forward(20)

def fout():
  for i in range(3):
      henk.color("red")
      henk.forward(20)

print('Welkom bij dit spel. Probeer het woord te raden.')

woorden = ["lynx", "arbeidsongeschiktheidsverzekering", "secretarisvogel"]
verkeerdGeradenLetters = []
geradenLetters = []

geraden = False

aantalKeren = 0
ronden = 0

lettersList = []

def lettersFunctie(woord, letter):
  for i in range(len(woord)):
    if (woord[i] == letter):
        lettersList.append(i)

woord = woorden[random.randint(0, 2)]
print("het woord heeft " + str(len(woord)) + ' letter ')

while geraden == False:
  letter = input("geef een letter: ")

  if (woord.find(letter) != -1):
    goed()
    geradenLetters.append(letter)
    lettersFunctie(woord, letter)
    hoeveelLetters = "Letter komt voor in "
    for x in lettersList:
      hoeveelLetters += f"positie {x + 1} "
    print(f"De letter {letter} komt {woord.count(letter)} keer voor in het woord.")
    print(f"{hoeveelLetters}")

  else:
    fout()
    verkeerdGeradenLetters.append(letter)
    print(f"De letter {letter} komt NIET voor in het woord.")

  keuze = input("weet je het woord. Antwoord ja of nee: ")

  if (ronden < 4):
    if keuze == "ja":
        antwoord = input("geef het woord : ")
        if (antwoord == woord):
            print("GERADEN")
            geraden = True
        else:
          aantalKeren = aantalKeren + 1
          print(f"Let op: je hebt nog maar {3 - aantalKeren} kansen.")
    
  else:
    print(f"Game over, want je hebt al 3 x geraden.")
  
  ronden = ronden + 1