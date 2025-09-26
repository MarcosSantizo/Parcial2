from django import forms
from .models import Usuario, Video

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'edad']

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad <= 0:
            raise forms.ValidationError('La edad debe ser mayor a 0.')
        return edad

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['titulo', 'descripcion', 'url']
