import numpy as np
opcion=1
while opcion >= 1 and opcion <= 7:
    print("--------MENU DE LA CALCULADORA-------")
    print("[1]  Suma de matrices")
    print("[2]  Resta de matrices")
    print("[3]  Producto de matriz con una escalar")
    print("[4]  Multiplicacion de matrices")
    print("[5]  Traspuesta de una matriz")
    print("[6]  Inversa de una matriz")
    print("[7]  Rango de la matriz")
    print("[8]  Determinante de una matriz")
    opcion=int(input("Escoje una opcion: "))

    if opcion==int(1):
#-----------------------------------------------------------------------------------------------------------------------------------------
#--------------OPCION 1-------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------

        print("SUMA DE MATRICES")
        f1=int(input("Ingrese numero de filas de Matriz A: "))
        c1=int(input("Ingrese numero de columnas de Matriz A: "))
        f2=int(input("Ingrese numero de filas de Matriz B: "))
        c2=int(input("Ingrese numero de columnas de Matriz B: "))
        if f1==f2 and c1==c2:
            print("------INGRESO DE DATOS------")
            A=np.empty((f1,c1))
            B=np.empty((f2,c2))
            C=np.empty((f1,c1))
            print("Matriz A")
            for i in range(f1):
                for j in range(c1):
                    dato=float(input("Ingrese el valor de ["+str(i+1)+"]["+str(j+1)+"]: "))
                    A[i][j]=dato
            print("Matriz B")
            for i in range(f2):
                for j in range(c2):
                    dato=float(input("Ingrese el valor de ["+str(i+1)+"]["+str(j+1)+"]: "))
                    B[i][j]=dato
                    C[i][j]=A[i][j]+B[i][j]
            print()
            print("Matriz A:")
            print(A)
            print("Matriz B:")
            print(B)
            print("-----RESULTADO-----")

            for i in range(f1):
                for j in range(c1):
                    if j==(c1-1):
                        print(C[i][j])
                    else:
                        print(C[i][j], end=" ")
            print("-----FIN DE SUMA DE MATRICES------")        
        else:
            print("----NO SE PUEDE SUMAR LAS MATRICES----")
            break




    else:
        if opcion==int(2):
#-----------------------------------------------------------------------------------------------------------------------------------------
#--------------OPCION 2-------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------
            print("RESTA DE MATRICES")
            f1=int(input("Ingrese numero de filas de Matriz A: "))
            c1=int(input("Ingrese numero de columnas de Matriz A: "))
            f2=int(input("Ingrese numero de filas de Matriz B: "))
            c2=int(input("Ingrese numero de columnas de Matriz B: "))
            if f1==f2 and c1==c2:
                print("------INGRESO DE DATOS------")
                A=np.empty((f1,c1))
                B=np.empty((f2,c2))
                C=np.empty((f1,c1))
                print("Matriz A")
                for i in range(f1):
                    for j in range(c1):
                        dato=float(input("Ingrese el valor de ["+str(i+1)+"]["+str(j+1)+"]: "))
                        A[i][j]=dato
                print("Matriz B")
                for i in range(f2):
                    for j in range(c2):
                        dato=float(input("Ingrese el valor de ["+str(i+1)+"]["+str(j+1)+"]: "))
                        B[i][j]=dato
                        C[i][j]=A[i][j]-B[i][j]
                print()
                print("Matriz A:")
                print(A)
                print("Matriz B:")
                print(B)
                print("-----RESULTADO-----")

                for i in range(f1):
                    for j in range(c1):
                        if j==(c1-1):
                            print(C[i][j])
                        else:
                            print(C[i][j], end=" ")
                print("-----FIN DE RESTA DE MATRICES------")        
            else:
                print("----NO SE PUEDE RESTAR LAS MATRICES----")
                break

        elif opcion==int(3):
#-----------------------------------------------------------------------------------------------------------------------------------------
#--------------OPCION 3-------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------
            print("-------PRODUCTO DE UNA MATRIZ CON UN ESCALAR--------")
            f=int(input("Ingrese el numero de filas de la matriz:"))
            c=int(input("Ingrese el numero de columnas de la matriz:"))
            A=np.empty((f,c))
            for i in range(f):
                for j in range(c):
                    A[i][j]=input("Ingrese el valor de A["+str(i+1)+"]["+str(j+1)+"]:")
            e=float(input("Ingrese el escalar a multiplicar:"))
            
            print()
            print("LA MATRIZ INGRESADA:")
            print(A, "multiplicado por", e)
            print()
            print("MATRIZ RESPUESTA:")
            for i in range(f):
                for j in range(c):
                    A[i][j]=A[i][j]*e
                    if j==(c-1):
                        print(round(A[i][j],2))
                    else:
                        print(round(A[i][j],2), end=" ") 
            print("-----------FIN DE PRODUCTO DE UNA MATRIZ CON UN ESCALAR-------")
        
        elif opcion==int(4):
#-----------------------------------------------------------------------------------------------------------------------------------------
#--------------OPCION 4-------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------

