# usuarios/views.py
"""Vistas de gestión de usuarios: registro."""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegistroUsuarioForm


class RegistroView:
    """Vista basada en función para el registro de nuevos usuarios.

    Flujo:
        GET  → muestra el formulario vacío.
        POST → valida, crea el usuario y redirige al login con mensaje.

    No usa auto-login post-registro: el usuario debe autenticarse
    manualmente para mayor seguridad y claridad del flujo.
    """

    @staticmethod
    def get(request):
        return render(request, 'registration/register.html', {
            'form': RegistroUsuarioForm()
        })

    @staticmethod
    def post(request):
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                '¡Cuenta creada exitosamente! Inicia sesión para continuar.'
            )
            return redirect('login')

        return render(request, 'registration/register.html', {'form': form})


def registro(request):
    """Entry point de la vista de registro (compatible con urls.py funcional)."""
    view = RegistroView()
    if request.method == 'POST':
        return view.post(request)
    return view.get(request)
