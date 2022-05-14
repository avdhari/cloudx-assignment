from django.shortcuts import render
from contact.models import UserData


def home_view(request):
    data_list = UserData.objects.all()
    context = {
        'data_list': data_list,
    }
    return render(request, 'contact/home.html', context)