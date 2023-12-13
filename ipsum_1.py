import random

obsah_slova = ["Neytiri","Eywa","Hometree","Toruk","Uniltìrantokx","Tsaheylu","Kxanì","Omatikaya","Skxawng"
               ,"Tsahaylu","Ikran","Mokri","Pxey","Vawmataw","Kelutral","Txìm","Talioang","Fpeio","Utral","Atokirina'"
               ,"Tìng","Tìkangkem","Hallelujah","Kìyevame","Kunsip","Tstunwi","Nantang","Aytirea","Aean","Tsulfätu"
               ,"Zongsteng","Kìyevit","Nì'ul","Swotyu","Ayoe","Tsamsiyu","Pxare","Awnga","Oel ngati kameie","Txon'a'it"]

x = 1

pocet_radku = int(input("Zadejte prosím kolik požadujete řádků: "))
pocet_slov_ve_vete = int(input("Zadejte prosím kolik může věta obsahovat slov: "))

while pocet_radku >= x:
    mnozstvi_slov = random.randint(1, min(pocet_slov_ve_vete, len(obsah_slova)))
    random_slova = random.sample(obsah_slova, mnozstvi_slov)
    veta = " ".join(random_slova)
    upravena_veta = veta.capitalize()
    print(f"{upravena_veta}.")
    x +=1