from django import forms
from Sidefi.models import Individuo, Visita
from captcha.fields import CaptchaField


class CaptchaForm(forms.Form):
    captcha = CaptchaField()


# class LoginForm(forms.Form):

# 	nombreusuario = forms.CharField(max_length = 50)
# 	password = forms.CharField(max_length = 20,
# 		widget = forms.TextInput(attrs = {'type' : ' password'}))


class IngresarEstudiante(forms.ModelForm):

    fecha_nac= forms.DateField(widget=forms.TextInput(attrs={'id':'fecha_nac'}))

    class Meta:
        model = Individuo
        fields = ['nombre', 'genero', 'fecha_nac', 'activo', 'centro']

        widgets = {
            'centro': forms.Textarea(attrs = {'cols':50, 'rows':1, 'readonly':True})

        }


class IngresarVisita(forms.ModelForm):

    class Meta:
        model = Visita
        fields = ['codigo', 'activo', 'individuo', 'edad', 'pesoVisita', 'alturaVisita', 'imcVisita', 'pesoReferencia', 

         'alturaReferencia', 'imcReferencia']

        # widgets = {
        #     'codigo': forms.Textarea(attrs = {'cols':12, 'rows':1, 'readonly':True}),
        #     'edad': forms.Textarea(attrs = {'cols':12, 'rows':1, 'readonly':True}),
        #     'pesoReferencia': forms.Textarea(attrs = {'cols':12, 'rows':1, 'readonly':True}),
        #     'alturaReferencia': forms.Textarea(attrs = {'cols':12, 'rows':1, 'readonly':True}),
        #     'imcReferencia': forms.Textarea(attrs = {'cols':12, 'rows':1, 'readonly':True}),
            

        #}

