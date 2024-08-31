from random import randint

#itens = ['anel tipo 1', 'anel tipo 2', 'anel tipo 3', 'colar tipo 1', 'colar tipo 2', 'colar tipo 3', 'brinco tipo 3', 'pulseira tipo 3', 'pulseira tipo 3']
itens_base = ['anel', 'colar', 'brinco', 'pulseira', 'relogico']
tipo=['ouro', 'prata', 'prata banhado a ouro',  'aco inox banhado a prata','aco inox']
com = [ 'com diamante', 'com rubi', 'com safira' ,'com perola', 'com esmeralda', 'sem adorno']
tamanho = ['A', 'B', 'C', 'D', 'E']
quantidadeDeUsuarios = 2000
arquivo = open('comando_insert_itens.txt', 'w+')
lista_de_itens = []

x = 0
for i in itens_base:
    random_valor_para_item = randint(30, 300)
    for t in range(len(tipo)):
        for c in range(len(com)):
            for tm in range(len(tamanho)):
                if randint(1,10) < 8:
                    nome = f'{i} feito de {tipo[t]} {com[c]} de tamanho {tamanho[tm]}' 
                    qnt = randint(100, 500)
                    preco = random_valor_para_item + 55*(len(com)-c)*(len(com)-c) + 40*(len(tipo)-t)*(len(tipo)-t) + 15*(len(tamanho)-tm)*(len(tamanho)-tm)
                    codigoParaInserir = "INSERT INTO ITENS (id, item, preco, quantidade_restante) VALUES (" +str(x)+ "," + ' '+ "'" + nome+ "'," + ' '+ ""+  str(preco) + "," + ' '+ "'" + str(qnt)+ "'"+  ');\n'
                    arquivo.write(codigoParaInserir)
                    lista_de_itens.append([x, nome, preco, qnt])
                    x+=1

        
arquivo.close()  

quantidadeDePedidos = 10_000
arquivo = open('comando_insert_pedidos.txt', 'w+')

status = ['pagamento pendente', 'pago', 'item enviado', 'recebido']
for x in range(quantidadeDePedidos):

    id_usuario = randint(0, 1999)

    quantidade_de_compras = randint(1, 20)
    if(quantidade_de_compras < 10):
        quantidade_de_compras = 1
    elif( quantidade_de_compras <15):
        quantidade_de_compras = 2
    elif( quantidade_de_compras <=17):
        quantidade_de_compras = 3
    elif( quantidade_de_compras <=19):
        quantidade_de_compras = 4
    else:
        quantidade_de_compras = 5

    status_agora = status[randint(0,len(status)-1)]
    dia = randint(1,29)
    if(dia<10):
        data = '2024-0'+str(randint(1,8))+'-0'+str(dia)
    else:
        data = '2024-0'+str(randint(1,8))+'-'+str(dia)
    for y in range(quantidade_de_compras):  
        item_escolhido = randint(0, len(lista_de_itens)-1)
        while(lista_de_itens[item_escolhido][3]<3):
            item_escolhido = randint(0, len(lista_de_itens))
        
        quantidade_comprada = randint(1,10)
        if(quantidade_comprada < 8):
            quantidade_comprada = 1
        elif(quantidade_comprada <=9):
            quantidade_comprada = 2
        else:
            quantidade_comprada = 3

        lista_de_itens[item_escolhido][3] -= quantidade_comprada
        codigoParaInserir = "INSERT INTO PEDIDOS (id, id_item, quantidade, data, status, id_usuario) VALUES (" + ""+str(x)+ "," + ' '+ "" + str(item_escolhido)+ "," + ' '+ ""+  str(quantidade_comprada) + "," + ' '+ "'" + data+ "', '"+status_agora +"', "+str(id_usuario) +  ');\n'
        arquivo.write(codigoParaInserir)
arquivo.close()