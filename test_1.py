# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 21:48:48 2017

@author: iibanez
"""

stringA = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp."
stringB = "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle."
stringC = " sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
stringD = "map"
from string import maketrans

intab ='abcdefghijklmnopqrstuvwxyz'
outab ='cdefghijklmnopqrstuvwxyzab'
trantab = maketrans(intab,outab)

print stringA.translate(trantab)
print stringB.translate(trantab)
print stringC.translate(trantab)
print stringD.translate(trantab)
#for letra in stringA:
#    stringA.index(letra)
#    if letra in abc:
#        indice = (abc.index(letra))-24
#        #stringA2.append(abc[indice])
#        stringA2 += abc[indice]
#    else:
#        #stringA2.append(" ")
#        stringA2 += " "
#
#print repr(stringA2)
#    
#
#for letra in stringB:
#    stringB.index(letra)
#    if letra in abc:
#        indice = (abc.index(letra))-24
#        #stringA2.append(abc[indice])
#        stringB2 += abc[indice]
#    else:
#        #stringA2.append(" ")
#        stringB2 += " "
#
#print repr(stringB2)
#
#for letra in stringC:
#    stringC.index(letra)
#    if letra in abc:
#        indice = (abc.index(letra))-24
#        #stringA2.append(abc[indice])
#        stringC2 += abc[indice]
#    else:
#        #stringA2.append(" ")
#        stringC2 += " "
#
#print repr(stringC2)
##