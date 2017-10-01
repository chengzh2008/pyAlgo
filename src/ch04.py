"""Ch04"""
from collections import defaultdict


def cover(board, label=1, top=0, left=0, side=None):
    """cover board with a missing corner"""

    if side is None:
        side = len(board)

    # side of sub-board
    sub_side = side // 2

    offsets = (0, -1), (side - 1, 0)

    for dy_outer, dy_inner in offsets:
        for dx_outer, dx_inner in offsets:
            if not board[top + dy_outer][left + dx_outer]:
                # label the inner corner
                board[top + sub_side + dy_inner][left + sub_side + dx_inner] = label

    print_board(board)
    # next label
    label += 1
    # recursively do the label for its subboard
    if sub_side > 1:
        for dy in [0, sub_side]:
            for dx in [0, sub_side]:
                label = cover(board, label, top + dy, left + dx, sub_side)

    return label

def print_board(board):
    """pretty print 2-D array: x downward, y rightward"""
    for row in board:
        print (" %2i" * 8) % tuple(row)
    print "#" * 16

def ins_sort_rec(seq, i):
    """insertion sort: recursive"""
    if not i:
        return
    ins_sort_rec(seq, i - 1) # sort i-1 items first
    j = i
    # start from j, compare j with j -1 item, swap if not ordered
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1
    return seq

def ins_sort_iter(seq):
    """insertion sort: interative"""
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
    return seq

def sel_sort_rec(seq, i):
    """selection sort: recursive"""
    if not i:
        return seq
    max = i
    for j in range(i):
        if seq[j] > seq[max]:
            max = j
    seq[max], seq[i] = seq[i], seq[max]
    sel_sort_rec(seq, i - 1)
    return seq

def sel_sort_iter(seq):
    for i in range(len(seq) - 1, 0, -1):
        max = i
        for j in range(i):
            if seq[j] > seq[max]:
                max = j
        seq[max], seq[i] = seq[i], seq[max]
    return seq

def naive_max_permutation(M, A=None):
    """naive implementation for maximum permutation
    M = [2, 2, 0, 5, 3, 5, 7, 4]
    #c is mapped to #a
    """
    if A is None:
        A = set(range(len(M))) # set of the index
    if len(A) == 1: # base case: single element
        return A
    B = set(M[i] for i in A) # set of the pointed index
    C = A - B # set of the index that nobody is pointing to
    if C:
        A.remove(C.pop()) # remove index that nobody is pointing to
        return naive_max_permutation(M, A)
    return A

def max_permutation(M):
    n = len(M)
    A = set(range(n)) # result set: initialized to be a full set
    count = [0]*n # counter
    for i in M:
        count[i] += 1 # initialize counter
    Q = [i for i in A if count[i] == 0]
    while Q:
        k = Q.pop()
        A.remove(k)
        j = M[k] # who is k pointing to
        count[j] -= 1
        if count[j] == 0:
            Q.append(j)
    return A

def counting_sort(A, key=lambda x: x):
    B, C = [], defaultdict(list)
    for i in A:
        C[key(i)].append(i)
    for k in range(min(C), max(C) + 1):
        B.extend(C[k])
    return B

def celebrity(G):
    """ liner time to find a celebrity
    who does not know anyone but everyone else knows him/her
    """
    number = len(G)
    assert number >= 2
    cand1, cand2 = 0, 1  # cand1, cand2 as potential candidate
    for cand in range(2, number):
        if G[cand1][cand2]:
            cand1 = cand
        else:
            cand2 = cand
    if cand1 == number: # cand1 was last replaced
        cand = cand2
    else:
        cand = cand1
    for everyone in range(number):
        if everyone == cand:
            continue
        if G[cand][everyone]:
            break # cand knows everyone
        if not G[everyone][cand]:
            break # someone does not know cand
    else:
        return cand # celebrity cand has been found
    return None

def naive_top_sort(G, S=None):
    """naive implementation of topological sorting
    similar to insertion sort
    """
    if S is None:
        S = set(G) # put all items into the set
    if len(S) == 1:
        return list(S) # base: single item
    take_one = S.pop() # reduction: take one out
    seq = naive_top_sort(G, S) # recursively sort the rest
    min_pos = 0 # mark for the position
    for i, u in enumerate(seq):
        if take_one in G[u]: # if there is an edge from i to take_one
            min_pos = i + 1 # update the insert position
    seq.insert(min_pos, take_one) # insert take_one to the right place
    return seq

def top_sort(G):
    """topological sorting based on in-edge counting"""
    count = dict((u, 0) for u in G) # initialize count 0 for every node
    S = [] # result list
    for u in G:
        for v in G[u]:
            count[v] += 1
    Q = [i for i in G if count[i] == 0]
    while Q:
        k = Q.pop()
        S.append(k)
        for l in G[k]:
            count[l] -= 1
            if count[l] == 0:
                Q.append(l)
    return S

def relexation():
    """relexation technique"""
    for v in range(n):
        C[v] = float('inf')
    for i in range(N): # N is a large number
        u, v = random.randrange(n), random.randrange(n)
        C[v] = min(C[v], A[u] + B[u][v]) # relax
