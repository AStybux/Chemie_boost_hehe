element = [
        ['H', '   '*6, 'He'],
        ['Li', 'Be', 'B ', 'C ', 'N ', 'O ', 'F ', 'Ne'],
        ['Na', 'Mg', 'Al', 'Si', 'P ', 'S ', 'Cl', 'Ar'],
        ['K ', 'Ca', 'Sc', 'Ti', 'V ', 'Cr', 'Mn', 'Fe', 'Co', 'Ni'],
        ['Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr'],
        ['Rb', 'Sr', 'Y ', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd'],
        ['Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I ', 'Xe'],
        ['Cs', 'Ba', 'La', 'Hf', 'Ta', 'W ', 'Re', 'Os', 'Ir', 'Pt'],
        ['Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn'],
        ['Fr', 'Ra', 'Ac', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds'],
        ['Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og'],
]

element = [[' ' + x for x in '123456789']] + element

element = [[' '] + x for x in element]

print(*(' '.join(x)+'\n' for x in element)) 
