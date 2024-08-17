import random

def dice_simulator():
    # Wir rollen zwei Würfel und geben die Ergebnisse aus.
    wurfel_1 = random.randint(1, 6)


    print(f"Du hast gewürfelt: {wurfel_1}")

# Wir starten den Simulator und rollen die Würfel x-mal
x = int(input("Wie oft soll der Dice Simulator gestartet werden? "))
for i in range(x):
    dice_simulator()

