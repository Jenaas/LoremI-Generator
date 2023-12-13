import random

def zpet(seznam):
    o = len(seznam)
    cisla = random.randint(1 , o) - 1
    vychod = seznam[cisla]
    return vychod


casove_predpony = ["Včera večer", "Dnes ráno", "Před chvílí", "Za chvíli", "Během dne", "V minulém týdnu","V příštím měsíci", "Včera",
                    "Dnes", "Zítra", "Předevčírem", "Za dva dny", "Před třemi hodinami", "Za pět minut", "Bylo nebylo"]
uvodni_predstaveni = ["byl jeden", "slanil se z okna", "vyšel ze školy", "usedl k počítači", "probudil se včas", "začal den s úsměvem","byl jednou za tmy"]
vlastnost = ["hloupý", "bystrý", "široký", "úspěšný", "empatický", "ambiciózní", "kreativní", "vstřícný", "stručný", "loajální",
              "neústupný", "veselý", "vzácný", "tolerantní", "otevřený", "ohnivý","mazaný"]
nahodne_postavy = ["čert","Ježíš","Václav", "zlobr","hasič","tulák","Mikuláš","panda","Žeryk","šmoula","Jaroslav","Harry","trpaslík","papoušek","bubák"]
spojky = [" a", ", ale", ", protože", ", když"]
jak = ["škodolibě", "naštvaně", "nadšeně", "rychle","silně", "slabě","hlasitě"]
slovesa = ["dorazil" , "nedorazil", "otevřel","neotevřel","byl","nebyl","postával","plakal","utíkal","psal","díval"]

finalni_vyber =[casove_predpony, uvodni_predstaveni, vlastnost, nahodne_postavy, spojky, jak, slovesa]


text = " "
for i in finalni_vyber:
    text = text + zpet(i) + " "
    
print(f"{text}.")    