
Xtortuga=float(input("Ingrese distancia en metros"))
Vtortuga=float(input("Ingrese velocidad en m/h"))
XAquiles=0
VAquiles=10*Vtortuga
T=Xtortuga/(9*Vtortuga)
print(int(T))
Tm=(T*60)%60
print(int(Tm))
Ts=(Tm*60)%60
print(int(Ts))
XAquiles = round (10*Vtortuga*T, 5)
print("Aquiles alcanza a la tortuga en: ", int(T), "horas, " , int(Tm), "minutos y " , int(Ts), "sebgundos")
print("Aquiles alcanzo la tortuga a los", XAquiles, "metros")
for i in (5,4,3,2,1):
intervalo_t= T/i
intervalo_en_m=(intervalo_t*60)%60
intervalos_en.s=(intervalo_en_m*60)%60
XAquiles_intervalo=intervalo_t*VAquiles
print("Distancia      Tiempo")
print(round(XAquiles_intervalo, 3)),"m " , int(intervalo_t)