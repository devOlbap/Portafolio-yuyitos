from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_exempt


from django.views import View

from django.http import HttpResponseRedirect



#models
from PRODUCTOS.model.producto import Producto
from PRODUCTOS.forms import ProductoForm



class IndexPageView(View):

    template_name  = "producto/index.html"

    def get(self, request):

        pro = Producto.objects.all()

        data={
            'productos':pro
        }

        return render(request, self.template_name , data)
    

class AddProducto(View):
    template_name = 'producto/agregarProducto.html'

    def get(self, request):

        if 'submitted' in request.GET:
            submitted  =True
        else:
            submitted = False

        form  = ProductoForm

        data = {
            'form':form,
            'submitted':submitted
        }

        return render(request, self.template_name, data )

    def post(self, request):
        
        submitted = False

        form = ProductoForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos/add?submitted=True')

        return render(request, self.template_name, {'submitted':submitted})



def updateProducto(request, *args, **kwargs):
    
    template_name ='producto/actualizarProducto.html'

    producto = Producto.objects.get(pk = kwargs['pk'])
    form_producto = ProductoForm(request.POST or None, instance=producto)

    if form_producto.is_valid():
        form_producto.save()
        return redirect('listProductos')

    return render(request, template_name, {'producto': producto, 'form':form_producto})

def deleteProducto(request,*args, **kwargs):

    producto_del = Producto.objects.get(pk = kwargs['pk'])

    producto_del.delete()


    return redirect('listProductos')





