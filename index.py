import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from tabulate import tabulate
matplotlib.use('TkAgg')#solucion error para mostrar la grafica  al hacer un ejecutable del codigo 
import os
import time
from colorama import init, Fore              #follow in ig: @imleticio 
from sympy import symbols
from  sympy import lambdify
from  sympy import sympify,simplify
from pyfiglet import figlet_format
from rich.console import Console   
from rich.markdown import Markdown
from rich.table import Table
from time import sleep
from rich.panel import Panel
import sympy 
from sympy import symbols, Eq, solve, diff
from rich.style import Style
#==============================================================================
init()
init(autoreset=True)
console = Console()

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

#==============================================================================
texto1 = """
Las funciones se ingresan
-a*x**exponente
- seno=sin()
- coseno=cos() 
- tangente=tanh()
- e=exp()

siempre en función de x
"""
x = symbols('x')

texto2="""
Elija una opcion:
-A)Metodo Biseccion
-B)metodo Regula Fassi
-C)Metodo de Newton
-D)Metodo Secante"""
#==============================================================================

def menu():
    
    
    
    while True:
            limpiar_consola()
            print(Fore.GREEN+figlet_format('Metodos Numericos',font="doom",justify='center',width=120))
            Paneli= Panel(texto2, title="Menu", border_style="white", width=40, expand=False)
            console.print(Paneli, justify="center")
            respuesta=console.input((':yellow_circle: Seleccione una [bold cyan]opcion:[/bold cyan]'))
            if respuesta.upper()=='A':
        
        
                while True:
                
                        fx,f,intervalo_x1,intervalo_x2,criterio_toleranza,aux_metodos=pedir_datos(respuesta)
                        aux_intervalox1=intervalo_x1
                        aux_intervalox2=intervalo_x2

                        funcion,solucion,contador,intervalo_x1,intervalo_x2,arr,arr2,arr3,arr4,arr5,bandera =metodo_de_biseccion(f,intervalo_x1,intervalo_x2,criterio_toleranza,fx)

                

                        if bandera==0:
                            aux_solucion=float(solucion)
                            mostrar_resultado(funcion,solucion,contador,intervalo_x1,intervalo_x2,arr,arr2,arr3,arr4,arr5,aux_metodos)
                            print(mostrar_grafica(fx,f,aux_solucion,aux_intervalox1,aux_intervalox2,respuesta))
                            
                            break
            elif respuesta.upper()=='B':
        
        

                while  True:
                
                        fx,f,intervalo_x1,intervalo_x2,criterio_toleranza,aux_metodos=pedir_datos(respuesta)
                        aux_intervalox1=intervalo_x1
                        aux_intervalox2=intervalo_x2


                        funcion,solucion,contador,intervalo_x1,intervalo_x2,arr,arr2,arr3,arr4,arr5,bandera=metodo_regula_falsi(f,intervalo_x1,intervalo_x2,criterio_toleranza,fx)
                

                        if bandera==0:
                            aux_solucion=float(solucion)
                            mostrar_resultado(funcion,solucion,contador,intervalo_x1,intervalo_x2,arr,arr2,arr3,arr4,arr5,aux_metodos)
                            print(mostrar_grafica(fx,f,aux_solucion,aux_intervalox1,aux_intervalox2,respuesta))
                            break

            elif respuesta.upper()=='C':
          
          

                while True:
                        fx,f,intervalo_x1,intervalo_x2,criterio_toleranza,aux_metodos=pedir_datos(respuesta)
                        aux_intervalox1=intervalo_x1
                        aux_intervalox2=intervalo_x2
                        derivada=diff(f)
                        if abs(derivada.subs(x, intervalo_x1)) < 0.00000001:
                            console.print(":x: [red] La derivada en el punto de partida es cercana a cero, no se podra aplicar el metodo desde este punto. [/red]")
                            with Console().status('Esperando para ingresar los datos nuevamente',spinner='aesthetic'):
                                sleep(4)
                        else:
                            funcion,solucion,contador,intervalo_x1,intervalo_x2,arr,arr2,arr3,arr4,arr5,bandera=metodo_newtonRaphson(f,derivada,intervalo_x1,intervalo_x2,criterio_toleranza,fx)
                            if bandera==0:
                                aux_solucion=float(solucion)
                                mostrar_resultado(funcion,solucion,contador,intervalo_x1,intervalo_x2,arr,arr2,arr3,arr4,arr5,aux_metodos)
                                print(mostrar_grafica(fx,f,aux_solucion,aux_intervalox1,aux_intervalox2,respuesta))
                            
                                break
                           
          
            elif respuesta.upper()=='D':
          
                while True:
                
                        fx,f,intervalo_x1,intervalo_x2,criterio_toleranza,aux_metodos=pedir_datos(respuesta)
                        aux_intervalox1=intervalo_x1
                        aux_intervalox2=intervalo_x2
                        funcion,solucion,contador,intervalo_x1,intervalo_x2,arr,arr2,arr3,arr4,arr5,bandera=metodo_secante(f,intervalo_x1,intervalo_x2,criterio_toleranza,fx)
                        if bandera==0:
                            aux_solucion=float(solucion)
                            mostrar_resultado(funcion,solucion,contador,intervalo_x1,intervalo_x2,arr,arr2,arr3,arr4,arr5,aux_metodos)
                            print(mostrar_grafica(fx,f,aux_solucion,aux_intervalox1,aux_intervalox2,respuesta))
                            break
            else:
                console.print(":x: [red] Ingrese una de las opciones que se encuntra disponible [/red]")
                with Console().status('Esperando para ingresar los datos nuevamente',spinner='aesthetic'):
                 sleep(3)

            continuar=console.input(':orange_circle: Desea [blue_violet]ingresar nuevamente una función?: [/blue_violet] [dark_orange3] S/N [/dark_orange3]')
            if continuar.upper()=='N':
                  break

           
            
