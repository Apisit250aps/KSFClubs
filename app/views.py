from django.shortcuts import render

# Create your views here.

def page(request):
    
    return render(request, 'index.html')


def staff_palace(request):
    
    return render(request, 'palace.html')