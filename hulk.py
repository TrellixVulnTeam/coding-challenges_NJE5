def hate_and_love(layers):
    retorno = "I "
    for i in range( layers):
        if i == 0:
            retorno += "hate "
        elif i % 2 == 0:
            retorno += "that I hate "
        else:
            retorno += "that I love "
    retorno += "it"
    print(retorno)
        
hate_and_love(int(input()))