import argparse
import random
import string


parser = argparse.ArgumentParser(description = 'Password generator')


parser.add_argument('-l', '--length', type=int, default=12, help="Password length (deflaut: 12)")
parser.add_argument('-d', '--digits', action='store_true', help="Include digits") #action='store_true' -> si l'utilisateur indique l'option alors le script va prendre en compte les chiffres dans le mdp
parser.add_argument('-s', '--symbols', action='store_true', help="Include symbols")
parser.add_argument('-u', '--uppercase', action='store_true', help="Include uppercases")


args = parser.parse_args() #Python va lire la ligne de commande quand tu exécutes le script et va récupérer ce que l'utilisateur a passé et le stocker dans args.


mdp = string.ascii_lowercase


if args.uppercase:
    mdp += string.ascii_uppercase


if args.symbols:
    mdp += string.punctuation


if args.digits:
    mdp += string.digits


if not mdp:
    print("ERROR: No character set selected !")
    exit()


motDePasse = ""


for i in range(args.length):
    motDePasse += random.choice(mdp)


print("Your password:", motDePasse)