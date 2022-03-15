from re import template
from django.shortcuts import render
from django.views import generic
from .forms import CitasForm
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

class HomeView(generic.TemplateView):
    template_name = 'index.html'
    
class ServicesView(generic.TemplateView):
    template_name = 'services.html'
    
class CitasView(generic.FormView):
    form_class = CitasForm
    template_name = 'citas.html'
    
    def get_success_url(self):
        return reverse('citas')
    
    def form_valid(self, form):
        messages.info(self.request, 'Cita agendada exitosamente, pronto nos pondremos en contacto contigo.')
        
        name = form.cleaned_data.get('Nombre')
        email = form.cleaned_data.get('Email')
        celular = form.cleaned_data.get('Celular')
        dia = form.cleaned_data.get('Dia')
        hora = form.cleaned_data.get('Hora')
        servicio = form.cleaned_data.get('Servicio')
        consulta = form.cleaned_data.get('Consulta')
        terminos = form.cleaned_data.get('Acepto_terminos_de_privacidad')
        
        full_message = f"""
                  CITA PROGRAMADA
        ____________________________________
        Nombre: {name}
        Email: {email}
        Telefono: {celular}
        Dia: {dia} Hora: {hora}
        Servicio: {servicio}
        ____________________________________
        
        Consulta: {consulta}
        
        """
        if terminos is True:
            send_mail(
                subject= "Cita Programada",
                message= full_message,
                from_email= settings.DEFAULT_FROM_EMAIL,
                recipient_list= [settings.NOTIFY_EMAIL],
            )
        
            return super(CitasView, self).form_valid(form)
    
