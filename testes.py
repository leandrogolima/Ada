#import farmacia_versao_foi_amem



lista_clientes = ['Ana','Bruno','Carol','Douglas','Elaine','Fabio']

def carrinho(cliente:object,lista_medicamentos:list)-> list:
    
    compra = []
    fmt = "{:15}|{:^15}|R$ {:<10.2f}"
    if cliente not in lista_clientes: # verificar com cpf dos clientes cadastrados
        return 'Cliente não cadastrado'
    else:
        
        while True:
            produto = input('Entre com o produto ou digite 0 para sair.\n')# verificar com a lista medicamentos
            valor = 10
            if produto == "0":
                break
            else:
                quantidade = input('entre com a quantidade - ')
                compra.append((produto,int(quantidade),int(quantidade)*valor))
                
    print('Cliente: {:<45}'.format(cliente))
    print('-------------------------------------------')
    print('{:15}|{:^15}|R$ {:<10}'.format('Produtos','Quantidade','Valor'))
    print('-------------------------------------------')      
    for i,j, k in compra:
        print(fmt.format(i,j,k))
    total = sum([float(i) for j,k,i in compra])
    print('{:<31}|R$ {:<}'.format('TOTAL',total))
    return compra




carrinho('Ana')





            
    