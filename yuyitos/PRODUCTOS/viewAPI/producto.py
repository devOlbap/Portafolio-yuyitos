from django.shortcuts import render



from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import rest_framework


from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions



#models
from PRODUCTOS.model.producto import Producto
from PRODUCTOS.model.producto import ProductoSerializer



class IndexPageView(APIView):

    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            pro = Producto.objects.all()
            serial = ProductoSerializer(pro, many=True)

        except Exception as ex:
            print(str(ex), ': error try get toda las solicitudes')

        return JsonResponse(serial.data, safe=False)
    
    def post(self, request,*args, **kwargs):

        prod_serial = ProductoSerializer(data= request.data)

        if prod_serial.is_valid():
            prod_serial.save()

            resp ={
                'mensaje': 'producto creado'
            }

            return Response(prod_serial.data, resp)
        
        resp ={
            'mensaje':'error al crear producto'
        }
        return Response(prod_serial.errors,resp)

class ProductoView(APIView):

    def get(self,request, *args, **kwargs):
        
        try:
            prod = Producto.objects.get(pk=self.kwargs['pk'])
        
        except Exception as ex:
            print( 'ERROR AL CONSULTAR UN PRODUCTO POR SU PK',str(ex))
        
        producto_detalle = ProductoSerializer(prod)

      
        return JsonResponse(producto_detalle.data)
    
    def put(self, request, *args, **kwargs):
        
        try: 
            qProducto = Producto.objects.get(pk=self.kwargs['pk'])

        except Exception as ex:
            print("error except def put ",str(ex))

        if  qProducto:


            qProducto.sku = request.data['sku']
            qProducto.descripcion = request.data['descripcion']
            qProducto.precio_compra = request.data['precio_compra']
            qProducto.precio_venta = request.data['precio_venta']
            qProducto.stock = request.data['stock']
            qProducto.stock_critico = request.data['stock_critico']
            qProducto.categoria = request.data['categoria']
            qProducto.tipo_producto = request.data['tipo_producto']
            qProducto.proveedor = request.data['proveedor']

            #print(data)
            #exit()

            qProducto.save()

            resp = {
                'mensaje':'Producto actualizado correctamente '
            }

            return JsonResponse(resp)

        else:
            resp = {
                'mensaje':'error al actualizar producto'
            }
            return JsonResponse(resp)

    def delete(self, requet, *args, **kwargs):
        
        delProducto = Producto.objects.filter(pk=self.kwargs['pk'])
 
        if delProducto:

            delProducto.delete()
            resp = {
                'mensaje':'producto eliminado correctamente'
            }
            return JsonResponse(resp)
        else:
            resp = {
                'mensaje':'error al eliminar producto'
            }
            return JsonResponse(resp)
     
