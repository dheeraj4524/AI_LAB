class State:
    def __init__(self, m, c, b):
        self.m = m
        self.c = c
        self.b = b
    def is_valid(self):
        if self.m < 0 or self.c < 0:
            return False
        if self.m < self.c and self.m > 0:
            return False
        if 3 - self.m < 3 - self.c and 3 - self.m > 0:
            return False
        return True
    def is_goal(self):
        return self.m == 0 and self.c == 0 and self.b == 1
    def __eq__(self, other):
        return self.m == other.m and self.c == other.c and self.b == other.b
    def __hash__(self):
        return hash((self.m, self.c, self.b))
def successors(state):
    successor_states = []
    moves = [(2, 0), (1, 0), (1, 1), (0, 1), (0, 2)]  
    for move in moves:
        if state.b == 0:  # boat on the left side
            new_state = State(state.m - move[0], state.c - move[1], 1)
        else:  # boat on the right side
            new_state = State(state.m + move[0], state.c + move[1], 0)
        if new_state.is_valid():
            successor_states.append(new_state)
    return successor_states
def find(initial_state):
    visited = set()
    queue = [[initial_state]]
    if initial_state.is_goal():
        return [initial_state]
    while queue:
        path = queue.pop(0)
        current_state = path[-1]
        for successor in successors(current_state):
            if successor not in visited:
                new_path = list(path)
                new_path.append(successor)
                queue.append(new_path)
                visited.add(successor)
                if successor.is_goal():
                    return new_path
    return None
def print_solution(solution):
    if solution is None:
        print("No solution found.")
        return
    stepcount=0
    print("Missionaries and Cannibals Solution:")
    m_remaining = solution[0].m  # Initial number of missionaries on the left side
    c_remaining = solution[0].c  # Initial number of cannibals on the left side  
    for idx, state in enumerate(solution):
        boat = "Left" if state.b == 0 else "Right"     
        if idx > 0:
            moved_m = abs(m_remaining - state.m)  # Calculate the moved missionaries
            moved_c = abs(c_remaining - state.c)  # Calculate the moved cannibals
        else:
            moved_m, moved_c = 0, 0  
        m_remaining = state.m  # Update the remaining missionaries count
        c_remaining = state.c  # Update the remaining cannibals count
        print("step : ",stepcount)
        if moved_m > 0 or moved_c > 0:
            print(f"{moved_m}M {moved_c}C moved from Left to Right" if state.b == 1 else f"{moved_m}M {moved_c}C moved from Right to Left")   
        print(f"{state.m}M {state.c}C are on Left Side")
        print(f"{m - state.m}M {c - state.c}C are on Right Side")
        print(f"Boat: {boat} side")
        print()
        stepcount+=1
if __name__ == "__main__":
    m = int(input("Enter no.of missionaries: "))
    c = int(input("Enter no.of cannibals: "))
    if m!=c:
        print("Missionaries and Cannibals are not in equal number not possible")
    else:
        initial_state = State(m, c, 0)
        sol = find(initial_state)
        print_solution(sol)
        print("Goal State is reached")