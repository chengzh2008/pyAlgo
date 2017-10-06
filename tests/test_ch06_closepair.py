"""Testing for ch06"""

import logging
import random
import unittest
from bisect import bisect, bisect_left
from copy import deepcopy

LOG = logging.getLogger(__name__)

def find_closest_pair(list_points):
    """wrapper function for finding the closest point and distance"""
    pt_sort_by_x = sorted(list_points, key=lambda x: x[0]) # sort by x coordinate
    pt_sort_by_y = sorted(list_points, key=lambda x: x[1]) # sort by y coordinate
    return closest_pair(pt_sort_by_x, pt_sort_by_y) # resursive D&C

def closest_pair(pt_sort_by_x, pt_sort_by_y):
    num = len(pt_sort_by_y)
    if num <= 3:
        return closest_pair_small3(pt_sort_by_x)
    mid = num // 2 # middle index for the array
    left_x = pt_sort_by_x[:mid] # two part split based on mid of x coordinate
    right_x = pt_sort_by_x[mid:]

    mid_pt_x = pt_sort_by_x[mid][0]

    # split pt_sort_by_y list into two part based on x value
    left_y = list()
    right_y = list()
    for pt in pt_sort_by_y:
        if pt[0] < mid_pt_x:
            left_y.append(pt)
        else:
            right_y.append(pt)

    # recursively call both parts
    (p1, q1, min1) = closest_pair(left_x, left_y)
    (p2, q2, min2) = closest_pair(right_x, right_y)

    # smallest of two parts
    if min1 < min2:
        sm_d = min1
        sm_pair = (p1, q1)
    else:
        sm_d = min2
        sm_pair = (p2, q2)

    (p3, q3, min3) = closest_pair_between_parts(pt_sort_by_x, pt_sort_by_y, sm_d, sm_pair)

    if sm_d < min3:
        return p1, q1, sm_d
    else:
        return p3, q3, min3

def closest_pair_small3(points):
    p1 = points[0]
    p2 = points[1]
    d_12 = dist(p1, p2)
    if len(points) == 2:
        return p1, p2, d_12
    p3 = points[2]
    d_23 = dist(p2, p3)
    d_13 = dist(p1, p3)
    if d_12 < min(d_23, d_13):
        return p1, p2, d_12
    elif d_23 < d_13:
        return p2, p3, d_23
    else:
        return p1, p3, d_13



def closest_pair_between_parts(pt_sort_by_x, pt_sort_by_y, sm_d, sm_pair):
    """find the smallest pair and distance between two parts:"""
    num = len(pt_sort_by_y)
    mid_x = pt_sort_by_x[num//2][0] # middle pioint x value

    # create a subarray of points from pt_sort_by_y that x value is not sm_d away from the mid point.
    sub_pts_by_y = [x for x in pt_sort_by_y if mid_x - sm_d <= x[0] <= mid_x + sm_d]

    # check continuous 7 points in this subarray and find the closest pair from them
    best = sm_d
    len_subarray = len(sub_pts_by_y)
    for i in range(len_subarray):
        for j in range(i+1, min(i+7, len_subarray)):
            p, q = sub_pts_by_y[i], sub_pts_by_y[j]
            dst = dist(p, q)
            if dst < best:
                best = dst
                sm_pair = p, q
    return sm_pair[0], sm_pair[1], best

def dist(p, q):
    import math
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)



class Ch06TestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_closest_pair(self):
        number = 1000 # 1000 points
        int_min = -10**5
        int_max = 10**5
        lst1 = [random.randint(int_min, int_max) for i in range(number)]
        lst2 = [random.randint(int_min, int_max) for i in range(number)]
        list_points = list(zip(lst1, lst2))
        p1, p2, min_d = find_closest_pair(list_points)
        LOG.info("cloest pair is {0}:{1}, distance is {2}".format(p1, p2, min_d))
        self.assertEqual(len(list_points), number +1)






if __name__ == '__main__':
    unittest.main()
