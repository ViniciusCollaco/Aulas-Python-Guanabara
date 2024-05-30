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
    if situacao != False:
        if boletim['Media'] >= 7:
            boletim['Situação'] = 'Aprovado'
        else:
            boletim['Situação'] = 'Reprovado'
    return boletim

resposta = notas(5.5, 2.5, 10, 6.5)
print(resposta)

