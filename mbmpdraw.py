from colorama import Fore, Back, init
from sys import argv
init()

extnumdict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14, 'f':15}
extcolorlist = ['reset', 'black', 'white', 'red', 'green', 'blue', 'yellow', 'cyan', 'magneta', 'lblack', 'lred', 'lgreen', 'lblue', 'lyellow', 'lcyan', 'lmagneta']
colorlist = ['reset', 'white', 'red', 'green', 'blue', 'yellow', 'cyan', 'magneta']
colorlist5 = ['reset', 'white', 'red', 'green', 'blue']
if '-fcolor' in argv:
    fcolor = argv[argv.index('-fcolor')+1]
else:
    fcolor = 'white'
if '-bcolor' in argv:
    bcolor = argv[argv.index('-bcolor')+1]
else:
    bcolor = 'white'
if '-symbol' in argv:
    symbol = argv[argv.index('-symbol')+1]
else:
    symbol = '　'
if '-bsymbol' in argv:
    bsymbol = argv[argv.index('-bsymbol')+1]
else:
    bsymbol = '　'
if '-file' in argv:
    file = argv[argv.index('-file')+1]
else:
    file = 'example.mbmp'
if '-help' in argv:
    print('mbmpdraw [-file -fcolor -bcolor]')
class color:
    def text(text, _fgc, _bgc='reset'):
        _fgc = _fgc.lower()
        _bgc = _bgc.lower()
        tx = text + Fore.RESET
        out = ''
        if _fgc == 'red':
            out = Fore.RED
        elif _fgc == 'blue':
            out = Fore.BLUE
        elif _fgc == 'green':
            out = Fore.GREEN
        elif _fgc == 'reset':
            out = Fore.RESET
        elif _fgc == 'yellow':
            out = Fore.YELLOW
        elif _fgc == 'cyan':
            out = Fore.CYAN
        elif _fgc == 'magneta':
            out = Fore.MAGENTA
        elif _fgc == 'black':
            out = Fore.BLACK
        elif _fgc == 'white':
            out = Fore.WHITE
        elif _fgc == 'lblack':
            out = Fore.LIGHTBLACK_EX
        elif _fgc == 'lred':
            out = Fore.LIGHTRED_EX
        elif _fgc == 'lblue':
            out = Fore.LIGHTBLUE_EX
        elif _fgc == 'lgreen':
            out = Fore.LIGHTGREEN_EX
        elif _fgc == 'lyellow':
            out = Fore.LIGHTYELLOW_EX
        elif _fgc == 'lcyan':
            out = Fore.LIGHTCYAN_EX
        elif _fgc == 'lmagneta':
            out = Fore.LIGHTMAGENTA_EX
        else:
            print('E')
        if _bgc == 'red':
            out = out + Back.RED + tx
        elif _bgc == 'blue':
            out = out + Back.BLUE + tx
        elif _bgc == 'green':
            out = out + Back.GREEN + tx
        elif _bgc == 'reset':
            out = out + Back.RESET + tx
        elif _bgc == 'yellow':
            out = out + Back.YELLOW + tx
        elif _bgc == 'cyan':
            out = out + Back.CYAN + tx
        elif _bgc == 'magneta':
            out = out + Back.MAGENTA + tx
        elif _bgc == 'black':
            out = out + Back.BLACK + tx
        elif _bgc == 'white':
            out = out + Back.WHITE + tx
        elif _bgc == 'lblack':
            out = out + Back.LIGHTBLACK_EX + tx
        elif _bgc == 'lred':
            out = out + Back.LIGHTRED_EX + tx
        elif _bgc == 'lblue':
            out = out + Back.LIGHTBLUE_EX + tx
        elif _bgc == 'lgreen':
            out = out + Back.LIGHTGREEN_EX + tx
        elif _bgc == 'lyellow':
            out = out + Back.LIGHTYELLOW_EX + tx
        elif _bgc == 'lcyan':
            out = out + Back.LIGHTCYAN_EX + tx
        elif _bgc == 'lmagneta':
            out = out + Back.LIGHTMAGENTA_EX + tx
        else:
            print('E')
        return out + Fore.RESET + Back.RESET
with open(file, 'r') as f:
    f = f.read().split('\n')
if file.split('.')[-1] == '8cbmp':
    colored=8
elif file.split('.')[-1] == 'cbmp':
    colored=8
elif file.split('.')[-1] == 'xbmp':
    colored=16
elif file.split('.')[-1] == '5cbmp':
    colored=5
else:
    colored=0
if colored==8:
    for i in f:
        ln = ''
        for j in i:
            ln = ln + color.text(symbol, fcolor, colorlist[int(j)])
        print(ln)
elif colored==16:
    for i in f:
        ln = ''
        for j in i:
            ln = ln + color.text(symbol, fcolor, extcolorlist[extnumdict[j.lower()]])
        print(ln)
elif colored==5:
    for i in f:
        ln = ''
        for j in i:
            ln = ln + color.text(symbol, fcolor, colorlist5[int(j)])
        print(ln)
else:
    for i in f:
        ln = ''
        for j in i:
            if int(j) == 1:
                ln = ln + color.text(symbol, fcolor, bcolor)
            else:
                ln = ln + bsymbol
        print(ln)