from collections import deque
def fight(robot_1, robot_2, tactics):
    r1_tactics = deque(robot_1["tactics"])
    r2_tactics = deque(robot_2["tactics"])
    while robot_1["health"] > 0 and robot_2["health"] > 0:
        if not r1_tactics and not r2_tactics:
            break
        if robot_1["speed"] >= robot_2["speed"]:
            if r1_tactics:
                robot_2["health"] -= tactics[r1_tactics.popleft()]
            if robot_2["health"] <= 0:
                break
            if r2_tactics:
                robot_1["health"] -= tactics[r2_tactics.popleft()]
        else:
            if r2_tactics:
                robot_1["health"] -= tactics[r2_tactics.popleft()]
            if robot_1["health"] <= 0:
                break
            if r1_tactics:
                robot_2["health"] -= tactics[r1_tactics.popleft()]
        
    
    if robot_1["health"] == robot_2["health"]:
        return "The fight was a draw."
    elif robot_1["health"] > robot_2["health"]:
        return f"{robot_1['name']} has won the fight."
    else:
        return f"{robot_2['name']} has won the fight."