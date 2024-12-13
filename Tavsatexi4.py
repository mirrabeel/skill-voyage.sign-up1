def first_algorithm(floors, break_floor):
    k = int((2*floors)**0.5)        #ადეკვატურია k-ს პოვნა (შესაძლებელია გაუმჯობესება)
    drops = 0
    current_floor = 0 

# პირველი ბურთის გადმოგდებები
    for i in range(1, k+1):
        next_floor = current_floor + floors // K
        drops += 1 
        if next_floor >= break_floor: 
        # თუ ბურთი გატყდა, მეორეთი ძებნა
            for floor in range(current_floor +1,next_floor +1):
                drops += 1
                if floor == break_floor:
                    return floor, drops
    current_floor = next_floor

#თუ ბურთი არ გატყდა, ყველაზე მაღალი სართულია
    return floors, drops

def second_algorithm(floors,break_floor):
    k=1
    drops = 0
    current_sum = 0
    
    # k- ს გამოთვლა, n<=k(k+1)/2 შესასრულებლად
    while current_sum <  floors:
        current_sum += k
        k += 1 
    k -= 1

    # პირველი ბურთის გადმოგდება
    current_floor = 0 
    for i in range (k, 0, -1):
        next_floor = current_floor + i
        drops +=1
        if next_floor >= break_floor:
            # თუ ბურთი გატყდა, მეორეთი ცდა
            for floor in range(current_floor + 1, next_floor + 1):
                drops += 1
                if floor == break_floor:
                    return floor, drops
        current_floor = next_floor
    # თუ ბურთი არ გატყდა, ყველაზე მაღალი სართულია
    return floors, drops

def test_algorithms():
    floors = 100        #ცათამბჯენის სართულების რაოდენობა
    break_floor = 57    # სართული, საიდანაც ბურთი ტყდება

    # პირველი ალგორითმის ტესტი
    result1, drops1 = first_algorithm(floors, break_floor)        
    print(f"First Algirithm: Breaks at floor {result1} with {drops1} drops.")

    # მეორე ალგორითმის ტესტი
    result2, drops2 = second_algorithm(floors, break_floor)
    print(f"Second_Algorithm: Breaks at floor  {result2} with {drops2} drops.")

    #შედარება
    if drops1 > drops2:
        print("მეორე ალგორითმი არის უფრო მეტად ეფექტური")
    elif drops1 < drops2:
        print(" პირველი ალგორითმი არის უფრო მეტად ეფექტური")
    else:
        print("ორივე ალგორითმი არის თანაბრად ეფექტური")

#ტესტირების გაშვება
test_algorithms()

    

    