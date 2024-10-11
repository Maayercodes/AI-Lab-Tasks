# Code of A* Algorithm (without importing any library)
class Node:
    def __init__(self, position, g=0, h=0, parent=None):
        self.position = position  
        self.g = g  
        self.h = h  
        self.f = g + h 
        self.parent = parent   
    def __eq__(self, other):
        return self.position == other.position
    def __lt__(self, other):
        return self.f < other.f
def heuristic(current_node, goal_node):
    """Manhattan distance heuristic function."""
    return abs(current_node.position[0] - goal_node.position[0]) + abs(current_node.position[1] - goal_node.position[1])
def a_star(start, goal, grid):
    """A* algorithm to find the shortest path from start to goal in a grid."""
    open_list = []  
    closed_list = []  
    start_node = Node(start, g=0, h=heuristic(Node(start), Node(goal)))
    goal_node = Node(goal)
    open_list.append(start_node)
    while open_list:
        current_node = min(open_list, key=lambda node: node.f)
        open_list.remove(current_node)
        closed_list.append(current_node)
        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  
        neighbors = get_neighbors(current_node, grid)
        for neighbor_pos in neighbors:
            neighbor = Node(neighbor_pos, parent=current_node)
            if neighbor in closed_list:
                continue        
            neighbor.g = current_node.g + 1  
            neighbor.h = heuristic(neighbor, goal_node)  
            neighbor.f = neighbor.g + neighbor.h 
            if add_to_open(open_list, neighbor):
                open_list.append(neighbor)
    return None  
def get_neighbors(node, grid):
    """Get valid neighbors for a node in the grid."""
    neighbors = []
    x, y = node.position
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction in directions:
        new_x, new_y = x + direction[0], y + direction[1]
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 0:
            neighbors.append((new_x, new_y))
    return neighbors
def add_to_open(open_list, neighbor):
    """Check if a neighbor should be added to the open list."""
    for node in open_list:
        if neighbor == node and neighbor.g > node.g:
            return False
    return True
if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    start = (0, 0)  
    goal = (4, 4) 
    path = a_star(start, goal, grid)
    if path:
        print("Path found:", path)
    else:
        print("No path found")
