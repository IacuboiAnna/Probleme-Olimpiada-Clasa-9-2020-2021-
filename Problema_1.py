x=int(input("Dati numarul de pasari:"))
if (x%2==0):
    print("La ferma sunt:", x//2, "gaini", (x//2)//4, "rate", x-(x//2)-((x//2)//4), "gaste")
if (x%2==1):
    print("La ferma sunt:", (x-1)//2, "gaini", ((x-1)//2)//4, "rate", x-((x-1)//2)-(((x-1)//2)//4), "gaste")