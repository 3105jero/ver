

#create the diccionary and safe the values in the list

def agregar_producto (inventarios,name,writer,category,price,amount,sell,date):
    producto = {
            'nombre':name,
            'autor':writer,
            'categoria':category,
            'precio':price,
            'cantidad':amount,
            'ventas':sell,
            'fecha':date
        }
    inventarios.append(producto)

    #show the inventory, if inventory is empty show "inventary empty,safe a book"

def mostrar_inventario(inventarios):
    if inventarios==[]:
            print("inventario vacio,recuerda ingresar un libro")

    else:
        for i in inventarios:
            print(f"producto: {i['nombre']} | autor: {i['autor']} | categoria: {i['categoria']} | valor: {i['precio']} | cantidad: {i['cantidad']}")

        #look the book for the name,if no have this name "no found"

def buscar_producto(inventarios,look):
    for g in inventarios:
            if look == g ['nombre']:
                print(f"producto: {g['nombre']} | autor: {g['autor']} | categoria: {g['categoria']} | valor: {g['precio']} | cantidad: {g['cantidad']}")
            else:
                    print ("producto no encontrado")

        #if sell a book, update the amount, if the inventory if empty show a message

def actualizar_producto(inventarios,found,cantnew,ventastotal,vend):
    if inventarios==[]:
            print("inventario vacio,recuerda ingresar un producto")
    else:
        
        for e in inventarios:
            if found==e['nombre']:

                ventastotal=e['ventas']+cantnew
                vend=e['cantidad']-cantnew
                e.update({'cantidad':vend})
                e.update({'ventas':ventastotal})
                print(f"ventas totales por el momento son {e['ventas']}")

            else:
                print ("producto no encontrado")

        #delate the book,if the inventory if empty show a message

def eliminar_producto(inventarios,delate):
    if inventarios==[]:
        print("inventario vacio,recuerda ingresar un producto")
    else:
        for eli in inventarios:
            if delate == eli['nombre']:
                inventarios.remove(eli)
            else:
                print ("producto no encontrado")

        #calculate the price, the top 3 books more expensive,the most expensive book, the book with the most units, and if have discount or not

def calcular_estadisticas(inventarios):
    #create the variables for the calculation
    valortotal=0
    cantidadtotal=0
    preciofinal=0
    preciofinal2=0
    preciofina=0

    #the user answer if have discount and the name of the book or all books
    discount=input("tiene descuento? ")
    estadist=input("ingrese el nombre del libro al que le quiere sacar el valor total del inventario / todos")


    if inventarios==[]:
        print("inventario vacio,recuerda ingresar un producto")

    else:
        #When the discount is no, the values ​​do not get the 10% discount.

        if discount=="no":

        #when the user seek only a book
            for esta in inventarios:
                if estadist == esta['nombre']:
                    valortotal=esta['precio']
                    cantidadtotal=esta['cantidad']
                    preciofinal=valortotal*cantidadtotal
                    print(f"producto: {esta['nombre']} | valor: {esta['precio']} | cantidad: {esta['cantidad']} | su valor total es {preciofinal}")

            #if the user seek all books

                elif estadist=="todos":
                    preciofina= esta['cantidad']*esta['precio']
                    preciofinal2+=preciofina
                    cantidadtotal+=esta['cantidad']

            maximovalor=None
            maximocantidad=None
            nameva=""
            nameca=""

            #look for the most expensive

            for maxi in inventarios:
                if maximovalor is None or maxi['precio']>maximovalor:
                    maximovalor=maxi['precio']
                    nameva=maxi['nombre']

            #find the one with the most units

                if maximocantidad is None or maxi ['cantidad']>maximocantidad:
                    maximocantidad=maxi['cantidad'] 
                    nameca=maxi['nombre']

            #print the most expensive, the most units and the total number of products and price


            print(f"el producto con mayor precio es: {nameva} | valor: {maximovalor} ")
            print(f"el producto con mayor cantidad es: {nameca} | cantidad: {maximocantidad} ")
            print(f"hay un total de {cantidadtotal} de productos, y en total con todos los productos tienes {preciofinal2} a la venta")

            #seek the top 3 most expenisve books 


            productos_ordenados = sorted(inventarios, key=lambda x: x['precio'], reverse=True)
            top_3_mas_caros = productos_ordenados[:3]
            for cost in top_3_mas_caros:
                print(f"los productos mas costosos son: {cost['nombre']} | valor: {cost['precio']} ")

            #It's the same as if there's no discount, but in the end I multiply the values ​​by 0.90

        if discount == "si":

            for esta in inventarios:
                if estadist == esta['nombre']:
                    valortotal=esta['precio']
                    cantidadtotal=esta['cantidad']
                    preciofinal=valortotal*cantidadtotal
                    print(f"producto: {esta['nombre']} | valor: {esta['precio']*0.90} | cantidad: {esta['cantidad']} | su valor total es {preciofinal*0.90}")

                elif estadist=="todos":
                    preciofina= esta['cantidad']*esta['precio']
                    preciofinal2+=preciofina
                    cantidadtotal+=esta['cantidad']


            maximovalor=0
            maximocantidad=0
            nameva=""
            nameca=""

            for maxi in inventarios:
                if maxi['precio'] > maximovalor:
                    maximovalor=maxi['precio']
                    nameva=maxi['nombre']

                if maxi['cantidad'] > maximocantidad:
                    maximocantidad=maxi['cantidad']
                    nameca=maxi['nombre']



            print(f"el producto con mayor precio es: {nameva} | valor: {maximovalor*0.90} ")
            print(f"el producto con mayor cantidad es: {nameca} | cantidad: {maximocantidad} ")
            print(f"hay un total de {cantidadtotal} de productos, y en total con todos los productos tienes {preciofinal2*0.90} a la venta")
            
            productos_ordenados = sorted(inventarios, key=lambda x: x['precio'], reverse=True)
            top_3_mas_caros = productos_ordenados[:3]
            for cost in top_3_mas_caros:
                print(f"los productos mas costosos son: {cost['nombre']} | valor: {cost['precio']} ")


