"""some data for testing"""

a, b, c, d, e, f, g, h = range(8)
# un-weighted graph
G = [
    {b, c, d, e, f}, #a
    {c, e},
    {d},
    {e},
    {f},
    {c, g, h},
    {f, h},
    {f, g}
]
#weighted graph: dict of lists
W_G = [
    {b:2, c:1, d:3, e:9, f:4},    # a
    {c:4, e:3},                   # b
    {d:8},                        # c
    {e:7},                        # d
    {f:5},                        # e
    {c:2, g:2, h:2},              # f
    {f:1, h:6},                   # g
    {f:9, g:8}                    # h
]

# weighted graph: dict of dicts
W_G_dict_dict = {
    a: {b:2, c:1, d:3, e:-9, f:4},    # a
    b: {c:4, e:3},                   # b
    c: {d:8},                        # c
    d: {e:7},                        # d
    e: {f:5},                        # e
    f: {c:2, g:2, h:2},              # f
    g: {f:1, h:6},                   # g
    h: {f:9, g:8}                    # h
}
