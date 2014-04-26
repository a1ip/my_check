from matrix_dict import list_to_dict


   

def checkio(data):
   
   def check(x,y, value):
      """Checking square around landfield.
      Checked is indicated by "x"
      Returns count of founded landfield."""
      count = 0
      for i in range(-1,2): 
         for j in range(-1,2):
            try:
               x1 = x+i
               y1 = y+j
               if mapa[x1, y1] == value:
                  mapa[x1, y1] = "x"
                  count += 1 + check(x1,y1,value)
            except KeyError:
               pass  # well, you might be a little out of map! So what' 
      return count

   # Converting list matrix to dictionary matrix.
   # See list_to_dict() docstring for more explanation.
   mapa = list_to_dict(data)  #minicourse of Czech language: mapa = map :)
   result = [] 
   for (x,y), value in mapa.items():
      if value not in (0, "x"):
         result.append(check(x,y,value))                    
   return sorted(result)   
       
      

ch = checkio([[0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]]) #== [2, 3, 3, 4],
print(ch)
                

    
