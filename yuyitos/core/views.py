from django.shortcuts import render

from django.views import View
# Create your views here.
class IndexPageView(View):

    template_name = 'core/home.html'
    
    def get(self, request):

        #aqui hare las consultas de: 
        #ventas en estado fiado,
        #clientes en estado no autorizado para hacer fiado
        #lista de productos con stock critico



        return render(request, self.template_name)