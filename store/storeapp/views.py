from django.contrib import auth, messages
from django.http import HttpResponse
from django.shortcuts import render

from storeapp.form import orderCreationForm
from storeapp.models import Course,Materials


# Create your views here.
def index(request):
   return render(request, "index.html")
def home(request):
  return render(request,"home.html")

from django.shortcuts import render, redirect
def order_create_view(request):

    form = orderCreationForm()
    if request.method == 'POST':
        name = request.POST.get('fname',)
        age=request.POST.get('age')
        dob = request.POST.get('dob',)
        phone = request.POST.get('phone',)
        address = request.POST.get('address',)
        email = request.POST.get('email',)
        purpose = request.POST.get('purpose',)
        department=request.POST.get('department_id')
        course=request.POST.get('course_id')
        materials=Materials(name=name,dob=dob,age=age,phone=phone,address=address,email=email,purpose=purpose,department=department,course=course)
        materials.save()

        form = orderCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order confirmed')

    return render(request, 'home.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('/')






# AJAX
def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'course_dropdown_list_options.html', {'courses': courses})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


