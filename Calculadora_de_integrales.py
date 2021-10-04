from string import ascii_lowercase
from tkinter import  Tk,Label,Frame,Canvas,GROOVE,Scrollbar,filedialog,StringVar,Button,Entry
from sympy import integrate,Symbol 
root= Tk()
root.title("Calculadora de integrales entre rectas")
root.resizable(False,False)
root.geometry("440x630")

def main():   
    datos = (var_texto.get())  # Obtenemos el número de la StringVar
    actual.set(f"La direccion actual es:{datos}")    
    with open(datos,"r") as archivo:
        lista = [linea.rstrip() for linea in archivo]

    for i in range(len(lista)):
        if int(lista[i]) >= 1 and int(lista[i]) <=20:
            a= int(lista[i]),i
            break
    repeticiones=a[0]               
    marca=a[1]
    print("La cantidad de repeticiones es: ",lista[marca])
    milabel=Label(frame,text=f"La cantidad de repeticiones es: {lista[marca]}")
    milabel.pack()
    aux4=0
    for i in range(1,len(lista)-marca): 
        pendientes=[]
        coeficientes=[]    
        pts_interseccion={}    
        marca+=1
        if marca <= len(lista)-1:
            blabla=lista[marca].split()
            if len(blabla)==1 and blabla[0] not in ascii_lowercase and aux4 <=repeticiones:        
                aux4+=1
                print(aux4,") Area")
                milabel=Label(frame,text=f"{aux4}) Area").pack()
                if int(lista[marca]) >= 2 and int(lista[marca]) <=100000:
                    cantidad_rectas = int(lista[marca]),marca
                    marca=cantidad_rectas[1]                    
                    print("La cantidad de rectas es de: ",lista[marca])
                    milabel=Label(frame,text=f"La cantidad de rectas es: {lista[marca]}").pack()
                    aux2=0            
                    aux3=1
                    condicion=True
                    aux=0 
                    while condicion == True:
                        orden=lista[marca+aux3].split()
                        print("los puntos x1,y1,x2,y2 en ese orden son: ",orden)
                        milabel=Label(frame,text=f"los puntos x1,y1,x2,y2 en ese orden son: {orden}").pack()
                        aux3+=1     
                        if aux3 == cantidad_rectas[0]+1:
                            condicion=False
                            break                                  
                        for i in range(4):
                            if float(orden[i]) < -1000 or float(orden[i]) >1000 or len(orden) != 4:
                                aux+=1 
                                condicion= False
                                print("No cumple requisitos")
                                milabel=Label(frame,text="No cumple requisitos").pack()
                                break
                    if aux==0:
                        for i in range(1,cantidad_rectas[0]+1):
                            orden=lista[marca+i].split()
                            x_1=float(orden[0])
                            y_1=float(orden[1])                
                            x_2=float(orden[2])
                            y_2=float(orden[3])
                            aux2+=1                    
                            try:
                                m = (y_2-y_1) / (x_2-x_1)
                            except ZeroDivisionError:
                                print("La recta no existe")            
                            c = y_1 - m*(x_1)
                            pendientes.append(m)
                            coeficientes.append(c)
                        print(">>>>>>>>>Se guardaron los puntos anteriores")
                        milabel=Label(frame,text=">>>Se guardaron los puntos anteriores").pack()
                    if aux2 == cantidad_rectas[0]:
                        marca+=aux2
                        print("la variable es en el eje: ",lista[marca+1])
                        print("*************************************")
                        milabel=Label(frame,text=f"la variable es en el eje: {lista[marca+1]}")
                        milabel.pack()
                        milabel=Label(frame,text="***********************************").pack()
                        if lista[marca+1] == "x":
                            marca+=2
                            orden=lista[marca].split()
                            print("limite inferior es de: ",orden[0])
                            milabel=Label(frame,text=f"limite inferior es de: {orden[0]}").pack()
                            print("limite superior es de: ",orden[1])
                            milabel=Label(frame,text=f"limite superior es de: {orden[1]}").pack()
                            interseccion(coeficientes,pendientes,pts_interseccion) #diccionario de intersecciones
                            correcion=pts_interseccion.items() #Lista de intersecciones
                            print("los pts de interseccion son: ",pts_interseccion)##
                            print("los coeficientes son:",coeficientes)##
                            print("las pendientes son: ",pendientes)##
                            calculo(float(orden[0]),float(orden[1]),correcion,"x",pendientes,coeficientes)
                        elif lista[marca+1] == "y":
                            marca+=2
                            orden=lista[marca].split()
                            print("limite inferior es de: ",orden[0])
                            milabel=Label(frame,text=f"limite inferior es de: {orden[0]}").pack()
                            print("limite superior es de: ",orden[1])
                            milabel=Label(frame,text=f"limite superior es de: {orden[1]}").pack()
                            interseccion(coeficientes,pendientes,pts_interseccion) #diccionario de intersecciones
                            correcion=pts_interseccion.items() #Lista de intersecciones
                            calculo(float(orden[0]),float(orden[1]),correcion,"y",pendientes,coeficientes)
                        else:
                            print("Eje ingresado no valido")
                            milabel=Label(frame,text="Eje ingresado no valido").pack()
                else:
                    print("La cantidad de rectas no cumple requisitos")
                    milabel=Label(frame,text="La cantidad de rectas no cumple requisitos").pack()               
                print("__________________________________________________________")
                milabel=Label(frame,text="__________________________________________________________").pack()
                print("\n")
                milabel=Label(frame,text="\n").pack()

