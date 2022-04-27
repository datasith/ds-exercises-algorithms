def iou(bbox1, bbox2):
    
    xm1,ym1,xM1,yM1 = bbox1
    xm2,ym2,xM2,yM2 = bbox2

    if xm2 > xM1 or xm1 > xM2 or yM1 < ym1 or yM2 < ym1:
        return 0

    bbox_i = [max(xm1,xm2), max(ym1,ym2), min(xM1,xM2), min(ym1,ym2)]

    return area(bbox_i) / ( area(bbox1) + area(bbox2) - area(bbox_i) )

def area(bbox):
    x1,y1,x2,y2 = bbox
    return abs(x1-x2) * abs(y1-y2)


if __name__ == '__main__':
    bbox1 = [0,0,1,1]
    bbox2 = [0.5,0.5,1,1]
    ans = iou(bbox2,bbox1) # -> 0.25
    assert ans == 0.25, "check yo code!"
    print(ans)