from turtle import Turtle as Zelva

BARVY =   {
          1 : "red",
          2 : "blue",
          3 : "white"
          }
POZICE = {
          1 : (0,0),    #Levý spodní
          2 : (120,0),   #Pravý spodní
          3 : (120,60),   #Pravý horní
          4 : (0, 60)     #Levý hodní
          }
          

if __name__ == "__main__":
    # Nakreslíme červenou vlajku
    vlajky = {}
    vlajka = (1,2,3,4,1)
    vlajky[vlajka] = "Bílá země"
    z = Zelva()
    z.speed(1)
    barva = vlajka[-1]
    z.fillcolor(BARVY[barva]) #Poslední prvek je číslo barvy
    z.color = "black"
    
    z.hideturtle()
    z.begin_fill()
    for bod in vlajka[:-1]:
        z.setpos(*POZICE[bod])
    z.setpos(0,0)
    z.end_fill()
