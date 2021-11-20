from django.shortcuts import render, redirect



from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import rest_framework


from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions

from django.views import View

from django.http import HttpResponseRedirect



#models
from PRODUCTOS.model.proveedor import Proveedor
from PRODUCTOS.forms import ProveedorForm



class IndexPageView(View):

    template_name  = "proveedor/index.html"

    def get(self, request):

        pro = Proveedor.objects.all()

        data={
            'proveedores':pro
        }

        return render(request, self.template_name , data)
    

class AddProveedor(View):
    template_name = 'proveedor/agregarProveedor.html'

    def get(self, request):

        if 'submitted' in request.GET:
            submitted  =True
        else:
            submitted = False

        form  = ProveedorForm

        data = {
            'form':form,
            'submitted':submitted
        }

        return render(request, self.template_name, data )

    def post(self, request):
        
        submitted = False

        form = ProveedorForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos/proveedores/add?submitted=True')

        return render(request, self.template_name, {'submitted':submitted})



def updateProveedor(request, *args, **kwargs):
    
    template_name ='proveedor/actualizarProveedor.html'

    proveedor = Proveedor.objects.get(pk = kwargs['pk'])
    form_proveedor = ProveedorForm(request.POST or None, instance=proveedor)

    if form_proveedor.is_valid():
        form_proveedor.save()
        return redirect('listProveedor')

    return render(request, template_name, {'proveedor': proveedor, 'form':form_proveedor})


def deleteProveedor(request,*args, **kwargs):

    producto_del = Proveedor.objects.get(pk = kwargs['pk'])

    producto_del.delete()


    return redirect('listProveedor')




