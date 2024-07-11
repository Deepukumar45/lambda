#(1)
Slicing=lambda v:v[2:]
print(Slicing("deepu"))

#(2)
var = lambda v:v.rstrip()
print(var("  hello deepu "))

#(3)
IND = lambda a:a.lstrip()
print(IND("  hello deepu "))

#(4)
IND = lambda a:a.strip('#')
print(IND("###Nepal###"))

#(5)
IND = lambda a:a.strip('cmow.')
print(IND("www.example.com"))

#(6)
IND = lambda a:a.lstrip('star ')
print(IND("Deepu!"))

#(7)
IND = lambda a:a.removeprefix('star ')
print(IND("Deepu!"))

IND = lambda a:a.removesuffix('Python')
print(IND("HelloHtml"))

#(8)
IND = lambda a:a.replace('\n','')
print(IND(' \n \t hello\n'))

#(9)
IND = lambda a:a.upper()
print(IND("i love nepal!"))

#(10)
IND = lambda a:a.lower()
print(IND("i love nepal!"))

#(11)
Prime = lambda a:a.capitalize()
print(Prime("i love nepal!"))

#(12)
Prime = lambda a:a.islower()
print(Prime("I LOVE NEPAL!"))

Prime = lambda a:a.islower()
print(Prime("i love nepal!"))

#(13)
Prime = lambda a:a.isupper()
print(Prime("I LOVE NEPAL!"))

Prime = lambda a:a.isupper()
print(Prime("i love nepal!"))

#(14)
Prime = lambda a:a.count('o')
print(Prime("i love Amritsar"))

#(15)
Prime = lambda a:a.find('M')
print(Prime("Kathmandu"))

Anime = lambda a:a [1:]
print(Anime("Kathmandu"))

#(16)
Anime = lambda a:a.rfind('A')
print(Anime("Kathmandu"))

#(17)
Anime = lambda a:a.startswith('KAT')
print(Anime("Kathmandu"))

#(18)
Anime = lambda a:a.endswith('NDU')
print(Anime("Kathmandu"))

#(19)
Anime = lambda s:s.partition('cricket')
print(Anime("I love watching cricket"))

Anime = lambda s:s.partition('love')
print(Anime("I love watching cricket"))

#(20) center
Anime = lambda d:d.center(30, '-')
print(Anime("food is tasty!"))

#(21) ljust
Anime = lambda d:d.ljust(30, '-')
print(Anime("food is tasty!"))

#(22) rjust
Anime = lambda d:d.rjust(30, '-')
print(Anime("food is tasty!"))

#(23) swapcase()
Roniyar = lambda h:h.swapcase()
print(Roniyar("HELLO kathmandu"))

#(24)) zfill()
Roniyar = lambda h:h.zfill(8)
print(Roniyar("600"))

Roniyar = lambda h:h.zfill(6)
print(Roniyar("-900"))

#(25) f-Strings 
let = 'place'
city = 'kathmandu'
Roniyar = lambda h:h.fstring()
print(f'{city} is the famous {let} in India!')

#(26)
Roniyar = lambda s:s.split()
print(Roniyar("Kathmandu is in Nepal"))

#(27)rsplit()
Roniyar = lambda h:h.rsplit()
print(Roniyar("Kathmandu is in Nepal"))

#(28) 
Roni = lambda s:s.isalpha()
print(Roni("worst"))

#(29)
Roni = lambda s:s.isnumeric()
print(Roni("8084"))

#(30)
hey = lambda s:s.isalnum()
print(hey("best7415"))