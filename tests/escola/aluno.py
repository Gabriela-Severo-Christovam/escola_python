def calcular_media(entrada:list[float]) -> float:

    """"
    Calcula a média de uma lista de notas. 

    Parâmetros:
    notas (list[float]): Lista de notas a serem calculadas.

    Retorna:
    float: A média das notas, arredondada para uma casa decimal.
    """

    #Validando se entrada é uma lista 
    if not isinstance(entrada, list):
        raise TypeError("Nota invalida")

    #Validando se a lista é vazia
    if len(entrada) == 0:
        raise ValueError("Não é permitido uma lista vazia")

    for entradas in entrada:
        if not type(entradas) == int and not type(entradas) == float:
            raise TypeError("nota invalida")
        if entradas < 0 or entradas > 10:
            raise ValueError("nota invalida")

    media = sum(entrada)/len(entrada)
    return round(media,1)