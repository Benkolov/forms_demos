from django.shortcuts import render
from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(max_length=100)


def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        form.is_valid()
        name = form.cleaned_data['your_name']
    else:
        form = NameForm()
        name = None

    context = {
        'form': form,
        'name': name,
    }
    return render(request, 'web/index.html', context)
