# 1-2-amalyot

# davlatlar = ('Yaponiya,' 'Xitoy,' 'Korea,' 'Singapur')
# print("royxat uzunligi:", len(davlatlar), "ga teng")

# 3-amaliyot

# davlatlar = ['yaponiya', 'Xitoy','Korea', 'Singapur', 'AQSH']
# print(sorted(davlatlar))

# 4-5-amaliyot
# davlatlar = ['yaponiya', 'Xitoy','Korea', 'Singapur', 'AQSH']
# davlatlar.reverse()
# print(sorted(davlatlar))

# 8-9-amaliyot
# juft_sonlar = list(range(120, 1200, 2))
# yigindi = sum(juft_sonlar )
# print(yigindi)

# 10-11-amaliyot

# sonlar = [2, 6, 8 ,5 ,3, 9]
# print(len(sonlar))

# eng_kichik = min(sonlar)
# eng_katta = max(sonlar)

# ayirma = eng_katta - eng_kichik
# print(ayirma)

# sonlar = [2, 6, 8 ,5 ,3, 9, 10]

# eng_boshidagi_elament = sonlar[0]
# eng_oxiridagi_elament = sonlar[-1]
# ortadagi_elament = len(sonlar) / 2

# print(eng_boshidagi_elament)
# print(eng_oxiridagi_elament)
# print(ortadagi_elament)

# 14-151-16-17-18-amaliyotlar 
taomlar = ["Osh", "Mastava", "Shashlik", "Choponcha", "Jiz"]
print(taomlar)
taomlar.append("Blinchik")
taomlar.append("Somsa")
taomlar.remove("Mastava")
taomlar.remove("Jiz")
taomlar.remove( "Choponcha" )
nonushta = taomlar[:]
nonushta = tuple(nonushta)
nonushta [0] = "qaymoq"
nonushta [0] = "non"
print(nonushta)