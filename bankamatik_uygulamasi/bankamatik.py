
hesapA = {
    'ad' : 'Diana Bel',
    'hesapNo': '12345',
    'bakiye': 5000,
    'ekHesap': 3000
}

hesapB = {
    'ad' : 'Kıyal Bel',
    'hesapNo': '12',
    'bakiye': 4000,
    'ekHesap': 2000
}

def paraCek(hesap, miktar):
    print(f'Merhaba {hesap["ad"]}')

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz')
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullan = input('ek hesap kullanılsın mı (e\h) ')

            if ekHesapKullan == 'e':
                ekHesapKullan= miktar-hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullan
                print('paranızı alabilirsiniz.')
            else:
                print(f'{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} bulunmamaktadır.')
        else:
            print('bakiye yetersiz')

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır")

paraCek(hesapA, 3000)
bakiyeSorgula(hesapA)
print('******************')
paraCek(hesapA, 3000)
