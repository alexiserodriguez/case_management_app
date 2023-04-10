from django import forms
from .models import Cases, CaseComments, CasePresentations, Documents
from django.contrib.auth.models import User
from .widgets import DatePickerInput
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CasesForm(forms.ModelForm):
    lawyers=forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple, label="Abogados propios" )
          
    class Meta:
        model = Cases
        fields = ['name', 'description', 'start_date', 'case_type', 'demandante', 'demandado',
                  'juzgado', 'partido_judicial', 'phase', 'demandado', 'lawyers', 'cont_lawyer_one', 'cont_lawyer_two', 'cont_lawyer_three', 'procurador_one',
                  'procurador_two',
                  'procurador_three','pc_one','pc_two','pc_three']
        CASE_TYPES_CHOICES = (
            ("", "Seleccione un tipo de juicio"),
            ("Juicio ordinario", "Juicio ordinario"),
            ("Juicio verbal", "Juicio verbal"),
            ("Juicio Monitorio", "Juicio Monitorio"),
            ("Juicio Cambiario", "Juicio Cambiario"),
        )

        PHASE_CHOICES = (
            ('', 'Seleccione la fase actual del procedimiento'),
            ('Reclamación Extrajudicial', 'Reclamación Extrajudicial'),
            ('Demanda', 'Demanda'),
            ('Poder Apud Acta', 'Poder Apud Acta'),
            ('Contestación a la demanda', 'Contestación a la demanda'),
            ('Audiencia previa', 'Audiencia previa'),
            ('Juicio oral', 'Juicio oral'),
            ('Recurso apelación', 'Recurso apelación'),
            ('Recurso casación', 'Recurso casación'),
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Introduce el título del procedimiento"
            }),
            'start_date': DatePickerInput(),
            'description': forms.Textarea(attrs={'class': "form-control", 'placeholder': "Introduce la descripción del procedimiento"}),
            'case_type': forms.Select(choices=CASE_TYPES_CHOICES, attrs={'class': 'form-control'}),
            'demandante': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Introduce el nombre del Demandante"
            }),
            'demandado': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Introduce el nombre del Demandado"
            }),
            'juzgado': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Introduce el juzgado"
            }),
            'partido_judicial': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Introduce el partido judicial"
            }),
            'phase': forms.Select(choices=PHASE_CHOICES, attrs={'class': 'form-control'}),
            'cont_lawyer_one': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Introduce el nombre de un abogado contrario",
                'required': True
            }),
            'cont_lawyer_two': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Introduce el nombre de un abogado contrario",
                'required': False
            }),
            'cont_lawyer_three': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Introduce el nombre de un abogado contrario",
                'required': False
            }),
            'procurador_one': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Introduce el nombre de un procurador propio",
                'required': True
            }),
            'procurador_two': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Introduce el nombre de un procurador propio",
                'required': False
            }),
            'procurador_three': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Introduce el nombre de un procurador propio",
                'required': False
            }),
            'pc_one': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Introduce el nombre de un procurador contrario",
                'required': True
            }),
            'pc_two': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Introduce el nombre de un procurador contrario",
                'required': False
            }),
            'pc_three': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Introduce el nombre de un procurador contrario",
                'required': False
            }),

        }
        labels = {
            'name':'Título del procedimiento',
            'description':'Descripción',
            'phase': 'Fase',
            'lawyers': 'Abogados propios',
            'start_date': 'Fecha de comienzo',
            'cont_lawyer_one': 'Abogado contrario 1',
            'cont_lawyer_two': 'Abogado contrario 2',
            'cont_lawyer_three': 'Abogado contrario 3',
            'case_type': 'Tipo de procedimiento',
            'procurador_one': "Procurador propio 1",
            'procurador_two': "Procurador propio 2",
            'procurador_three': "Procurador propio 3",
            'pc_one': "Procurador contrario 1",
            'pc_two': "Procurador contrario 2",
            'pc_three': "Procurador contrario 3",
            
        }


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email",
                  "username", "password1", "password2")


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = CaseComments
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': "form-control", 'placeholder': "Introduce tu comentario"}),
        }
        labels = {
            'comment': "Comentario"
        }
        
class CreatePresentationForm(forms.ModelForm):
    class Meta:
        model = CasePresentations
        fields = ['description', 'presentation_date']
        widgets = {
            'description': forms.Textarea(attrs={'class': "form-control", 'placeholder': "Introduce tu comentario"}),
            'presentation_date':DatePickerInput()
        }
        labels = {
            'description': "Descripción de presentación",
            'presentation_date':"Fecha de presentación"
        }

class DocForm(forms.ModelForm):
    class Meta:
        model=Documents
        fields=('title','doc')
        
        labels={
            'title':'Título',
            'doc':'Documento (PNG,JPG)'
        }