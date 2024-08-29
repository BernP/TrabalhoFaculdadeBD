#Gerador de CEP aleatório
from random import randint





def CriarNomeAleatorio():
    primeirosNome = ['Augusto', 'Joao', 'Jose', 'Ricardo', 'Felipe', 'Lucas', 'Igor', 'Arthur', 'Artur', 'Andre', 'Anderson', 'Eduardo', 'Bruno', 'Mario', 'Maria', 'Maria Eduarda', 'Helena', 'Filipa','Felicia', 'Lara','Luana','Leticia','Cecilia','Marina','Mariana','Carolina','Raquel']
    sobreNomes = ['Silva', 'da Silva', 'Cruz', 'da Cruz', 'Carvalho', 'Pereira', 'Silveira', 'Figueredo', 'Costa','da Costa', 'Ferreira', 'Lima', 'Santos', 'Mendes', 'Nunes','Teixeira', 'Marques', 'Alves', 'Gomes', 'Lopes', 'Sousa', 'Souza']
    
    nome = primeirosNome[randint(0, len(primeirosNome)-1)] + ' '
    quantidadeDeSobrenomes = randint(1, 5)
    
    for x in range(quantidadeDeSobrenomes):
        escolhido = randint(0,len(sobreNomes)-1)
        if x < quantidadeDeSobrenomes-1:
            nome += sobreNomes[escolhido] + ' '
            sobreNomes.pop(escolhido)
        else:
            nome += sobreNomes[escolhido]
            sobreNomes.pop(escolhido)

    return(nome)

def CriarCepAleatorio():
    cep = ""
    for x in range(5):
        cep += (chr(randint(0,9)+48))

    cep += '-'

    for x in range(3):
        cep += (chr(randint(0,9)+48))
    
    return cep

def CriarCPFAleatorio():
    cpf = ""
    for x in range(3):
        for y in range(3):
            cpf += (chr(randint(0,9)+48))

        if(x<2):
            cpf += '.'

    cpf += '-'

    for x in range(2):
        cpf += (chr(randint(0,9)+48))
    
    return cpf

def CriarEndereçoAleatorio():
    primeirosNome = ['Augusto', 'Joao', 'Jose', 'Ricardo', 'Felipe', 'Lucas', 'Igor', 'Arthur', 'Artur', 'Andre', 'Anderson', 'Eduardo', 'Bruno', 'Mario', 'Maria', 'Maria Eduarda', 'Helena', 'Filipa','Felicia', 'Lara','Luana','Leticia','Cecilia','Marina','Mariana','Carolina','Raquel']
    sobreNomes = ['Silva', 'da Silva', 'Cruz', 'da Cruz', 'Carvalho', 'Pereira', 'Silveira', 'Figueredo', 'Costa','da Costa', 'Ferreira', 'Lima', 'Santos', 'Mendes', 'Nunes','Teixeira', 'Marques', 'Alves', 'Gomes', 'Lopes', 'Sousa', 'Souza']
    

    nome = primeirosNome[randint(0, len(primeirosNome)-1)] + ' '
    quantidadeDeSobrenomes = randint(1, 2)
    
    for x in range(quantidadeDeSobrenomes):
        escolhido = randint(0,len(sobreNomes)-1)
        if x < quantidadeDeSobrenomes:
            nome += sobreNomes[escolhido] + ' '
            sobreNomes.pop(escolhido)
        else:
            nome += sobreNomes[escolhido]
            sobreNomes.pop(escolhido)

    epipeto = ['Marechal', 'Comandante', 'Capitao', 'Professor(a)', 'Presidente', 'Desembargador(a)', 'Sr(a).']
    lugares = ['Praca', 'Rua', 'Avenida']

    endereco = lugares[randint(0, len(lugares)-1)] + ' ' + epipeto[randint(0, len(epipeto)-1)] + ' '+ nome +'- numero '+ str(randint(1,1200))
    
    if(randint(0,9) >= 8):
        endereco += ' apt. ' + chr(randint(0,9)+48)+chr(randint(0,5)+48)+chr(randint(1,9)+48)
    
    return(endereco)

#print(CriarNomeAleatorio())
#print(CriarCepAleatorio())
#print(CriarCPFAleatorio())
#print(CriarEndereçoAleatorio())


quantidadeDeUsuarios = 2000
arquivo = open('comando_insert.txt', 'w+')


for x in range(quantidadeDeUsuarios):
    codigoParaInserir = "INSERT INTO USUARIOS (nome, cpf, cep, endereco, id) VALUES (" + "'"+CriarNomeAleatorio()+ "'," + ' '+ "'" + CriarCPFAleatorio()+ "'," + ' '+ "'"+  CriarCepAleatorio() + "'," + ' '+ "'" + CriarEndereçoAleatorio()+ "', "+ str(x) +');\n'
    arquivo.write(codigoParaInserir)
arquivo.close()