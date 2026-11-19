from poligono import *
def main():
    q = Quadrado(20)
    print(f"Um quadrado de {q.lado}cm tem perimetro de {q.perimetro()}mm")
    print(f"Um quadrado de {q.lado}cm tem area de  {q.area()}mm2")

    c = Circulo(12)
    print(f"Um circulo de raio {c.raio}cm tem perimetro de {c.perimetro():.1f}cm")
    print(f"Um circulo de raio {c.raio}cm tem area de {c.area():.1f}cm3")

if __name__ == '__main__':
    main()