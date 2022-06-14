gem = [
42.3,
38.4,
53.8,
34.6,
46.1




]

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
