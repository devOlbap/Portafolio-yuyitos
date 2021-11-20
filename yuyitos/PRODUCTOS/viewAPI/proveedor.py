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
from PRODUCTOS.model.proveedor import Proveedor
from PRODUCTOS.model.proveedor import ProveedorSerializer




class IndexPageView(APIView):

    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            prov = Proveedor.objects.all()
            serial = ProveedorSerializer(prov, many=True)

        except Exception as ex:
            print( ':Try get all proveedores',str(ex))

        return JsonResponse(serial.data, safe=False)
    
    def post(self, request,*args, **kwargs):

        serialProv = ProveedorSerializer(data= request.data)

        if serialProv.is_valid():
            serialProv.save()

            resp ={
                'mensaje': 'proveedor creado'
            }

            return Response(resp, status=status.HTTP_201_CREATED)
        
        resp ={
            'mensaje':'error al crear proveedor'
        }
        return Response(serialProv.errors,resp)

class ProveedorView(APIView):

    def get(self,request, *args, **kwargs):
        
        try:
            prove = Proveedor.objects.get(pk=self.kwargs['pk'])
        
        except Exception as ex:
            print(str(ex), 'TRY CONSULTA PROVEEDOR POR PK')
        
        serialProveedor = ProveedorSerializer(prove)

      
        return JsonResponse(serialProveedor.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        
        try: 
            posProveedor = Proveedor.objects.filter(pk=self.kwargs['pk'])

        except Exception as ex:
            print("error except def put ",str(ex))

        if posProveedor:
            upProveedor = Proveedor.objects.get(pk = self.kwargs['pk'])
            upProveedor.razon_social = request.data['razon_social']
            upProveedor.rut = request.data['rut']
            upProveedor.dv = request.data['dv']
            upProveedor.direccion = request.data['direccion']
            upProveedor.giro = request.data['giro']
            upProveedor.rubro = request.data['rubro']
            upProveedor.telefono = request.data['telefono']
            upProveedor.correo = request.data['correo']
            upProveedor.nom_representante = request.data['nom_representante']
            upProveedor.comuna = request.data['comuna']


            #print(data)
            #exit()

            upProveedor.save()

            resp = {
                'mensaje':'proveedor actualizado correctamente '
            }

            return JsonResponse(resp)

        else:
            resp = {
                'mensaje':'error al actualizar proveedor'
            }
            return JsonResponse(resp)

    def delete(self, requet, *args, **kwargs):

        try:
            delProveedor = Proveedor.objects.filter(pk=self.kwargs['pk'])
        except Exception as ex:
            print(str('error try DELETE: ', ex))

        if delProveedor:
            prov = Proveedor.objects.get(pk=self.kwargs['pk'])
            prov.delete()
            resp = {
                'mensaje':'proveedor eliminado correctamente'
            }
            return JsonResponse(resp)
        else:
            resp = {
                'mensaje':'error al eliminar proveedor'
            }
            return JsonResponse(resp)
     
