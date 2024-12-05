from django.shortcuts import render,redirect
from .models import User_Data

# Create your views here.
def home_page(request):

    display_data = User_Data.objects.all()

    return render(request,'home.html',{'display_data':display_data})


def contact_page(request):
    if request.method == 'POST':
        # Accessing POST data correctly
        a = request.POST.get('f_name')
        b = request.POST.get('l_name')
        c = request.POST.get('email')
        d = request.POST.get('mobile')
        e = request.POST.get('message')

        User_Data.objects.create(
            first_name=a,
            last_name=b,
            email=c,
            mobile=d,
            message=e
        )

        # Redirect to home page
        return redirect('home')

    return render(request, 'contact.html')
