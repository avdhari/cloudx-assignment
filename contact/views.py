from django.shortcuts import render, redirect
from contact.models import UserData
from contact.forms import NewContactForm


def home_view(request):
    data_list = UserData.objects.all()
    form = NewContactForm()
    if request.POST:
        form = NewContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success-page')

    context = {
        'data_list': data_list,
        'form': form,
    }
    return render(request, 'contact/home.html', context)


def success_view(request):
    return render(request, 'contact/success.html')