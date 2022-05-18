
from django.shortcuts import render
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required


from . forms import EditFullUser, NuestraCreacionUser
from .models import Avatar, UserExtension

# Create your views here.

def index(request):
    return render(request, "accounts/index.html", {'user_avatar_url': buscar_url_avatar})


def about(request):
    nombre= f'Hola!  soy Lara González.'


    intro= ' Tengo 26 años, soy abogada y me especializo en derecho corporativo'


    return render (request,"accounts/about.html")


def login (request):
        if request.method== 'POST':
            form= AuthenticationForm(request, data=request.POST)

            if form.is_valid():
                username= form.cleaned_data['username']
                password= form.cleaned_data['password']

                user = authenticate(username=username, password=password)

                if user is not None:
                    django_login(request, user)
                    return render(request, 'accounts/index.html', {'msj': 'Te logueaste con éxito!'})
                    
                else:
                    return render(request, 'accounts/login.html', {'form': form, 'msj':'No se autenticó'})  
            else:
                return render(request, 'accounts/login.html', {'form': form,'msj': 'Formulario con datos incorrectos'})  
        else:
            form = AuthenticationForm()
            return render(request, 'accounts/login.html', {'form': form, 'msj': ''})
        


def registrar(request):

    if request.method == 'POST':
        form=NuestraCreacionUser(request.POST)

        if form.is_valid():
            username= form.cleaned_data['username']
            form.save()
            return render(request, 'accounts/index.html', {'msj': f'Se creo el user {username}'} )
        else:
          return render(request, 'accounts/registrar.html', {'form': form, 'msj': ''})  

    form= NuestraCreacionUser()
    return render(request, 'accounts/registrar.html', {'form': form, 'msj': ''})

@login_required
def editar(request):
    msj= ''
    user_extension_logued, _ = UserExtension.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = EditFullUser(request.POST, request.FILES)
        if form.is_valid():

            request.user.email = form.cleaned_data['email']
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            user_extension_logued.avatar = form.cleaned_data['avatar']
            user_extension_logued.link = form.cleaned_data['link']
            user_extension_logued.more_description = form.cleaned_data['more_description']
            
            if form.cleaned_data['password1'] != '' and form.cleaned_data['password1'] == form.cleaned_data['password2']:
                request.user.set_password(form.cleaned_data['password1'])
            
            request.user.save()
            user_extension_logued.save()
            
            return render(request, 'accounts/index.html', {'msj': 'Se modificó el user con éxito!'})
        else:   
            return render(request, 'accounts/editar_user.html', {'form': form, 'msj': '', 'user_avatar_url': buscar_url_avatar(request.user)})
        
    form = EditFullUser(
    initial={
            'email': request.user.email,
            'password1': '',
            'password2': '',
            'first_name': request.user.first_name,
            'last_name': request.user.last_name, 
            'avatar': user_extension_logued.avatar,
            'link': user_extension_logued.link,
            'more_description': user_extension_logued.more_description
        }
    )
    return render(request, 'accounts/editar_user.html', {'form': form})



def buscar_url_avatar(user):
    return Avatar.objects.filter(user=user)[0].imagen.url


@login_required
def usuario_datos(request):
    
    mas_datos, _ =UserExtension.objects.get_or_create(user=request.user)
    return render(request, "accounts/usuario_datos.html", {"mas_datos": mas_datos})