myframe=Frame(root,relief=GROOVE,width=150,height=100,bd=1).place(x=10,y=10)
canvas=Canvas(myframe)
frame=Frame(canvas)
var_texto = StringVar()
mi_label = Label(frame, text="Especifique la direccion de archivo que desea usar:").pack()
mi_label1 = Label(frame, text=r"Ejemplo:C:\Users\ nombre\Escritorio\datos.dat").pack()
cuadro_texto = Entry(frame, textvariable=var_texto).pack()

def ficheros():    
    fichero=filedialog.askopenfilename(title="Datos")
    var_texto.set(fichero)
    
btn_examinar = Button(frame,text="Examinar...",command=ficheros)
btn_examinar.pack()
btn_aceptar = Button(frame, text="Aceptar", command=main)
btn_aceptar.pack()
actual = StringVar()
mi_label2 = Label(frame, textvariable=actual).pack()
def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=400,height=600)

def calculo(limite_inferior,limite_superior,correcion,eje,pendientes,coeficientes ):               
    comprobante=[]
    first_interseccion = sorted(correcion, key=lambda tup: tup[0]) #lista de intersecciones ordenadas   
    for i in range(len(first_interseccion)):
        if first_interseccion[i][0] > limite_inferior and first_interseccion[i][0] < limite_superior:
            comprobante.append(first_interseccion[i][0])
    if eje == "x":
        superior=alturas_x(limite_inferior,pendientes,coeficientes)[-1][1]
        inferior=alturas_x(limite_inferior,pendientes,coeficientes)[0][1]
    elif eje == "y":
        superior=alturas_y(limite_inferior,pendientes,coeficientes)[-1][1]
        inferior=alturas_y(limite_inferior,pendientes,coeficientes)[0][1]        
    
    if len(comprobante) >= 1:               
        if eje == "x":
            area_inicial1=integrales_x(pendientes[superior],coeficientes[superior],pendientes[inferior],coeficientes[inferior],limite_inferior,comprobante[0])
        elif eje== "y":
            area_inicial1=integrales_y(pendientes[superior],coeficientes[superior],pendientes[inferior],coeficientes[inferior],limite_inferior,comprobante[0])            
        area_inicial=abs(area_inicial1)  

        sumas_areas_intermedias=[]
        for i in range(len(comprobante)):
            if eje == "x":
                superior=alturas_x(comprobante[i],pendientes,coeficientes)[-1][1]
                inferior=alturas_x(comprobante[i],pendientes,coeficientes)[0][1]
            elif eje == "y":
                superior=alturas_y(comprobante[i],pendientes,coeficientes)[-1][1]
                inferior=alturas_y(comprobante[i],pendientes,coeficientes)[0][1]                    
            if i < len(comprobante)-1:    
                if eje == "x":
                    area_intermedia1=integrales_x(pendientes[superior],coeficientes[superior],pendientes[inferior],coeficientes[inferior],comprobante[i] , comprobante[i+1])
                elif eje == "y":
                    area_intermedia1=integrales_y(pendientes[superior],coeficientes[superior],pendientes[inferior],coeficientes[inferior],comprobante[i] , comprobante[i+1])                    
                area_intermedia=abs(area_intermedia1)
                sumas_areas_intermedias.append(area_intermedia)
        
        medio=0
        if len(sumas_areas_intermedias) != 0:
            for i in sumas_areas_intermedias:
                medio+=i
            
        if eje == "x":
            superior=alturas_x(comprobante[len(comprobante)-1],pendientes,coeficientes)[-1][1]
            inferior=alturas_x(comprobante[len(comprobante)-1],pendientes,coeficientes)[0][1]
        elif eje == "y":
            superior=alturas_y(comprobante[len(comprobante)-1],pendientes,coeficientes)[-1][1]
            inferior=alturas_y(comprobante[len(comprobante)-1],pendientes,coeficientes)[0][1]            
    
        if eje == "x":
            area_final1=integrales_x(pendientes[superior],coeficientes[superior],pendientes[inferior],coeficientes[inferior],comprobante[len(comprobante)-1],limite_superior)
        elif eje == "y":
            area_final1=integrales_y(pendientes[superior],coeficientes[superior],pendientes[inferior],coeficientes[inferior],comprobante[len(comprobante)-1],limite_superior)            
        area_final=abs(area_final1)
            
        area_total= area_inicial + medio + area_final  
        print("El area total por metodo de las partes es : ",area_total)
        milabel=Label(frame,text=f"EL area por mrtodo de las partes es de: {area_total}").pack()
    else:
        if eje == "x":
            area=integrales_x(pendientes[superior],coeficientes[superior],pendientes[inferior],coeficientes[inferior],limite_inferior,limite_superior)
        elif eje == "y":            
            area=integrales_y(pendientes[superior],coeficientes[superior],pendientes[inferior],coeficientes[inferior],limite_inferior,limite_superior)           
        
        milabel=Label(frame,text=f"EL area por integrales simples es de: {area}").pack()
        print("EL area por integrales simples es de: ",area)

