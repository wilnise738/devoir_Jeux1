from random import randrange

comp_nommber=randrange(0,500)
chance = 5

print("Bienvenue dans mon jeux! \nCe jeux, tu vas deviner un nombre secret. \n")
chosen_number=int(input("Entrer un nombre compris entre 0 à 500: \n"))

if chosen_number == comp_nommber:
    print("Félicitation, tu as gagné")

while chosen_number !=comp_nommber and chance !=0:
     if chosen_number > comp_nommber:
        print("Desolée, le nombre secret est inférieur au nombre que tu as entré.")
        if chance >1:
            print("Il te reste" ,chance, "chances")
        elif chance == 1:
            print("Il te reste" ,chance, "chance")
        chosen_number=int(input("Entrer donc un autre nombre. \n"))
     elif chosen_number < comp_nommber:
        print("Desolée, le nombre secret est supérieur au nombre que tu as entré.")
        if chance >1:
            print("Il te reste" ,chance, "chances")
        elif chance == 1:
            print("Il te reste" ,chance, "chance")
        chosen_number=int(input("Entrer donc un autre nombre. \n"))
     else:
        print("Felicitation, tu as gagné!")
        print("Le nombre secret est bien ",comp_nommber)
        break
     chance -= 1   

if chance ==0:
    print("desolée, Tu as épuisé de toutes tes chances.")
    print("Le nombre secret est" ,comp_nommber,"\n")

print("Merci d'avoir joué avec moi!")