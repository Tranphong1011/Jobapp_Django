
from django import forms
from django.utils.translation import gettext_lazy as _
from register.models import Register



def validator(value):
    if "," in value:
        raise forms.ValidationError('Invalid Input, Please enter again')
    return value
    
    
    
# class RegisterForm(forms.Form):
#     email = forms.EmailField(max_length=200, validators=[validator], label="Email")
#     first_name = forms.CharField(max_length=200, validators=[validator], label="First name")
#     last_name = forms.CharField(max_length=200, validators=[validator], label="Last name")
#     update_f_name = forms.CharField(max_length=200, validators=[validator], label="Update first name")
#     update_l_name = forms.CharField(max_length=200, validators=[validator], label="Update last name")
    
#     def clean_first_name(self):
#         data = self.cleaned_data['first_name']
#         if "," in data:
#             raise forms.ValidationError('Invalid first_name')
#         return data

# sử dụng model form 
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields= '__all__'
        # exclude = ('first_name',)
        labels = {
            'first_name': _('Enter first name'),
            'last_name': _('Enter last name'),
            'update_f_name': _('Update first name'),
            'update_l_name': _('Update last name')}
        help_texts = {'first_name' : _('Enter characters only')}
        error_message = {
            'first_name':{
                'required':_('First name invalid'),
            }
        }
        