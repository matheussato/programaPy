
def ehTriangulo(lado1,lado2,lado3):
    return lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2
    # if (lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2):
    #     return True
    # else: return False


def tipoTriangulo1(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        return True
    else: False

def tipoTriangulo2(lado1,lado2,lado3):
    if lado1 == lado2 and lado1 != lado3 or lado3 == lado1 and lado3 != lado2:
        return True
    else: return False
    
def tipoTriangulo3(lado1,lado2,lado3):    

    if lado1 != lado2 and lado2 != lado3 :
        return True
    else:return False
       
     
while True:
    
    print("""   
                MENU
                
            1- Digitar valor dos lados
            2- Sair
           """)
    opcao = int(input("Digite a opção desejada= "))

    if opcao == 1:
        l1 = int(input("Digite um valor do lado= "))
        l2 = int(input("Digite um valor do lado= "))
        l3 = int(input("Digite um valor do lado= "))
        
        if ehTriangulo(l1,l2,l3):
            if tipoTriangulo1(l1,l2,l3) :
                print(" Equilátero")
            elif tipoTriangulo2(l1,l2,l3) :
                print("Isósceles")
            elif tipoTriangulo3(l1,l2,l3) :
                print("Escaleno")            
            
        else:print("Não é triângulo")        
        
    elif opcao == 2:
        break





        

        
        
        
        


