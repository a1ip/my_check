def checkio(number):
    zero = int(False)
    one = int(True)
    two = one + one
    three = one + two
    four = two + two
    five = four + one
    six = four + two
    seven = six + one
    eight = four + four
    

    def quick(check):
        if check in (two,
                     three,
                     five,
                     seven): return True
        #fast checking of last number
        checking = list(str(number)).pop()
        if checking in (zero,
                        two,
                        four,
                        five,
                        six,
                        eight):
            return False
        count = zero
        check_three = sum([int(i) for i in str(check)])
        #Is d*vided by three?
        while count <= check_three:
            count += three
            if count == check_three:
                return False
        return True

    if not quick(number):
        return False
    #to shorten iteration I calculate square root
    #it is not necessary, just for show :)
    #this is the slowest part :)
    half = float(str(zero) +
                 "." + str(five))
    root = int(number ** half)
    count = five
    while count <= (root + one):
        count += two #starting by seven, skipping even numbers
        if quick(count): continue #skipping already checked numbers
        counter = count
        while counter <= number:
            counter += count
            if counter == number:
                return False       
    return True
        


if __name__ == "__main__":
    print(checkio(110))
    
