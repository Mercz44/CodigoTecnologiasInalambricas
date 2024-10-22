print("Programa que calcula la pérdida de señal dependiendo de la distancia y los vidrios con los que se cuentan.")

numVidrios = int(input("Ingrese cuántos cristales se tienen en el problema: "))


numSeñal = float(input("Ingrese el valor de la señal inicial: "))


for i in range(numVidrios):
    numSeñal *= 0.90 
    print(f"Después de {i + 1} cristal(es), la señal es: {numSeñal:.2f}")

print(f"Señal final después de {numVidrios} cristales: {numSeñal:.2f}")
