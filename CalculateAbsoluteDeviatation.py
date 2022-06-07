gem = [84.6, 92.3, 96.2, 88.5, 80.8]

totaal = 0
for g in gem:
    totaal += g
print(len(gem))
gemiddelde = totaal/len(gem)
print(f"gem: {gemiddelde}")

total_deviation = 0
for g in gem:
    
    total_deviation += abs(gemiddelde - g)
deviation = total_deviation/len(gem)
print(f"deviation: {deviation}")
