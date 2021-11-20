from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect

from CLIENTES.model.cliente import Cliente 

from CLIENTES.form import ClienteForm

from django.views import View


class IndexPageView(View):
    template_name = "cliente/index.html"

    def get(self, request):
        
        
        clientes = Cliente.objects.all()

        data={
            'clientes':clientes
        }

        return render(request, self.template_name, data)

class AddCliente(View):

    template_name = "cliente/agregarCliente.html"

    def get(self, request):

        form = ClienteForm

        if 'submitted' in request.GET:
            submitted = True
        else:
            submitted = False

        return render(request, self.template_name, {'form':form, 'submitted':submitted})

    def post(self, request):
        
        submitted = False

        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/clientes/add?submitted=True')

        return render(request, self.template_name, {'submitted':submitted})


def updateCliente(request, *args, **kwargs):
    
    template_name ='cliente/actualizarCliente.html'

    cliente = Cliente.objects.get(pk = kwargs['pk'])
    form_cliente = ClienteForm(request.POST or None, instance=cliente)

    if form_cliente.is_valid():
        form_cliente.save()
        return redirect('listClientes')

    return render(request, template_name, {'cliente': cliente, 'form':form_cliente})

def deleteCliente(request,*args, **kwargs):

    cliente_del = Cliente.objects.get(pk = kwargs['pk'])

    cliente_del.delete()


    return redirect('listClientes')