#==============================================================================
def pedir_datos(arr):
            aux=''
            
            if arr.upper()=='A':
                      aux="Metodo de Biseccion"
            elif arr.upper()=='B':
                      aux="Metodo de Regula Falsi"
            elif arr.upper()=='C':
                      aux='Metodo de Newton Rapshon'
            elif arr.upper()=="D":
                      aux="Metodo Secante"
                      
            limpiar_consola()
            print(Fore.GREEN+figlet_format(aux,font="doom",justify='center',width=120))
            ##############################################################
            panel = Panel(texto1, title="Tener en cuenta", border_style="white", width=40, expand=False)
            console.print(panel, justify="center")

            x = symbols('x')
            


            funcion_ingresada = sympify(console.input(":yellow_circle: Ingrese una [bold cyan]función: [/bold cyan] "))
            print("\n")
            fx=lambdify(x , funcion_ingresada)
            f=sympy.simplify(funcion_ingresada)

            while True:
                try:   

                    intervalo_x1=float(console.input((':yellow_circle: Ingrese el valor del [bold cyan]limite inferior:[/bold cyan]')))
                    print("\n")
                    break
                except ValueError:
                     console.print(':x: [red] Deben de Ingrersar unicamente NUMEROS :x: [/red]\n')

            if arr.upper()=="C":
                    intervalo_x2=None
            else:
                        
                    while True:
                
                        try:

                            intervalo_x2=float(console.input(':yellow_circle: Ingrese el valor del [bold cyan] limite superior:[/bold cyan] '))
                            print("\n")
                            break
                        except ValueError:
                            console.print(':x: [red] Deben de Ingrersar unicamente NUMEROS :x: [/red]\n')

            while True:
                
                try:

                    criterio_toleranza=float(console.input(':yellow_circle: Ingrese el [bold cyan] criterio de toleranza: [/bold cyan]'))
                    break
                except ValueError:
                     console.print(':x: [red] Deben de Ingrersar unicamente NUMEROS :x: [/red]\n')
    
            return fx,f,intervalo_x1,intervalo_x2,criterio_toleranza,aux



#==============================================================================

def mostrar_grafica(fx,funcion_ingresada,raiz,intervalo_x1,intervalo_x2,metodo):
     
     plt.ioff()
     matplotlib.is_interactive()

     if metodo.upper()!="C":
        
        if(intervalo_x1 >=0 ) and (intervalo_x2 >=0):
        
            x_values=np.linspace(0, intervalo_x2, 400)
        
        elif (intervalo_x1 <= 0 ) and (intervalo_x2 <=0) :
        
            x_values=np.linspace(intervalo_x1, 0, 400)
        else:
                x_values = np.linspace(-10, 10, 400)
     else:
           x_values=np.linspace(-10, 10, 400)

     y_values = fx(x_values)
     
     # Graficar la función
     plt.plot(x_values,y_values,label=f'f(x)= {str(funcion_ingresada)}')
     plt.scatter(raiz, fx(raiz), color='red', label='Raíz encontrada')

     plt.axhline(0, color='black', linewidth=0.5)
     plt.title('Gráfico de la función y su raíz')
     plt.axhline(color='black')
     plt.axvline(color='black')
     plt.annotate(round(raiz,9),xy=(raiz,0.5))
     plt.xlabel('x')
     plt.ylabel('f(x)')
     plt.legend()
     plt.grid(True,which='both')
     plt.ylim([-15,15])
                
                

     plt.show()
     
     
