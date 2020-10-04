from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(Or(AKnight, AKnave),
#A can be either a knight or a knave and not both,
 Biconditional(AKnight, Not(AKnave)),
 #If a is telling the trurth the :
 Implication(AKnight, And(AKnight, AKnave))
 )


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
And(Or(AKnave,AKnight), Or(BKnight, BKnave)),
#As said by A
Implication(AKnight, And(AKnave, BKnave)),
Implication(AKnave, BKnight)

)


# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
And(Or(AKnave,AKnight), Or(BKnight, BKnave)),
Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
Implication(AKnight, Not(AKnave)),
Implication(BKnave, Not(BKnight))

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    And(Or(AKnave, AKnight), Or(BKnight, BKnave), Or(CKnave, CKnight)),
    Biconditional(BKnight,Biconditional(AKnight, AKnave)),
    Implication(AKnave, Not(AKnight)),
    Implication(BKnave, Not(BKnight)),
    Implication(CKnave, Not(CKnave)),
    Biconditional(CKnight, AKnight),
    Biconditional(BKnight, CKnave)
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
