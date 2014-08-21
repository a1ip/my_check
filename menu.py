menu = {
        # 1.
        (1,)        :    "První",
        (1,1)       :    "podstart",
        # 2.
        (2,)        :       "Druha",
        (2,1)       :   "POddruha",
        (2,1,2)     :   "PodPOdDruha",
        # 3.
        (3,)         :  "3", 
        (3,3,3,3)   :  "Třetí dole"
        
        }


def show_menu(menu, *,
              level: tuple =  None,
              deep = None):
    if level:
        menu = {item: menu[item] for item in
                menu if item[:len(level)] == level}
    
    for item in sorted(menu):    
        intend = len(item)
        if deep and deep < intend:
            continue
        print(" " * intend +
              menu[item])
    



show_menu(menu, deep = 2)
show_menu(menu, level = (1,))
show_menu(menu)
