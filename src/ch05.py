"""Ch05 Travesal"""
from collections import defaultdict


def walk(G, s, S=set()):
    """Graph travesal, start from node s
    S represent a set of node that to avoid during travesal
    """
    P, Q = dict(), set() # P: predecessor to remember the path; Q: a list of nodes to visit.
    P[s] = None # node s is the starting node, thus it has no predecessor
    Q.add(s) # start from s
    while Q:
        u = Q.pop()
        for v in G[u].difference(P, S): # v is is neighbor of u, and v is not in P and S
            Q.add(v)
            P[v] = u
    return P

def components(G):
    """find all connected components in a graph
    bigO is O(m + n) : n nodes and m edges
    """
    components = [] # list to hold connected components (dict) found
    seen = set() # a set to record what node has been visited
    for u in G:
        if u in seen:
            continue
        cc = walk(G, u) # get cc from starting node u
        seen.update(cc) # add all keys in cc to seen.
        components.append(cc)
    return components

def rec_dfs(G, s, S=None):
    """recursive depth_first_search"""
    if S is None:
        S = set()
    S.add(s)
    for u in G[s]:
        if u in S:
            continue
        rec_dfs(G, u, S)

def iter_dfs(G, s):
    """interative depth_first_search"""
    seen, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in seen:
            continue
        seen.add(u)
        Q.extend(G[u]) # add all neighbors of u to the Q
        yield u

def traverse(G, s, qtype=set):
    """General graph traverse"""
    seen, Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop(0)
        if u in seen:
            continue
        seen.add(u) # mark u to be seen
        for v in G[u]:
            Q.add(v) # add all neighbors to the to-do-list
        yield u

class stack1(list):
    """stack based on list
    with add method
    """
    add = list.append

def dfs_with_timestamp(G, s, discovery_time, finish_time, seen=None, stamp=0):
    """depth first search with timestamp"""
    if seen is None:
        seen = set()
    discovery_time[s] = stamp
    stamp += 1
    seen.add(s)
    for u in G[s]:
        if u in seen:
            continue
        stamp = dfs_with_timestamp(G, u, discovery_time, finish_time, seen, stamp)
    finish_time[s] = stamp
    stamp += 1
    return stamp

def dfs_topsort(G):
    """topological sorting based on dfs with timestamp"""
    seen, result = set(), []
    def recurse_dfs(u):
        if u in seen:
            return
        seen.add(u)
        for v in G[u]:
            recurse_dfs(v)
        result.append(u) # done wiht all of u's descendents.
    for u in G:
        recurse_dfs(u)
    result.reverse()
    return result

def iter_deepening_dfs(G, s):
    """depth controled dfs, mimic breath_first_traversal
    worse case is quadratic, most of the cases will be close to linear time
    """
    yielded = set() # record items have been yielded.
    def recurse(G, s, depth, seen=None):
        if s not in yielded:
            yield s
            yielded.add(s)
        if depth == 0:
            return
        if seen is None:
            seen = set()
        seen.add(s)
        for u in G[s]: # deal with all neighbors of s
            if u in seen:
                continue
            for v in recurse(G, u, depth - 1, seen):
                yield v
    n = len(G)
    for depth in range(n): # try depth from 0 to n - 1
        if len(yielded) == n:
            break
        for u in recurse(G, s, depth):
            yield u

def bfs(G, s):
    """Breath_first_search
    time complexity: linear O(n)
    """
    P, Q = {s: None}, deque([s]) # P is for path to retrieve the path
    # Q is the queue for FIFO to-do-list
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P:
                continue
            P[v] = u # u is the predecessor of v
            Q.append(v) # add v to the to-do-list
    return P

def retrieve_path(P, u):
    """retrive the path from dict P for node u"""
    path = [u]
    while P[u] is not None:
        path.append(P[u])
        u = P[u]
    return path.reverse()

def reverse_edge(G):
    """reverse all edges in G"""
    GT = {}
    for u in G:
        GT[u] = set()
    for u in G:
        for v in G[u]:
            GT[v].add(u)
    return GT

def scc(G):
    """find strongly connected components
    Kosaraju's algorithm
    step:
    1. run dfs_topsort based on timestamp to get a topological sorted list
    2. reverse all edges in the graph
    3. run a full traversal based on the sorted seq from step 1
    """
    GT = reverse_edge(G) # reverse all edges to get a new graph GT
    sccs, seen = [], set()
    for u in dfs_topsort(G): # full traversal based on the topological sorted list
        if u in seen:
            continue
        scc = walk(GT, u, seen) # get one strongly connected component
        seen.update(scc) # update the seen nodes
        sccs.append(scc)
    return sccs
