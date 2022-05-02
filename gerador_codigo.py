from ast import Try
import sys

def pontos_circulos(r):
    x = 0
    y = r
    p = 3 - 2*r

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

def mostrar_codigo(r):
    pontos = pontos_circulos(r)
    indice = 0
    for ponto in pontos:
        print( f"if (pixel_x + {ponto[0]} < len(img)) and (pixel_y + {ponto[1]} < len(img[0])):")
        print( f"    matriz[{indice}][img[pixel_x][pixel_y]][img[pixel_x + {ponto[0]}][img[pixel_y+ {ponto[1]}]]] += 1")
        indice+=1

if len(sys.argv) != 2:
    print("Usage: python gerador_codigo.py <radius>")
else:
    try:
        raio = int(sys.argv[1])
        mostrar_codigo(raio)
    except:
        print("Usage: radius must be a number")
