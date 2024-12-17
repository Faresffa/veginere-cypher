import string
alphabet=string.printable
def chiffre_cesar(texte, decalage):
   
    texte_chiffre = ""
    for char in texte:
            position = alphabet.index(char)
            nouvelle_position = (position + decalage) % len(string.printable)
            texte_chiffre += alphabet[nouvelle_position]

    return texte_chiffre


def cesar_uncypher(texte,decalage):
     return chiffre_cesar(texte,-decalage)

def brut_force(texte):
    for possible_key in range(0,len(string.printable)):
        texte_dechiffre=cesar_uncypher(texte, possible_key)
        print(f"Décalage {possible_key}: {texte_dechiffre}")
        
#viginère
def chiffre_vigenere(texte,cle):
    texte_chiffre = ''
    cle = cle.lower()  
    for i, char in enumerate(texte):
        decalage = string.ascii_lowercase.index(cle[i % len(cle)])  # Décalage basé sur la clé
        texte_chiffre += chiffre_cesar(char, decalage) 
    
    return texte_chiffre
        
    
    
    
    #texte_chiffre=chiffre_cesar(texte,cle)
    
#déchiffrement du vigenére 
def dechiffre_vigenere(texte,cle):
    texte_chiffre = ''
    cle = cle.lower()  
    for i, char in enumerate(texte):
        decalage = -(string.ascii_lowercase.index(cle[i % len(cle)])) 
        texte_chiffre += chiffre_cesar(char, decalage) 
    return texte_chiffre



def veginere_cypher(texte, cle, reverse=False):
    texte_chiffre = ""
    cle = cle.lower() 
    for i, char in enumerate(texte):
        decalage = string.ascii_lowercase.index(cle[i % len(cle)])  # Décalage basé sur la clé
        if  reverse:
            texte_chiffre += chiffre_cesar(char, decalage) 
        else:
            texte_chiffre += chiffre_cesar(char, decalage) 
    return texte_chiffre
    
    
        
    
txt="chill"

#chiffrement césar 
a=3
txtc=chiffre_cesar(txt,a)
print(txtc)

#dechiffrement césar 
b=-3
txtd=chiffre_cesar(txtc,b)
print(txtd)

#brute force 
txtb=brut_force(txtc)

#vigenére
cle="abc"
txtv=chiffre_vigenere(txt,cle)
print(txtv)
#dechiffremment veginere
txtdv=dechiffre_vigenere(txtv,cle)
print(txtdv)

#e

txtff=veginere_cypher(txt,cle)
print(txtff)
txtk=veginere_cypher(txtff,cle,True)
print(txtk)
