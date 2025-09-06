
contador=1
mujeres=0
hombres=0

while(contador <= 6):
    sexo= input("ingrese 1 si es mujer o 2 si es hombre: ")
    if(sexo == "1"):
        mujeres = mujeres+1
    elif(sexo == "2"):
        hombres=hombres+1    
    contador= contador +1

porcentaje_de_mujeres= int(mujeres * 100 / 6)
porcentaje_de_hombres= int(hombres * 100 / 6)

print(f"""porcentaje de hombres %{porcentaje_de_hombres}
porcentaje de mujeres %{porcentaje_de_mujeres}""")