# Solicitar al usuario las dimensiones de las matrices
                print("       ------MULTIPLICACION DE MATRICES------")
                filas_a = int(input("Ingrese el número de filas de la matriz A: "))
                columnas_a = int(input("Ingrese el número de columnas de la matriz A: "))

                filas_b = int(input("Ingrese el número de filas de la matriz B: "))
                columnas_b = int(input("Ingrese el número de columnas de la matriz B: "))

# Verificar si las dimensiones son adecuadas para la multiplicación de matrices
                if columnas_a != filas_b:
                    print("No es posible multiplicar estas matrices. El número de columnas de A debe ser igual al número de filas de B.")
                else:
    # Ingresar los elementos de las matrices A y B
                    matriz_a = np.zeros((filas_a, columnas_a))
                    matriz_b = np.zeros((filas_b, columnas_b))

                    print("Ingrese los elementos de la matriz A:")
                    for i in range(filas_a):
                        for j in range(columnas_a):
                            matriz_a[i][j] = float(input(f"Elemento A[{i+1}][{j+1}]: "))

                    print("Ingrese los elementos de la matriz B:")
                    for i in range(filas_b):
                        for j in range(columnas_b):
                            matriz_b[i][j] = float(input(f"Elemento B[{i+1}][{j+1}]: "))

    # Multiplicar las matrices
                    resultado = np.dot(matriz_a, matriz_b)

    # Imprimir el resultado
                    print("Matriz A:")
                    print(matriz_a)

                    print("Matriz B:")
                    print(matriz_b)

                    print("Resultado de la multiplicación:")
                    print(resultado)

                    print()
                    print("        -------FIN DE PRODUCTO DE MATRICES-------")



        elif opcion==int(5):
#-----------------------------------------------------------------------------------------------------------------------------------------
#--------------OPCION 5-------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------
            print("             -------TRANSPUESTA DE UNA MATRIZ-------")
            m=int(input("Ingrese el numero de filas de la matriz: "))
            n=int(input("Ingrese el numero de columnas de la matriz: "))
            A=np.empty((m,n))
            T=np.empty((n,m))

            print()
            print("Ingresando los valores de la Matriz...")
            for i in range(m):
                for j in range(n):
                    dato=float(input("Ingrese el valor de A["+str(i+1)+"]["+str(j+1)+"]: "))
                    A[i][j]=dato
                    T[j][i]=dato

            print("Matriz original:")
            print("")
            for i in range(m):
                for j in range(n):
                    if j==(n-1):
                        print(round(A[i][j],2))
                    else:

                        print(round(A[i][j],2), end="  ")

            print("Matriz transpuesta:")
            print("")
            for i in range(n):
                for j in range(m):
                    if j==(m-1):
                        print(round(T[i][j],2))
                    else:
                        print(round(T[i][j],2), end="  ")
            print("---------------FIN DE TRANSPUESTA DE UNA MATRIZ------------------")




        elif opcion==int(6):
#-----------------------------------------------------------------------------------------------------------------------------------------
#--------------OPCION 6-------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------  
                print("       -------INICIO DE INVERSA DE UNA MATRIZ-------")
                print("Solo se acepta matrices cuadradas")
                rango=int(input("Ingrese el rango de la matriz:"))
                A=np.empty((rango,rango))
                for i in range(rango):
                    for j in range(rango):
                        A[i][j]=input("Ingrese el valor de A["+str(i+1)+"]["+str(j+1)+"]:")

                determinante=np.linalg.det(A)
                print()
                #SI LA DETERMINANTE DE LA MATRIZ ES 0, NO TIENE INVERSA
                if determinante==0:
                    print("ESTA MATRIZ NO TIENE INVERSA")
                else:
                    print("La matriz ingresada es:")
                    print(A)
                    print("La inversa es:")
                    print(np.linalg.inv(A))

                print("        -------FIN DE INVERSA DE UNA MATRIZ  -------")





        elif opcion==int(7):
#-----------------------------------------------------------------------------------------------------------------------------------------
#--------------OPCION 7-------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------- 
                print("      -------INICIO DE RANGO DE UNA MATRIZ-------")
                f=int(input("Ingrese numero de filas de Matriz: "))
                c=int(input("Ingrese numero de columnas de Matriz: "))
                A=np.empty((f,c))
                for i in range(f):
                    for j in range(c):
                        dato=float(input("Ingrese el valor de ["+str(i+1)+"]["+str(j+1)+"]: "))
                        A[i][j]=dato

                # Calcula el rango de la matriz
                rango = np.linalg.matrix_rank(A)

                print("Matriz:")
                print(A)
                print("Rango de la matriz:", rango)
                print("      -------FIN DE RANGO DE UNA MATRIZ-------")




        elif opcion==int(8):
#-----------------------------------------------------------------------------------------------------------------------------------------
#--------------OPCION 8-------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------                  
                print("--------CALCULO DEL DETERMINANTE DE UNA MATRIZ--------")
                r=int(input("Ingrese el rango de la matriz: "))
                A=np.empty((r,r))
                for i in range(r):
                    for j in range(r):
                        dato=float(input("Ingrese el valor de A["+str(i+1)+"]["+str(j+1)+"]= "))
                        A[i][j]=dato
                determinante=np.linalg.det(A)
                print()
                print("La determinante es: ", round(determinante))

                print("      -------FIN DE CALCULO DE DETERMINANTE-------")      