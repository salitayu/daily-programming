from tkinter import N


def criticalConnections(n, connections):
    # an edge is a critical connection if and only if it is not a cycle
    # node rank - depth of node during dfs, starting node rank 0
    # only nodes on current dfs path have non special ranks
    # only nodes we started visiting but havent finished visiting have ranges 0 <= rank < n
    # if a node is not visited yet, it has a special rank of -2
    # if we fully completed the visit of a node, it has a special rank of n
    # path of length k during dfs, nodes on path have increasing ranks from 0 to k and incrementing by 1
    # next visit finds a node that has a rank of p where 0 <= p < k
    # you found a node that is on the current search path, which is a cycle
    # only the current level of search has to use theh return value of dfs, returning the minimum rank it finds
    # if dfs return something smaller than or equal to rank(u) then u knows its neighbor v help it to find a cycle
    # back to u or u's ancestor. so u knows it should discard the edge (u, v) which is a cycle.
    # after doing dfs on all nodes, all edges in cycles are discarded so the remaining edges are critical connections
    import collections
    def makeGraph(connections):
        graph = collections.defaultdic(list)
        for conn in connections:
            graph[conn[0]].append(conn[1])
            graph[conn[1]].append(conn[0])
        return graph
    graph = makeGraph(connections)
    connections = set(map(tuple, (map(sorted, connections))))
    rank = [-2] * n
    def dfs(node, depth):
        if rank[node] >= 0:
            return rank[node]
        rank[node] = depth
        min_back_depth = n
        for neighbor in graph[node]:
            if rank[neighbor] == depth - 1:
                continue
            back_depth = dfs(neighbor, depth + 1)
            if back_depth <= depth:
                connections.discard(tuple(sorted((node, neighbor))))
            min_back_depth = min(min_back_depth, back_depth)
        rank[node] = n
        return min_back_depth
    dfs(0, 0)
    return list(connections)