from django import forms

class psicologoform(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    especialidad=forms.CharField(max_length=50)


class contactoform(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    mensaje=forms.CharField(max_length=50)
    


class especialidadesform(forms.Form):
   tipo=forms.CharField(max_length=50)

class busquedaform(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    especialidad=forms.CharField(max_length=50)
    



