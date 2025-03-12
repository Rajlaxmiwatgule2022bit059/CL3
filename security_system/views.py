from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import User, Visitor, Incident, AccessLog

# views.py

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'security_system/login.html', {'error': 'Invalid credentials'})
    return render(request, 'security_system/login.html')

# Register View
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        user = User.objects.create_user(username=username, password=password, role=role)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'security_system/register.html')

# Dashboard View
@login_required
def dashboard_view(request):
    return render(request, 'security_system/dashboard.html')

# Visitor Management Views
@login_required
def visitor_list(request):
    visitors = Visitor.objects.all()
    return render(request, 'security_system/visitors.html', {'visitors': visitors})

@login_required
def visitor_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        purpose = request.POST['purpose']
        Visitor.objects.create(name=name, phone=phone, purpose=purpose)
        return redirect('visitor_list')
    return render(request, 'security_system/visitor_form.html')

@login_required
def visitor_update(request, pk):
    visitor = Visitor.objects.get(pk=pk)
    if request.method == 'POST':
        visitor.name = request.POST['name']
        visitor.phone = request.POST['phone']
        visitor.purpose = request.POST['purpose']
        visitor.save()
        return redirect('visitor_list')
    return render(request, 'security_system/visitor_form.html', {'visitor': visitor})

@login_required
def visitor_delete(request, pk):
    visitor = Visitor.objects.get(pk=pk)
    visitor.delete()
    return redirect('visitor_list')

# Incident Reporting Views
@login_required
def report_incident(request):
    if request.method == 'POST':
        description = request.POST['description']
        Incident.objects.create(reported_by=request.user, description=description)
        return redirect('incident_list')
    return render(request, 'security_system/inciform.html')

@login_required
def incident_list(request):
    incidents = Incident.objects.all()
    return render(request, 'security_system/incident.html', {'incidents': incidents})

# Access Logs Views
@login_required
def log_access(request):
    area = request.GET.get('area', 'Unknown Area')
    AccessLog.objects.create(user=request.user, area_accessed=area)
    return JsonResponse({'message': 'Access logged successfully!'})

@login_required
def access_logs(request):
    logs = AccessLog.objects.all()
    return render(request, 'security_system/access_logs.html', {'logs': logs})
