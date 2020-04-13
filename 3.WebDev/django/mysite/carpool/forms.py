from .models import NewDriverModel,DriverDatabaseModel
from django.forms import ModelForm


class NewDriverModelForm(ModelForm):
    class = Meta:
        model = NewDriverModel
        fields = '__all__'
        

class DriverDatabaseModelForm(ModelForm):
    class = Meta:
        name = DriverDatabaseModel
        fields = '__all__'