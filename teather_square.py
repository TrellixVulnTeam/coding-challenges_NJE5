def teather_square(w,h,p):
    width_in_pieces=0
    height_in_pieces=0

    if (w % p) != 0:
        width_in_pieces = (w // p) + 1
    else:
        width_in_pieces = (w // p)

    if (h % p) != 0:
        height_in_pieces = (h // p) + 1
    else:
        height_in_pieces = (h // p)
    
    print(width_in_pieces * height_in_pieces)


#width,height,piece=map(int,input().split())
#teather_square(width, height, piece)

testes = [1,0,1,0,0,1]
i=0
for teste in testes:
    if teste:
        print(i)
    i += 1