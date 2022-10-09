from django import forms
from .models import *


class OrderForm(forms.ModelForm):

   class Meta:
      model = Order
      exclude =[""]


class FeedbackForm(forms.Form):
   email = forms.EmailField(initial="admin@admin.com", label='Залиште вашу електронну адресу')
   phone = forms.CharField(max_length=10, label='Залиште ваш номер телефону')
   review = forms.CharField(widget=forms.Textarea, label='Залиште ваш відгук')
   grade = forms.ChoiceField(required=False, choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")],
                             label='Оберіть оцінку')
   general_feedback = forms.ChoiceField(required=False, choices=[("1", "Позитивне"), ("2", "Негативне")],
                                        label='Загальне враження')


