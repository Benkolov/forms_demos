from django.forms import URLInput
from django.shortcuts import render
from django import forms
from .models import Person


class PersonForm(forms.Form):
    your_name = forms.CharField(
        label="Your name",
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your placeholder name',
                'class': 'form-control',
                'custom-attribute': 'custom-value'
            }
        ),
    )

    age = forms.IntegerField()

    HOBBY_CHOICES = [
        (1, 'Football'),
        (2, 'Basketball'),
        (3, 'Tennis'),
    ]

    hobby = forms.CharField(widget=forms.RadioSelect(choices=HOBBY_CHOICES))

    is_happy = forms.BooleanField(required=False)


def index(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']

            Person.objects.create(name=form.cleaned_data['your_name'], age=form.cleaned_data['age'])
    else:
        form = PersonForm()
        name = None

    context = {
        'form': form,
        'name': name,
    }
    return render(request, 'web/index.html', context)
