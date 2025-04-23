card_ef = 1.3
quality = 5
for i in range(10):
    card_ef = card_ef + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    print(card_ef)