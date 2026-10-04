import time

def type_text(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.009)
    print()

def get_choice():
    while True:
        answer = input("\n> ").strip()

        if answer in ["1", "2", "3", "4"]:
            return answer

        print("Choose 1, 2, 3, or 4.")

print("=" * 65)
print("                    CARL VAN LOON")
print("=" * 65)
print()

type_text("Eddie enters a private conference room.")
type_text("Everything about the building says power.")
type_text("Glass walls. Expensive suits. Silence.")
print()

type_text("At the end of the table sits Carl Van Loon.")
print()

type_text('"Sit down, Eddie."')
type_text('"Thank you."')
type_text('"I have been hearing some interesting things about you."')
print()

type_text("Eddie knows exactly what Carl wants.")
type_text("A solution to a billion-dollar problem.")
pause = input("\nPress ENTER to continue...")

print()
type_text("Carl slides a folder across the table.")
type_text("Inside are financial reports, market data, and company records.")
print()

type_text('"You have one hour."')
type_text('"To do what?"')
type_text('"Tell me what everyone else is missing."')
print()

print("1. Analyze the financial data")
print("2. Challenge Carl directly")
print("3. Pretend you already know the answer")
print("4. Ask for more information")

choice = get_choice()

print()

if choice == "1":
    type_text("Eddie opens the folder.")
    type_text("His eyes move across the numbers.")
    time.sleep(1)
    type_text("Revenue.")
    type_text("Debt.")
    type_text("Acquisitions.")
    type_text("Market pressure.")
    type_text("Everything connects.")

    print()
    type_text("Eddie finds a hidden weakness.")
    type_text("The company is worth more than the market believes.")

    result = "analysis"

elif choice == "2":
    type_text("Eddie looks directly at Carl.")
    type_text('"Your strategy is wrong."')
    print()
    type_text("The room becomes completely silent.")
    type_text("Carl slowly smiles.")
    type_text('"Interesting."')

    result = "confidence"

elif choice == "3":
    type_text("Eddie leans back.")
    type_text('"I already know what the problem is."')
    type_text("Carl raises an eyebrow.")
    type_text('"Then explain it."')

    result = "bluff"

else:
    type_text('"I need more information."')
    type_text("Carl studies him.")
    type_text('"Good answer."')
    type_text('"Most people pretend they understand."')

    result = "careful"

print()
pause = input("Press ENTER to continue...")

print()
print("=" * 65)
print("                       THE ANSWER")
print("=" * 65)
print()

if result == "analysis":
    type_text("Eddie explains the entire situation.")
    type_text("His argument is precise.")
    type_text("Every number has a purpose.")
    type_text("Carl listens without interrupting.")
    print()
    type_text('"You understand the game."')
    type_text('"I understand the numbers."')
    type_text('"No. You understand the game."')
    print()
    print("RESULT: CARL IS IMPRESSED")

elif result == "confidence":
    type_text("Eddie explains why Carl's strategy is outdated.")
    type_text("He predicts what the market will do next.")
    print()
    type_text("Carl says nothing.")
    type_text("Then he starts laughing.")
    print()
    type_text('"I like you, Eddie."')
    print()
    print("RESULT: RESPECT")

elif result == "bluff":
    type_text("Eddie gives Carl an answer.")
    type_text("It sounds convincing.")
    print()
    type_text("Carl asks one question.")
    type_text("Eddie knows the answer.")
    print()
    type_text("The bluff works.")
    print()
    print("RESULT: DANGEROUS SUCCESS")

else:
    type_text("Eddie asks questions.")
    type_text("He listens.")
    type_text("He waits.")
    print()
    type_text("Carl finally gives him the information.")
    type_text("Now Eddie sees the complete picture.")
    print()
    print("RESULT: PATIENCE")

print()
type_text("The meeting ends.")
type_text("Eddie walks out of the building.")
type_text("His life has just changed again.")