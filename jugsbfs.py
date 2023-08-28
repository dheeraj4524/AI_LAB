def bfsFindGoal(goal):
    visited = []
    queue = []
    queue.append(([0, 0], []))

    while queue:
        state, operations = queue.pop(0)
        x1, y1 = state

        ops = [
            [x, y1],
            [x1, y],
            [0, y1],
            [x1, 0],
            [0, x1 + y1] if y-(x1+y1) >= 0 else [x1 + y1 - y, y],
            [x1 + y1, 0] if x-(x1+y1) >= 0 else [x, x1 + y1 - x]
        ]

        for op in ops:
            if op == goal:
                return operations + [op]

            if op not in visited:
                visited.append(op)
                queue.append((op, operations + [op]))

    return None


if __name__ == "__main__":
    x, y = map(int, input("Enter the capacities: ").split())
    goal = list(map(int, input("Enter the goal capacities: ").split()))

    operations = bfsFindGoal(goal)

    if operations is None:
        print("Not possible!")
    else:
        print("The sequence of operations is:", operations)
