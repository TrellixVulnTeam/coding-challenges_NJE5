def beautiful_year(ano):
    array_ano = []
    for digit in ano:
        array_ano.append(digit)
    set_ano = set(array_ano)
    return(len(set_ano))
print(beautiful_year(str(input())))