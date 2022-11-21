BASE = 4 #nb personne
vacherin = 400.0 #g pour BASE
gruyere = 400.0 #g pour BASE
vin_blanc = 3 #dL pour BASE
ail = 2 #gousse pour BASE
pain = 400 #g pour BASE
arvine = 4 #bouteilles pour BASE

conv = int(input("Entrez le nombre de personne(s) conviées à la fondue moitié-moitié (dans les règles de l'art) : "))

ratio = conv / BASE

vacherin = vacherin * ratio
gruyere = gruyere * ratio
vin_blanc = vin_blanc * ratio
ail = ail * ratio
pain = pain * ratio
arvine = arvine * ratio

print(f"Pour faire une fondue fribourgeoise pour 3 personnes, il vous faut :\n"
      f"- {vacherin} gr de Vacherin Fribourgeois\n"
      f"- {gruyere} gr de Gruyère\n"
      f"- {vin_blanc} dl de vin blanc sec\n"
      f"- {ail} gousse(s) d'ail\n"
      f"- {pain} gr de pain\n"
      f"- {arvine} bouteille(s) de Petite Arvine, comme on dit «Beau pays, mais SEC !» ")