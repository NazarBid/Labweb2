from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Agent, Property, Client, Request, CustomUser
from .forms import AgentForm, PropertyForm, ClientForm, RequestForm, CustomUserCreationForm


# Agent views---------------------------------------------------------
@login_required
def agent_list(request):
    if request.method == 'GET' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        agents = list(Agent.objects.all().values())
        return JsonResponse({'agents': agents})
    else:
        agents = Agent.objects.all()
        return render(request, 'agent_list.html', {'agents': agents})

@login_required
def agent_detail(request, id):
    if request.method == 'GET' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        agent = get_object_or_404(Agent, pk=id)
        agent_data = {'first_name': agent.first_name, 'last_name': agent.last_name, 'specialty': agent.specialty}
        return JsonResponse({'agent': agent_data})
    else:
        agent = get_object_or_404(Agent, pk=id)
        return render(request, 'agent_detail.html', {'agent': agent})

@login_required
def agent_create(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = AgentForm(request.POST)
        if form.is_valid():
            agent = form.save()
            return JsonResponse({'status': 'success', 'agent_id': agent.pk})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else:
        form = AgentForm()
        return render(request, 'agent_create.html', {'form': form})

@login_required
def agent_update(request, id):
    agent = get_object_or_404(Agent, pk=id)
    if request.method == 'POST':
        form = AgentForm(request.POST, instance=agent)
        if form.is_valid():
            form.save()
            return redirect('agent_list')
    else:
        form = AgentForm(instance=agent)
    return render(request, 'agent_form.html', {'form': form})


@login_required
def agent_delete(request, id):
    agent = get_object_or_404(Agent, pk=id)
    agent.delete()
    return redirect('agent_list')
   

# Property views---------------------------------------------------------
@login_required
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties})

@login_required
def property_detail(request, id):
    property = get_object_or_404(Property, pk=id)
    return render(request, 'property_detail.html', {'property': property})

@login_required
def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'property_form.html', {'form': form})

@login_required
def property_update(request, id):
    property = get_object_or_404(Property, pk=id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'property_form.html', {'form': form})

@login_required
def property_delete(request, id):
    property = get_object_or_404(Property, pk=id)
    property.delete()
    return redirect('property_list')

# Client views---------------------------------------------------------
@login_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

@login_required
def client_detail(request, id):
    client = get_object_or_404(Client, pk=id)
    return render(request, 'client_detail.html', {'client': client})

@login_required
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

@login_required
def client_update(request, id):
    client = get_object_or_404(Client, pk=id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form': form})

@login_required
def client_delete(request, id):
    client = get_object_or_404(Client, pk=id)
    client.delete()
    return redirect('client_list')

# Request views---------------------------------------------------------
@login_required
def request_list(request):
    requests = Request.objects.all()
    return render(request, 'request_list.html', {'requests': requests})

@login_required
def request_detail(request, id):
    request_obj = get_object_or_404(Request, pk=id)
    return render(request, 'request_detail.html', {'request': request_obj})

@login_required
def request_create(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_list')
    else:
        form = RequestForm()
    return render(request, 'request_form.html', {'form': form})

@login_required
def request_update(request, id):
    request_obj = get_object_or_404(Request, pk=id)
    if request.method == 'POST':
        form = RequestForm(request.POST, instance=request_obj)
        if form.is_valid():
            form.save()
            return redirect('request_list')
    else:
        form = RequestForm(instance=request_obj)
    return render(request, 'request_form.html', {'form': form})

@login_required
def request_delete(request, id):
    request_obj = get_object_or_404(Request, pk=id)
    request_obj.delete()
    return redirect('request_list')


#login view-----------------------------------------------------
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    user = request.user
    logout(request)
    return render(request, 'logout.html')

@login_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

@login_required
def user_create(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_create.html', {'form': form})

@login_required
def user_detail(request, pk):
    user = CustomUser.objects.get(pk=pk)
    return render(request, 'user_detail.html', {'user': user})

@login_required
def user_edit(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserCreationForm(instance=user)
    return render(request, 'user_edit.html', {'form': form})

@login_required
def user_delete(request, pk):
    user = CustomUser.objects.get(pk=pk)
    user.delete()
    return redirect('user_list')