#==============================================================================
def mostrar_resultado(funcion,sol,contador,intervalo_x1,intervalo_x2,arr,arr2,arr3,arr4,arr5,metodo):
     
     limpiar_consola()
     print('\n')
     print(Fore.GREEN+figlet_format(metodo,font="doom",justify='center',width=120))

     texto=( f'# La funcion es {funcion}\n')

     md = Markdown(texto)
     console.print(md) 
     if intervalo_x2 ==None and arr3==None:
            resultados=(f""" 
            1. La raiz encontada se encuentra en el punto: {sol} 
            2. La raiz se encontro en la iteracion numero: {contador}
            3. El valor del intervalo x1 es: {intervalo_x1}      
            """)
            console.print(resultados) 
        #print(Fore.YELLOW + tabulate(matriz, headers=['Iteracion','Intervarlo x1','Intervalo x2',' Solucion aproximada','Error relativo'], tablefmt='fancy_grid'))

     
            tabla = Table(show_header=True, header_style="medium_spring_green", style=Style(color="gold1"))
            tabla.add_column('Iteraciones')
            tabla.add_column("Intervalo x1")
            tabla.add_column("Solucion aproximada",style="dark_slate_gray1")
            tabla.add_column("Error relativo")

            for iteraciones,intervalossx1,solucionaprox,error_rela in zip(arr,arr2,arr4,arr5):
                    tabla.add_row(iteraciones,str(intervalossx1),str(solucionaprox),str(error_rela))
     else:
          
            resultados=(f""" 
            1. La raiz encontada se encuentra en el punto: {sol} 
            2. La raiz se encontro en la iteracion numero: {contador}
            3. El valor del intervalo x1 es: {intervalo_x1} 
            4. El valor del intervalo x2 es: {intervalo_x2}     
            """)
            console.print(resultados) 
        #print(Fore.YELLOW + tabulate(matriz, headers=['Iteracion','Intervarlo x1','Intervalo x2',' Solucion aproximada','Error relativo'], tablefmt='fancy_grid'))

     
            tabla = Table(show_header=True, header_style="medium_spring_green", style=Style(color="gold1"))
            tabla.add_column('Iteraciones')
            tabla.add_column("Intervalo x1")
            tabla.add_column("Intervalo x2")
            tabla.add_column("Solucion aproximada",style="dark_slate_gray1")
            tabla.add_column("Error relativo")

            for iteraciones,intervalossx1,intervalossx2,solucionaprox,error_rela in zip(arr,arr2,arr3,arr4,arr5):
                    tabla.add_row(iteraciones,str(intervalossx1),str(intervalossx2),str(solucionaprox),str(error_rela))
          

        
     console.print( tabla  ,justify='center')

#==============================================================================
def caso_de_error(intervalo_x1,intervalo_x2,funcion):
        console.print(f':x: [red] La funcion puede no tener una raiz en el intervalo de X1:{intervalo_x1} Y X2 {intervalo_x2} o bien tiene mas de una raiz :x: [/red]')
        print('\n')
        texto=('# Revise la Grafica de la funcion, para elegir los valores de la funcion')
        md = Markdown(texto)
        console.print(md)

        plt.ioff()
        matplotlib.is_interactive()


        x_values = np.linspace(-10, 10, 400)
        
  
        y_values = funcion(x_values)

        y_values = funcion(x_values)
    # Graficar la función
        
        plt.plot(x_values,y_values,label=f'f(x)= {str(funcion)}')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.title('Gráfico de la función ')
        plt.axhline(color='black')
        plt.axvline(color='black')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.grid(True,which='both')
        plt.ylim([-15,15])
                               
        plt.show()
        with Console().status('Esperando para ingresar los datos nuevamente',spinner='aesthetic'):
                 sleep(3)
     
#==============================================================================
def metodo_regula_falsi(funcion,intervalox1,intervalox2,criterio_toleranza,fx):
    
    error_calculado=101
    arr=[]
    arr3=[]
    arr4=[]
    arr2=[]
    arr5=[]
    contador=0
    bandera=0

    if funcion.subs(x,intervalox1)*funcion.subs(x,intervalox2)<0:
         while  (error_calculado> criterio_toleranza):
              contador+=1
              
              solucion=intervalox2-(funcion.subs(x,intervalox2)*(intervalox2-intervalox1))/(funcion.subs(x,intervalox2)-funcion.subs(x,intervalox1))
              error_calculado=abs((solucion-intervalox1)/solucion)*100

              if funcion.subs(x,intervalox1)*funcion.subs(x,solucion)>0:
                 intervalox1=solucion
              else:
                   intervalox2=solucion
                   
              con='{:.0f} '.format(contador)
              arr.append(con)

              a='{:.10f} '.format(float(intervalox1)) #x-exp(-x)
              arr2.append(a)    

              b='{:.10f} '.format(float(intervalox2))
              arr3.append(b)

              sol='{:.10f} '.format(float(solucion))
              solucion2=str(sol)
              arr4.append(solucion2)

              error_calculado_pasado='{:.10f} '.format(float(error_calculado))
              error=str(error_calculado_pasado)+"%"

              arr5.append(error)  




         return funcion,solucion2,contador,intervalox1,intervalox2,arr,arr2,arr3,arr4,arr5,bandera
         
    else:
        
        bandera+=1
        caso_de_error(intervalox1,intervalox2,fx)

        
        
        return None, None,None,None,None,None, None,None,None,None,bandera

    

