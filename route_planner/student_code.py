def shortest_path(M, start, goal):
    """
    This function computes the shortest path from `start` to `goal` on map `M` using the A* algorithm.
    """
    
    # I use NumPy's norm to compute the ADMISSIBLE HEURISTIC cost between nodes and the goal node.
    from numpy.linalg import norm
    
    def dist(x, y):
        # This function computes the Euclidean distance between nodes `x` and `y` in graph `M`.
        return norm([M.intersections[x][0] - M.intersections[y][0], M.intersections[x][1] - M.intersections[y][1]])
    
    print("shortest path called")
    
    closed_nodes = set()  # set of nodes already visited and evaluated
    closest_parents = {}  # dictionary of parent nodes used to construct the shortest path when the algorithm is finished
    
    g = {start: 0}  # dictionary to keep track of distances from start to visited nodes
    open_nodes = {start: g[start] + dist(start, goal)}  # initialize the dictionary of open nodes with the start node
    
    # This loop continues until the dictionary `open_nodes` is empty.
    while open_nodes:
        current = min(open_nodes, key=open_nodes.get)  # open node with the minimum total cost `f`
        
        # Check to see if currently evaluated node is the goal. If so, construct the path and return it.
        if current == goal:
            path = [current]
            while current in closest_parents:
                current = closest_parents[current]
                path.append(current)
            return path[::-1]
        
        del open_nodes[current]    # remove the current node from the dictionary of open nodes, if it's not the goal
        closed_nodes.add(current)  # add the current node to the set of closed nodes
        
        # Iterate over all neighbor nodes connected to the current node in search of the next shortest extension to the path.
        for node in M.roads[current]:
            
            # If the neighbor node is in the set of closed nodes, don't consider it and continue the loop.
            if node in closed_nodes:
                continue
            
            node2current_dist = dist(node, current)  # compute distance between `current` node and its neighbor node.
            
            # If this is the first time we have encountered this neighbor node, or if the new estimate for the distance from
            # `start` to this neighbor node is less than the existing value, compute `f` and add the node to `open_nodes`.
            if (node not in g) or (g[current] + node2current_dist < g[node]):
                g[node] = g[current] + node2current_dist       # add/update shortest distance from `start` to neighbor node
                open_nodes[node] = g[node] + dist(node, goal)  # add this node to `open_nodes` or update its total cost
                closest_parents[node] = current                # add/update `current` node as closest parent of neighbor node
                
    # If the algorithm finishes unsuccessfully, return `None`.
    return None
