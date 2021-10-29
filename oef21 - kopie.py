gebruikersnaam = input("wat is je gebruikersnaam") 
paswoord = input("wat is je paswoord") 

bestand = open("olifant.txt", "wt")
bestand.write(f"welkom {gebruikersnaam} ")
bestand.write(f"dit is je paswoord {paswoord} ")
bestand.close()