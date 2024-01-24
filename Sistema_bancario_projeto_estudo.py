saldo = 8000
limite = 500
extrato = ""
numero_saque = 0
opcao = 1
deposito = 0
valor_saque = 0
quantidade_saque = 0
numero_operacao = 0
texto = "-"
SAQUE_MAXIMO = 3


while opcao != 0:
   
    opcao = input('''
        Bem vindo ao sistema bancário
                  
        [1] Depósito
        [2] Saque
        [3] Extrato
        [0] Fechar o programa
                  
        Selecione uma das opções e aperte " enter ":'''
    )
    if len(opcao) == 1:
        for i in opcao:
            teste = "1230"
            
            if opcao in teste:
                opcao = int(opcao)
                print(texto.center(60, '-'))
                if opcao == 1:
                    print(f"Saldo atual R$:{saldo}")
                    deposito = float(input("Digite o valor que deseja depositar R$:"))
                    if deposito > 0:
                        saldo += deposito
                        print(f"seu novo saldo é de: R$:{saldo:.2f}")
                        numero_operacao += 1
                        extrato += str(numero_operacao) + "- DEPOSITO R$:" + str(deposito) + " Saldo atual R$:" + str(saldo) + "\n"
                        print(texto.center(60, '-'))
                    else:
                        print(texto.center(60, 'x'))
                        print("Valor inválido !")
                        print(texto.center(60, 'x'))
                    
                elif opcao == 2:
                    
                    print(f"Saldo atual R$:{saldo}")
                    print(f"Saques diários realizados: {quantidade_saque}")
                    if SAQUE_MAXIMO != quantidade_saque:
                        valor_saque = float(input("Digite o valor que deseja sacar:"))
                        
                        if valor_saque < saldo:    
                            if valor_saque <= 500 and valor_saque < saldo and valor_saque > 0:

                                if SAQUE_MAXIMO > quantidade_saque:
                                    saldo -= valor_saque
                                    quantidade_saque += 1
                                    numero_operacao += 1
                                    extrato += str(numero_operacao) + "- SAQUE R$:" + str(valor_saque) + " Saldo atual R$:" + str(saldo) + "\n"
                                    
                                    
                                    print(f"Saques máximos no dia : 3\nSaques diários realizados: {quantidade_saque}")
                                    print(texto.center(60, '-'))
                                    
                            elif valor_saque <= 0:
                                print(texto.center(60, 'x'))
                                print("Valor inválido !")
                                print(texto.center(60, 'x'))
                            elif valor_saque > 500:
                                print("Valor do saque acima dos R$:500 permitido")
                                print(texto.center(60, 'x'))
                        else: 
                            print("Saldo insuficiente")    
                            print(texto.center(60, 'x')) 
                    else:
                        print(texto.center(60, 'x')) 
                        print("Não restam mais saques diários")    
                        print(texto.center(60, 'x'))  

                elif opcao == 3:
                    print(extrato)
                    print(texto.center(60, '-'))
        
                elif opcao == 0:
                    print(texto.center(60, '-'))
                    print("Obrigado por usar nossos serviços")
                    print(texto.center(60, '-'))
            else:
                print(texto.center(60, 'x'))
                print("Digite uma opção válida !".center(10, '#'))
                print(texto.center(60, 'x'))
    else:
        print(texto.center(60, 'x'))
        print("Digite uma opção válida !".center(10, '#'))
        print(texto.center(60, 'x'))
        
