def check_connection(edges, first, last):
    path = {first}
    check = 0
    # All points who can be acceseed from "first"
    # are put in path set.
    # At the end end "last" is checked if is in path set.
    while(len(path) > check):
        check = len(path)
        # this part can be easily optimized to avoid 
        # iterating through edges already accepted in path set.
        # I skipped this to keep my solution 
        # clear and easy to understand
        for edge in edges: 
            one, two = edge.split("-")
            if one in path or two in path:
                path.add(one)
                path.add(two)
    else:
        return last in path
        






assert check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "scout2", "scout3") == True
assert check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "dr101", "sscout") == False
