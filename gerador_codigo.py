from ast import Try
import sys

# Uso do algoritmo de Bresenham para obtenção dos pontos do círculo
# @param r -> raio do círculo
# @return pontos -> set com os pontos do círculo de raio r
def pontos_circulos(r):
    x = 0
    y = r
    p = 3 - 2*r

    #Guardar os pontos em um Set para já descartar pontos repetidos
    pontos =  {( x,  y)}
    pontos.add((-x,  y))
    pontos.add(( x, -y))
    pontos.add((-x, -y))
    pontos.add(( y,  x))
    pontos.add((-y,  x))
    pontos.add(( y, -x))
    pontos.add((-y, -x))

    while(x<y):
        if(p<0):
            p += 4*x + 6
        else:
            p += 4*(x-y) + 10
            y-=1
        x+=1
        pontos.add(( x,  y))
        pontos.add((-x,  y))
        pontos.add(( x, -y))
        pontos.add((-x, -y))
        pontos.add(( y,  x))
        pontos.add((-y,  x))
        pontos.add(( y, -x))
        pontos.add((-y, -x))
        
    return pontos


# Gerador do código para cálculo da matriz de co-ocorrência - evita fazer ponto a ponto
# @param r -> raio da matriz circular
def mostrar_codigo(r):

    # Obter set dos pontos
    pontos = pontos_circulos(r)

    # Printar código
    print(f"# Cálcula a matriz circular de co-ocorrência de raio {r}")
    print("# @param img -> matriz 2d de tons de cinza da imagem, tons -> quantização dos tons de cinza") 
    print(f"def c{r}(img, tons):")
    print("    # Matriz de co-ocorrência número de tons x número de tons")
    print("    matriz = np.zeros(tons*tons).reshape(tons, tons)")
    print("\n    # Contador de pontos inseridos")
    print("    contador_pontos = 0")
    print("\n    # Verificar co-ocorrência pixel a pixel")
    print("    for linha_pixel in range(len(img)):")
    print("        for coluna_pixel in range(len(img[0])):")
    print("\n            # Verificar co-ocorrência entre o pixel e todos os pontos do círculos")
    for ponto in pontos:
        print( f"            if (linha_pixel + {ponto[0]} < len(img)) and (coluna_pixel + {ponto[1]} < len(img[0])):")
        print( f"                matriz[img[linha_pixel][coluna_pixel]][img[linha_pixel + {ponto[0]}][img[coluna_pixel+ {ponto[1]}]]] += 1")
        print(  "                contador_pontos += 1")
    
    print("\n    # Calcular Probabilidade de cada co-ocorrência")
    print("    for linha_pixel in range(tons):")
    print("        for coluna_pixel in range(tons):")
    print("            matriz[linha_pixel][coluna_pixel] /= contador_pontos")
    print("    return matriz")


# Uso pela linha de comando
if len(sys.argv) != 2:
    print("Usage: python gerador_codigo.py <radius>")
else:
    try:
        raio = int(sys.argv[1])
        mostrar_codigo(raio)
    except:
        print("Usage: radius must be a number")