#==============================================================================
         
def metodo_de_biseccion (funcion,intervalo_x1,intervalo_x2,error_relativo,fx):
     solucion=None
     contador=0
     error_calculado=101
     arr=[]
     arr2=[]
     arr3=[]
     arr4=[]
     arr5=[]
     matriz=[]
     bandera=0

     if funcion.subs(x,intervalo_x1)*funcion.subs(x,intervalo_x2) < 0:
        while  error_calculado > error_relativo:
            #arr=[]
            contador+=1
            solucion=((intervalo_x1 + intervalo_x2)/2)
            error_calculado=abs((solucion-intervalo_x1)/solucion)*100

            '''if funcion(intervalo_x1)*funcion(solucion)==0:
                print(f"La solucion es {solucion}")'''
            
            if funcion.subs(x,solucion) *funcion.subs(x,intervalo_x1)> 0:
                intervalo_x1=(solucion)
            else:
                intervalo_x2=(solucion)  
            
            con='{:.0f} '.format(contador)
            arr.append(con)

            a='{:.10f} '.format(float(intervalo_x1)) #x-exp(-x)
            arr2.append(a)

            b='{:.10f} '.format(float(intervalo_x2))
            arr3.append(b)

            sol='{:.10f} '.format(float(solucion))
            solucion2=str(sol)
            arr4.append(solucion2)

            error_calculado_pasado='{:.10f} '.format(float(error_calculado))
            error=str(error_calculado_pasado)+"%"
            arr5.append(error)
            
            #matriz.append(arr) 

        return funcion,solucion2,contador,intervalo_x1,intervalo_x2,arr,arr2,arr3,arr4,arr5,bandera

     else:

        bandera+=1
        
        
        caso_de_error(intervalo_x1,intervalo_x2,fx)
        
        return None, None,None,None,None,None, None,None,None,None,bandera
     
def metodo_newtonRaphson(funcion,derivada,intervalo_x1,intervalo_x2,error_relativo,fx):
     
     
     error_calculado=101
     solucion=None
     contador=0
     arr=[]
     arr2=[]
     arr3=None
     arr4=[]
     arr5=[]
     intervalo_x2=None
     bandera=0 
     
     while  error_calculado > error_relativo:
          
          contador+=1
          solucion=intervalo_x1-(funcion.subs(x,intervalo_x1)/derivada.subs(x,intervalo_x1))
          error_calculado=abs((solucion-intervalo_x1)/solucion)*100
          intervalo_x1=solucion

          con='{:.0f} '.format(contador)
          arr.append(con)
          a='{:.10f} '.format(float(intervalo_x1))
          arr2.append(a)
          sol='{:.10f} '.format(float(solucion))
          solucion2=str(sol)
          arr4.append(solucion2)
          error_calculado_pasado='{:.10f} '.format(float(error_calculado))
          error=str(error_calculado_pasado)+"%"
          arr5.append(error)

     
     return funcion,solucion2,contador,intervalo_x1,intervalo_x2,arr,arr2,arr3,arr4,arr5,bandera
     
def metodo_secante(funcion,intervalo_x1,intervalo_x2,error_relativo,fx):
      
      error_calculado=101
      solucion=0
      contador=0
      error_calculado=101
      arr=[]
      arr2=[]
      arr3=[]
      arr4=[]
      arr5=[]
    
      bandera=0

      while error_calculado>error_relativo:
            contador+=1
            xra=solucion
            solucion=intervalo_x2-(funcion.subs(x,intervalo_x2)*(intervalo_x2-intervalo_x1)/(funcion.subs(x,intervalo_x2)-funcion.subs(x,intervalo_x1)))
            error_calculado=abs(((solucion-xra)/solucion)*100)
            intervalo_x1=intervalo_x2
            intervalo_x2=solucion

            con='{:.0f} '.format(contador)
            arr.append(con)
            a='{:.10f} '.format(float(intervalo_x1)) #x-exp(-x)
            arr2.append(a)

            b='{:.10f} '.format(float(intervalo_x2))
            arr3.append(b)

            sol='{:.10f} '.format(float(solucion))
            solucion2=str(sol)
            arr4.append(solucion2)


            error_calculado_pasado='{:.10f} '.format(float(error_calculado))
            error=str(error_calculado_pasado)+"%"
            arr5.append(error)  

      return funcion,solucion2,contador,intervalo_x1,intervalo_x2,arr,arr2,arr3,arr4,arr5,bandera
        
print(menu())

        
