class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rect(object):
    def __init__(self, p1, p2):
        '''Store the top, bottom, left and right values for points
               p1 and p2 are the (corners) in either order
        '''
        self.left   = min(p1.x, p2.x)
        self.right  = max(p1.x, p2.x)
        self.bottom = min(p1.y, p2.y)
        self.top    = max(p1.y, p2.y)


def range_overlap(a_min, a_max, b_min, b_max):
    '''Neither range is completely greater than the other
    '''
    return (a_min <= b_max) and (b_min <= a_max)


def overlap(aMin, aMax, bMin, bMax):
    if aMin.x > bMax.x or


t = int(raw_input())

for i in range(0,t):
    rect1 = map(int, raw_input().split())
    rect2 = map(int, raw_input().split())

    rectMin = Point(rect1[0],rect1[1])
    rectMax = Point(rect1[2],rect1[3])

    rect2Min = Point(rect2[0], rect2[1])
    rect2Max = Point(rect2[2], rect2[3])

    print range_overlap(rectMin,rectMax, rect2Min, rect2Max)


