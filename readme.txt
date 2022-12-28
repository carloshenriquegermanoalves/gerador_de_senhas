Projeto - Gerador de Senhas:
    - Motivação:
        - Importância de ter senhas fortes em plataformas digitais:
            - Segurança contra ataques cibernéticos
            - Baixo risco de perda de dados
            - Mantém seus dados seguros

    - Objetivo:
        - Criar senhas fortes:
            - Diretrizes:
                - No mínimo 8 caractéres
                - Combinação de letras maiúsculas e minúsculas
                - Símbolos e espaço
            - O que evitar:
                - Palavras repetidas
                - Informações pessoais:
                    - Data de nascimento
                    - Nome de parentes e/ou conhecidos
            - Cuidados adicionais:
                - Trocar a senha periódicamente
                - Não anotar e/ou guardar senhas em lugares óbvios
        
    - Como funcionará o algoritmo:
        - Texto e chave:
            - Passados pelo usuário
            - Criptografado pelo programa:
                - O texto será transformado em código ASCII
                - Cada código ASCII, por letra, terá seu código alterado por uma chave
                - O novo código ASCII gerado será convertido para letra, uma vez que o código ASCII gerado não será equivalente ao texto informado pelo usuário:
                    - O resultado desse processo será a sua senha criptografada

    - Funcionalidade extra:
        - Limite mínimo:
            - Palavra chave precisa ter, no mínimo, 8 caracteres
            - O programa não deixará o usuário progredir a menos que insira uma palavra chave de, no mínimo, 8 caractéres
