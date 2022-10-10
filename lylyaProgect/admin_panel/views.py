from django.shortcuts import render


def index_admin_panel(request):
    return render(request, 'admin_panel.html')
