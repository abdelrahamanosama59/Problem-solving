import math

ab  = int(input())
bc  = int(input())

ac = math.sqrt((ab*ab) + (bc*bc) )


bm = 0.5 * ac

anglec = math.asin(ab / ac)

anglec = math.degrees(anglec)

print(round(anglec) , chr(176) ,sep = '')
