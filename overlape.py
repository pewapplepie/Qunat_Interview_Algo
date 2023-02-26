

def not_overlap_group(rectangles):
    rectangles.sort()
    group = 1
    prevw, prevl = rectangles[0][0],rectangles[0][1]
    currminl = 0
    for w, l in rectangles[1:]:
        if w >= prevw and l < prevl:
            currminl = l
        elif w>= prevw and l >= currminl:
            print('hi', w, l)
            group += 1
            currminl = l
    
    return group
            
case1 = [(3,4),(1,2),(4,3),(5,5)]
case2 = [(2,5),(5,2),(5,3)]

not_overlap_group(case1)
not_overlap_group(case2)