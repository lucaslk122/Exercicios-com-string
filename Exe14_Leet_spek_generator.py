leet = {
    'A': '\o/',
    'B': 'zz',
    'C': '<>',
    'D': '[)',
    'E': '&!',
    'F': 'ph',
    'G': '6',
    'H': '#',
    'I': '1',
    'J': 'j',
    'K': '|<',
    'L': '|_',
    'M': '|\/|',
    'N': '/\/',
    'O': '0',
    'P': '|*',
    'Q': '9',
    'R': 'l2',
    'S': '5',
    'T': '7',
    'U': 'v',
    'V': 'XV',
    'W': 'vv',
    'X': '><',
    'Y': '`/',
    'Z': '2'}

texto = input('Texto: ')
for i in texto.upper():
    if i in leet:
        print(leet[i], end='')