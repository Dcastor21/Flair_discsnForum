from django.forms import ModelForm
from .models import *


class CreateInForum(ModelForm):
    class Meta:
        model=forum
        fields = "__all__"