def interseccion(coeficientesc,pendientesm,pts_interseccion):
    for i in range(len(coeficientesc)):
        for j in range(len(coeficientesc)):
            if (pendientesm[i] - pendientesm[j]) != 0: 
                x = float((coeficientesc[j] - coeficientesc[i])/(pendientesm[i] - pendientesm[j]))
                y= float(pendientesm[i]*x + coeficientesc[i])
                pts_interseccion[x]=y

def alturas_x(x,pendientes,coeficientes):
    igriegas=[]
    for i in range(len(coeficientes)):
        y=x*pendientes[i]+coeficientes[i]
        z=y,i,pendientes[i]
        igriegas.append(z)
    sorted_by_first = sorted(igriegas, key=lambda tup: (tup[0],tup[2]))   
    return sorted_by_first

def integrales_x(pendiente1,coeficiente1,pendiente2,coeficiente2,punto_inicio,punto_final):
    x = Symbol("x") 
    a=integrate(((pendiente1*x+coeficiente1)-(pendiente2*x+coeficiente2)),(x,punto_inicio,punto_final))
    return a

def alturas_y(y,pendientes,coeficientes):
    igriegas=[]
    for i in range(len(coeficientes)):
        x=(y-coeficientes[i])/pendientes[i]
        z=x,i,pendientes[i]
        igriegas.append(z)
    sorted_by_first = sorted(igriegas, key=lambda tup: (tup[0],tup[2]))   
    return sorted_by_first

def integrales_y(pendiente1,coeficiente1,pendiente2,coeficiente2,punto_inicio,punto_final):
    y = Symbol("y") 
    a=integrate(((y-coeficiente1)/pendiente1-((y-coeficiente2)/pendiente2)),(y,punto_inicio,punto_final))
    return a
##########################################################################################
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)
myscrollbar.pack(side="right",fill="y")
canvas.pack()
canvas.create_window((0,0),window=frame,anchor="center")
frame.bind("<Configure>",myfunction)

root.mainloop()