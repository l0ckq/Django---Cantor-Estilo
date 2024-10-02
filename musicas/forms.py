from django import forms
from .models import Musica

class MusicaForm(forms.ModelForm):
    class Meta: # -> Classe dentro da classe. Serve como uma espécie de parâmetro
        model = Musica
        fields =  ['nome', 'estilo'] # Dentro do Fields, se passa os campos necessárias que estão na Model 

    # A Classe Meta guarda e "modifica" os dados da classe especificada em model. O campo fields significa literalmente "campos"