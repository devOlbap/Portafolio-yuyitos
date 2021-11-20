from django.shortcuts import render, redirect



from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


from django.views import View

from django.http import HttpResponseRedirect



#models
from PRODUCTOS.model.pedido import Pedido
from PRODUCTOS.forms import PedidoForm



class IndexPageView(View):

    template_name  = "pedido/index.html"

    def get(self, request):

        ped = Pedido.objects.all()

        data={
            'pedidos':ped
        }

        return render(request, self.template_name , data)
    

class AddPedido(View):
    template_name = 'pedido/agregarPedido.html'

    def get(self, request):

        if 'submitted' in request.GET:
            submitted  =True
        else:
            submitted = False

        form  = PedidoForm

        data = {
            'form':form,
            'submitted':submitted
        }

        return render(request, self.template_name, data )

    def post(self, request):
        
        submitted = False

        form = PedidoForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos/pedido/add?submitted=True')

        return render(request, self.template_name, {'submitted':submitted})



def updatePedido(request, *args, **kwargs):
    
    template_name ='pedido/actualizarPedido.html'

    pedido = Pedido.objects.get(pk = kwargs['pk'])
    form_pedido = PedidoForm(request.POST or None, instance=pedido)

    if form_pedido.is_valid():
        form_pedido.save()
        return redirect('listPedidos')

    return render(request, template_name, {'pedido': pedido, 'form':form_pedido})


def deletePedido(request,*args, **kwargs):

    pedido_del = Pedido.objects.get(pk = kwargs['pk'])

    pedido_del.delete()


    return redirect('listPedidos')


