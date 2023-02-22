MostUsedHero = ['Anti Mage','Juggernaut','Earth Shaker','Phantom Asassins','Ember Spirit','Puck']
print(MostUsedHero)
print(134*'=')

#Method yang ada untuk memanipulasi List
#Method untuk menambah data kedalam List
DotA2Hero = MostUsedHero
DotA2Hero.append('Pudge')
print(DotA2Hero)

DotA2Hero.extend('Rubick')
print(DotA2Hero)

DotA2Hero.insert(2,'Luna')
print(DotA2Hero)
print(134*'=')

#Method untuk menghitung jumlah anggota
jumlahLuna = DotA2Hero.count('Luna')
print(jumlahLuna)

#Method untuk meremove suatu data
DotA2Hero.remove('Luna')
print(DotA2Hero)

#Method untuk mereverse data
DotA2Hero.reverse()
print(DotA2Hero)
print(134*'=')

AllHero = DotA2Hero.copy()
AllHero.append('Luna')
print(AllHero)
print(DotA2Hero)
