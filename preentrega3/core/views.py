from django.shortcuts import render

#crea tus vistas

def index(request):
    return render(request,"core/index.html",{"nombre":"ferreteria"}) 