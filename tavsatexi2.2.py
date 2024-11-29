def best_time_for_party(times):
    events= []

#თითოეული სტუმარი დროის ინტერვალის მიხედვით
    for start, end in times:
        events.append((start, 'start')) #სტუმრის მოსვლის დრო
        events.append((end, 'end')) #სტუმრის წასვლის დრო
    
    events.sort(key=lambda x: (x[0], x[1] == 'start'))

    curent_guests = 0
    max_guests = 0
    best_time = None 

    for event in events:
        if event[1] == 'start':
            curent_guests += 1
            if curent_guests > max_guests:
                max_guests = curent_guests
                best_time = event[0]
        else:
            curent_guests -=1
    
    return best_time

celebrity_times = [
    (6, 8),
    (7, 10),
    (9, 12),
    (11, 13),
    (5, 8),
]


best_time = best_time_for_party(celebrity_times)
print(f"best hour attend : {best_time}")
