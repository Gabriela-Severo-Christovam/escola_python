def calcular_media(entrada:list[float]) -> float:
    if not isinstance(entrada, list[float]):
        raise ValueError("As notas não é uma lista")

    if len(entrada) == 0:
        raise ValueError("Não é permitido uma lista vazia")

    media = sum(entrada)/len(entrada)
    return round(media,1)