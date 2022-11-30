
aug = [38,36,31,27,38,24,29,29,30,24,33,27,32,24,36,31,41,30,26,34,26,30,31,26,36,23,31,28,31,32,28]

augfile = open('aug.txt','w')
t = len(aug)

if t == 31:
    print("lehet auguszusi hőmérséklet")
    augfile.write("lehet auguszusi hőmérséklet")
else:
    print("nem lehet auguszusi hőmérséklet")
    augfile.write("lehet auguszusi hőmérséklet")
maxA = aug[0]
minA = aug[0]
for szam in aug:
    if szam > maxA:
        maxA = szam
    if szam < minA:
        minA = szam
print(f'legmagasabb hőmérséklet: {maxA}')
augfile.write(f'legmagasabb hőmérséklet: {maxA}')
print(f'legalacsonyabb hőmérséklet: {minA}')
augfile.write(f'legalacsonyabb hőmérséklet: {minA}')

osszeg = 0
for ho in aug:
    if ho > 31:
        osszeg = osszeg + 1
print(f'A hőmérséklet ennyiszer volt 31C felett {osszeg}')
augfile.write(f'A hőmérséklet ennyiszer volt 31C felett {osszeg}')

print(f'Augusztus 20-án ennyi volt a hőmérséklet {aug[20]}')
augfile.write(f'Augusztus 20-án ennyi volt a hőmérséklet {aug[20]}')

osszeg = 0
for num in aug:
    osszeg = osszeg + num
    atlag = osszeg / num
print(f'Átlag hőmérséklet {atlag:0.2f}')