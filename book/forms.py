from django import forms
from .models import Data

class AddData(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(AddData, self).__init__(*args, **kwargs)
            self.fields['mobile'].widget.attrs = {'class': 'myclass',}
    class Meta:
        model = Data
        fields = ['name', 'lastname', 'locality', 'city', 'mobile', 'email']

