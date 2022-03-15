from django import forms

class CitasForm(forms.Form):
    
    SERVICIOS_CHOICES = [('Ortodoncia', 'Ortodoncia'),
                         ('Endodoncia', 'Endodoncia'), 
                         ('Odontopediatria', 'Odontopediatria'),
                         ('Curacion', 'Curacion'),
                         ('Profilaxis', 'Profilaxis'),
                         ('Rehabilitacion Oral' , 'Rehabilitacion Oral')]
    
    Nombre = forms.CharField(label="" ,max_length=20, widget=forms.TextInput(attrs={'class':'mt-3',
                                                                          'placeholder':'Nombre',
                                                                          }))
    Email = forms.EmailField(label="" ,widget=forms.TextInput(attrs={'class':'mt-3',
                                                                          'placeholder':'Email',
                                                                          }))
    Celular = forms.CharField(max_length=10, label="" ,widget=forms.NumberInput(attrs={'class':'mt-3',
                                                                          'placeholder':'Celular',
                                                                          }))
    Dia = forms.CharField(label="", widget=forms.TextInput(attrs={'type':'date',
                                                                             'class':'mt-3',
                                                                             })  )
    Hora = forms.CharField( label="", widget=forms.TextInput(attrs={'type':'time',
                                                                                 'class':'mt-3',}))
                                
    Servicio = forms.CharField(label="", widget=forms.Select(choices=SERVICIOS_CHOICES, 
                                                             attrs={'class': 'mt-3'} ))    
    
    Consulta = forms.CharField(label="", max_length=300, widget=forms.TextInput(attrs={'class':'mb-3',
                                                                            'placeholder':'Mi consulta es:',
                                                                            'class':'mt-3 mb-3 p-3',
                                                                                       })) 
    
    Acepto_terminos_de_privacidad = forms.BooleanField(required=True)