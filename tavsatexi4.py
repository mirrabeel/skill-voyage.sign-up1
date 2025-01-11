def algorithm_1(floors, breaking_point):
    k = int(floors ** 0.5)
    first_ball_throws = second_ball_throws = 0
    for i in range(k, floors + 1, k):
        first_ball_throws += 1
        if i >= breaking_point:
            break
    for j in range(i - k + 1, i):
        second_ball_throws += 1
        if j == breaking_point:
            break
    total_throws = first_ball_throws + second_ball_throws
    return breaking_point, total_throws
 
def algorithm_2(floors, breaking_point):
    k = 1
    while (k * (k + 1)) // 2 < floors:
        k += 1
    first_ball_throws = second_ball_throws = 0
    current_floor = 0
    for i in range(k, 0, -1):
        current_floor += i
        first_ball_throws += 1
        if current_floor >= breaking_point:
            break
    for j in range(current_floor - i + 1, current_floor):
        second_ball_throws += 1
        if j == breaking_point:
            break
    total_throws = first_ball_throws + second_ball_throws
    return breaking_point, total_throws
 
floors = 100
breaking_point = 78
result_1 = algorithm_1(floors, breaking_point)
print("Algorithm #1:", result_1)
result_2 = algorithm_2(floors, breaking_point)
print("Algorithm #2:", result_2)