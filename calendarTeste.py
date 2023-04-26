from datetime import date #puxa o horario do sistema

DIAS = [ #cria se uma variavel chamada dias a qual recebe como conteudo os dias da semana
    'Segunda-feira', #insere o valor de segunda feira a variavel ''DIAS''
    'Terça-feira',   #insere o valor de terça feira a variavel ''DIAS''
    'Quarta-feira',  #insere o valor de quarta feira a variavel ''DIAS''
    'Quinta-Feira',  #insere o valor de quinta feira a variavel ''DIAS''
    'Sexta-feira',   #insere o valor de sexta feira a variavel ''DIAS''
    'Sábado',        #insere o valor de sanado a variavel ''DIAS''
    'Domingo'        #insere o valor de doming a variavel ''DIAS''
]

data_completa= input()# insere um valor a variavel 'data_completa

if len(data_completa) == 10: # vefica se a string possui 10 posições

    componentes = data_completa.split() # divide a string em 3 posiçoes ['21','03','2023']
    
    if len(componentes) == 3: # verifica se a variavel 'componentes' possui seu tamanho iqual a 3
        if componentes[0].isdigit() and componentes[1].isdigit() and componentes[2].isdigit() : # verifica se o conteudo das 3 posições de 'componentes' são numeros
            if len(componentes[0]) == 2 and len(componentes[1]) == 2 and len(componentes[2]) == 4: #verifica se dia,mes e ano possuem o tamanho correto
                
                day = int(componentes[0]) # a variavel 'day' recebe o valor da 'componentes' na posição '0' convertido em um inteiro
                
                month = int(componentes[1]) # a variavel 'month' recebe o valor da 'componentes' na posição '1' convertido em um inteiro
                
                year = int(componentes[2])   # a variavel 'year' recebe o valor da 'componentes' na posição '2' convertido em um inteiro

                if day < 32 and month < 13 : # criasse uma condicional onde day precisa recever uma valor inferior a 32 e a variavel 'month' receber um valor menor que 13
                    try: # faz o uso da função try para que o codigo não seja quebrado por nenhum eventual erro
                        data = date(year , month , day )  #cria se uma variavel chamada 'data' a qual recebe os valores das variaveis 'day' , 'month' e 'year' em convertidos no formato de data

                        indice_da_semana = data.weekday() # cria se uma variavel chamada 'indice_da_semana' a qual recebe o dia da semana correspondente a data inserida

                        dia_da_semana = DIAS[indice_da_semana] # a variavel 'dia_da_semana' recebe o valor da variavel 'DIAS' na posição correspondente 
                        print(dia_da_semana)
                    except:
                        print('ocorreu um erro inesperado,por favor informe uma data valida')
                    
                else:
                    print('por favor,insira um dia ou um mes valido') 
            else:
                print('por favor,insira no formato correto') 
        else:
            print('por favor,insira apenas numeros')             
    else:
        print('por favor,insira no formato DD MM YYYY')      

else: #se é string, não possui 10 posições
    print('por favor,verifique o tamanho da data' ) # imprime uma mensagem de erro no console