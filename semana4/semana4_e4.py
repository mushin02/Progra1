primer_numero= int(input("ingrese primer numero: "))
segundo_numero=int(input("ingrese segundo numero: "))
primer_tercero=int(input("ingrese tercero numero: "))

numeros= [primer_numero, segundo_numero, primer_tercero]
sorted_numeros = sorted(numeros)

print(sorted_numeros)
print (f'el mayor es {sorted_numeros[2]}')