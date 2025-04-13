import Bibli

Hexas = {
    "num1" : 'A',
    "num2" : 'B',
    "num3" : 'C',
    "num4" : 'D'
}

H = Bibli.hexa(Hexas)



print(H)
print(Bibli.in_hexa(H.num1 + H.num3))
print(Bibli.in_hexa(15))