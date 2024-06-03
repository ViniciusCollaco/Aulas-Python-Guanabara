def notas(*valores, situacao=False):
    """
    -> Funçao para analizar notas e situações de vários alunos.
    :Parametro valores: uma ou mais notas dos alunos (aceita várias)
    :Parametro situacao: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    boletim = {}
    boletim['Quantidade'] = len(valores)
    boletim['Maior'] = max(valores)
    boletim['Menor'] = min(valores)
    boletim['Media'] = sum(valores) / len(valores)
    if situacao:
        if boletim['Media'] >= 7:
            boletim['Situação'] = 'BOA'
        elif boletim['Media'] >= 5:
            boletim['Situação'] = 'RAZOÁVEL'
        else:
            boletim['Situação'] = 'Reprovado'
    return boletim

resposta = notas(5.5, 2.5, 8.5, situacao=True)
print(resposta)

