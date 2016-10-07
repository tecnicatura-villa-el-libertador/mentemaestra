from django import forms

def verificar(numero):
    if not numero.isdigit():
        return False
    if len(numero) != 4:
        return False
    if len(set(numero)) != 4:
        return False
    return True

class IngreseNumero(forms.Form):
	numero = forms.CharField(label="ingrese numero", max_length = 4)

	def clean_numero(self):
		numero = self.cleaned_data['numero']
		if not verificar(numero) :
			raise forms.ValidationError("no cumple con los requisitos!")
		return numero

class Registrar(forms.Form):
    nombre = forms.CharField(label="ingrese nombre", max_length = 15)

class Elegir(forms.Form):
    privado = forms.BooleanField(label="privado")
    


