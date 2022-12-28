def criptografa_texto(texto, chave):
    novo_texto = ''

    for i in range(len(texto)):
        letra = texto[i]
        codigo = ord(letra) #A função ord recebe, como parâmetro, uma letra e retorna seu código ASCII
        novo_codigo = codigo + chave #O código ASCII numérico será acrescido pela chave, gerando um novo código
        nova_letra = chr(novo_codigo) #O novo código será convertido para o caractére correspondente pela função chr
        novo_texto = nova_letra + novo_texto #O resultado da criptografia será adicionado à variável de novo texto

    return novo_texto #Ao término do processo acima, o texto completo criptografado será retornado


def verifica_comprimento_senha(senha):
    return len(senha)



palavra_chave = ''
while len(senha) < 8:
    palavra_chave = input('Digite a palavra chave [no mínimo 8 caractéres]: ')
    senha = criptografa_texto(palavra_chave, 2)

print(f'Sua nova senha é: {senha}')
print('Use-a com cuidado e não se esqueça de trocá-la periódicamente')
