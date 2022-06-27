from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http.response import StreamingHttpResponse
from .models import Car
from .forms import RegisterUserForm, AddCarForm
from .main_app import VideoCamera

# Create your views here.



# For deleting car
@login_required(login_url="/login_user")
def delete_car(request, car_id):
    car = Car.objects.get(pk=car_id)
    car.delete()
    messages.success(request, ("A car is successfully deleted"))
    return redirect('view_car')


# For updating car
@login_required(login_url="/login_user")
def update_car(request, car_id):
    car = Car.objects.get(pk=car_id)
    form = AddCarForm(request.POST or None, instance=car)
    if form.is_valid():
        form.save()
        messages.success(request, ("A car is successfully updated"))
        return redirect('view_car')

    return render(request, 'update_car.html', {'car': car, 'form': form})

# For adding car
@login_required(login_url="/login_user")
def add_car(request):
    submitted = False
    if request.method == "POST":
        form = AddCarForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user
            event.save()
            return HttpResponseRedirect('/add_car?submitted=True')
    else:
        form = AddCarForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_car.html',  {'form': form, 'submitted': submitted})

# For viewing car
@login_required(login_url="/login_user")
def view_car(request):
    car_owner = request.user # get current user
    car_list = Car.objects.filter(owner = car_owner) # get data of current user
    return render(request, 'view_car.html', {'car_list': car_list})

@login_required(login_url="/login_user")
def dashboard(request):
    return render(request, "index.html")

@login_required(login_url="/login_user")
def index(request):
    return render(request, "index.html")


def login_user(request):
    if request.method == "POST":
        # html names username and password
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Redirect to a dashboard/index page if login is successful
            login(request, user)
            return redirect('index')
        else:
            # Alert message if login failed
            messages.success(request, ("Incorrect username or password..."))
            return redirect('login_user')

    else:
        return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect('login_user')

def signup_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        # if registration is successful it will direct to dashboard/index page.
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            # Alert message if registration is succesful
            messages.success(request, ("Registration Successful"))
            return redirect('index')
    else:
        form = RegisterUserForm()

    return render(request, "signup.html", {'form': form})


# CAR PARKING SPACE
def gen(main_app):
    while True:
        frame = main_app.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')




