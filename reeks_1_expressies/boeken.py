prijs = 24.95
korting = .4
verzending_eerste = 3
verzending_rest = .75
aantal = 60

totaal = aantal * (prijs - (prijs * korting))
totaal += 1 * verzending_eerste
totaal += (aantal - 1) * verzending_rest

print(totaal)