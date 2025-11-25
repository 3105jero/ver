
import servicios

inventarios=[]

#create the menu for the user
while True:
    print("1.agregar producto")
    print("2.mostrar lista de productos")
    print("3.buscar producto por el nombre")
    print("4.vender producto")
    print("5.eliminar producto")
    print("6.calcular estadisticas")
    print("7.salir")
    ventastotal=0
    vend=0


#the user can't use numbers more big then 7 or more lowe thwn 0
    try:
        opcion=int(input("que opcion desea? "))
        if opcion<0 and opcion>7:
            print("error, solo numeros del 1 al 7")
        else:
            match opcion:

            #if the option is 1 call the funcion "agregar_producto"
                case 1:
                    name=input("dijite el nombre del libro: ")
                    writer=input("dijite el autor: ")
                    category=input("a que categoria pertenece el libro: ")
                    price=float(input("dijite el precio del libro que desee agregar: "))
                    amount=int(input("dijite la cantidad del libro que desee agregar: "))
                    date=input("que fecha se hizo el libro?")
                    sell=0

                    servicios.agregar_producto(inventarios,name,writer,category,price,amount,sell,date)

            #if the option is 2 call the funcion "mostrar_inventario" and show the inventary
                case 2:
                    servicios.mostrar_inventario(inventarios)

            #if the option is 3 call the funcion "buscar_producto" and show all books

                case 3:
                    look=input("diga el nombre del producto que esta buscando: ")
                    servicios.buscar_producto(inventarios,look)

            #if the option is 4 call the funcion "actualizar inventario" and update the amount

                case 4:
                    found=input("ingrese el producto que se vendio ")
                    cantnew=int(input("dijite la cantidad que se vendio: "))
                    servicios.actualizar_producto(inventarios,found,cantnew,ventastotal,vend)

            #if the option is 6 call the funcion "eliminar_producto" and delate one book

                case 5:
                    delate=input("dijite el producto que desee eliminar")
                    servicios.eliminar_producto(inventarios,delate)

            #if the option is 6 call the funcion "calcular_estadisticas" ans show me the most expensive books,the book with more units and the final price

                case 6:
                    servicios.calcular_estadisticas(inventarios)

            #if the option is 7 good bye, break the while

                case 7:
                    break
    except ValueError:
        print("ingrese un valor correcto,intente de nuevo")
