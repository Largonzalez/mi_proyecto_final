
from django.shortcuts import render
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required


from . forms import EditFullUser, NuestraCreacionUser
from .models import Avatar

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
    if request.method == 'POST':
        form=EditFullUser(request.POST)

        if form.is_valid():

            data= form.cleaned_data

            logued_user = request.user
            logued_user.email = data.get('email')
            logued_user.first_name = data.get('first_name', '')
            logued_user.last_name = data.get('last_name', '')
            if data.get('password1') == data.get('password2') and len(data.get('password1')) > 8:
                logued_user.set_password(data.get('password1'))
            else:
                msj = 'No se modifico el password.'
            
            logued_user.save()  
            return render(request, 'accounts/index.html', {'msj': 'Se modificó el user con éxito!', 'user_avatar_url': buscar_url_avatar(request.user)})
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
    return render(request, 'accounts/editar_usuario.html', {'form': form})



def buscar_url_avatar(user):
    return Avatar.objects.filter(user=user)[0].imagen.url



