nilai = int(input('Masukkan nilai: '))

while nilai < 100:
    if nilai >= 90:
        print('Predikat A')
        break
    elif nilai >= 80:
        print('Predikat B')
        break
    elif nilai >= 70:
        print('Predikat C')
        break
    elif nilai >= 60:
        print('Predikat D')
        break
    elif nilai >= 50:
        print('Predikat E')
        break
    else:
        print('Maaf, anda harus mengulang mata kuliah ini')
        break