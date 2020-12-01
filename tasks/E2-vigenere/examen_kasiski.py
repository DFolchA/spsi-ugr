import re

NONLETTERS_PATTERN = re.compile('[^A-Z]')
LONG_MAXIMA = 10

def examenKasiski(texto):
    secuenciasRepetidas = encontrarSecuenciasRepetidas(texto)
    factores = {}
    for secuencia in secuenciasRepetidas:
        factores[secuencia] = []
        for espacio in secuenciasRepetidas[secuencia]:
            factores[secuencia].extend(encontrarFactores(espacio))

    factoresOrdenados = ordenarFactoresComunes(factores)

    LongitudesPosibles = []
    for factor in factoresOrdenados:
        LongitudesPosibles.append(factor[0])

    return LongitudesPosibles

def encontrarSecuenciasRepetidas(msg):
    espacioEntreSec = {}
    for longitud in range(3, 10):
        for inicio in range(len(msg) - longitud):
            secuencia = msg[inicio:inicio + longitud]

            for i in range(inicio + longitud, len(msg) - longitud):
                if msg[i:i + longitud] == secuencia:
                    if secuencia not in espacioEntreSec:
                        espacioEntreSec[secuencia] = [] # initialize blank list

                    espacioEntreSec[secuencia].append(i - inicio)
    return espacioEntreSec

def encontrarFactores(num):
    if num <= 2:
        return []

    factores = []

    for i in range(3, LONG_MAXIMA + 1): 
        if num % i == 0:
            factores.append(i)
            factores.append(int(num / i))
    if 1 in factores:
        factores.remove(1)
    if 2 in factores:
        factores.remove(2)
    return list(set(factores))

def ordenarFactoresComunes(secuenciaFactores):
    cuenta = {} 

    for secuencia in secuenciaFactores:
        listaFactores = secuenciaFactores[secuencia]
        for factor in listaFactores:
            if factor not in cuenta:
                cuenta[factor] = 0
            cuenta[factor] += 1

    factoresOrdenados = []
    for factor in cuenta:
        if factor <= LONG_MAXIMA:
            factoresOrdenados.append( (factor, cuenta[factor]) )

    factoresOrdenados.sort(key=getItemAtIndexOne, reverse=True)

    return factoresOrdenados

def getItemAtIndexOne(x):
    return x[1]

mensaje = "UECWKDVLOTTVACKTPVGEZQMDAMRNPDDUXLBUICAMRHOECBHSPQLVIWOFFEAILPNTESMLDRUURIFAEQTTPXADWIAWLACCRPBHSRZIVQWOFROGTTNNXEVIVIBPDTTGAHVIACLAYKGJIEQHGECMESNNOCTHSGGNVWTQHKBPRHMVUOYWLIAFIRIGDBOEBQLIGWARQHNLOISQKEPEIDVXXNETPAXNZGDXWWEYQCTIGONNGJVHSQGEATHSYGSDVVOAQCXLHSPQMDMETRTMDUXTEQQJMFAEEAAIMEZREGIMUECICBXRVQRSMENNWTXTNSRNBPZHMRVRDYNECGSPMEAVTENXKEQKCTTHSPCMQQHSQGTXMFPBGLWQZRBOEIZHQHGRTOBSGTATTZRNFOSMLEDWESIWDRNAPBFOFHEGIXLFVOGUZLNUSRCRAZGZRTTAYFEHKHMCQNTZLENPUCKBAYCICUBNRPCXIWEYCSIMFPRUTPLXSYCBGCCUYCQJMWIEKGTUBRHVATTLEKVACBXQHGPDZEANNTJZTDRNSDTFEVPDXKTMVNAIQMUQNOHKKOAQMTBKOFSUTUXPRTMXBXNPCLRCEAEOIAWGGVVUSGIOEWLIQFOZKSPVMEBLOHLXDVCYSMGOPJEFCXMRUIGDXNCCRPMLCEWTPZMOQQSAWLPHPTDAWEYJOGQSOAVERCTNQQEAVTUGKLJAXMRTGTIEAFWPTZYIPKESMEAFCGJILSBPLDABNFVRJUXNGQSWIUIGWAAMLDRNNPDXGNPTTGLUHUOBMXSPQNDKBDBTEECLECGRDPTYBVRDATQHKQJMKEFROCLXNFKNSCWANNAHXTRGKCJTTRRUEMQZEAEIPAWEYPAJBBLHUEHMVUNFRPVMEDWEKMHRREOGZBDBROGCGANIUYIBNZQVXTGORUUCUTNBOEIZHEFWNBIGOZGTGWXNRHERBHPHGSIWXNPQMJVBCNEIDVVOAGLPONAPWYPXKEFKOCMQTRTIDZBNQKCPLTTNOBXMGLNRRDNNNQKDPLTLNSUTAXMNPTXMGEZKAEIKAGQ"
lista = examenKasiski(mensaje)
print(lista)
