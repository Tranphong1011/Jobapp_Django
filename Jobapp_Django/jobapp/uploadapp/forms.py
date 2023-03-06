from django import forms
from django.utils.translation import gettext_lazy as _
from uploadapp.models import UploadFiles
from uploadapp.models import Uploads


class uploadappForm(forms.ModelForm):

    class Meta:
        model = Uploads
        fields = '__all__'


class uploadfileForm(forms.ModelForm):

    class Meta:
        model = UploadFiles
        fields = '__all__'
