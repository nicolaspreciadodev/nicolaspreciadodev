# usuarios/tests.py
"""Tests de registro de usuarios."""
from django.test import TestCase, Client
from django.urls import reverse
from usuarios.models import CustomUser


class RegistroViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('usuarios:registro')
        self.datos_validos = {
            'username': 'nuevo_user',
            'first_name': 'Juan',
            'last_name': 'Pérez',
            'email': 'juan@test.com',
            'rol': 'DEPORTISTA',
            'password1': 'ClaveSegura123!',
            'password2': 'ClaveSegura123!',
        }

    def test_get_muestra_formulario(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Crear cuenta')

    def test_registro_exitoso_redirige_a_login(self):
        response = self.client.post(self.url, self.datos_validos)
        self.assertRedirects(response, reverse('login'))
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_rol_deportista_se_guarda_correctamente(self):
        self.client.post(self.url, self.datos_validos)
        user = CustomUser.objects.get(username='nuevo_user')
        self.assertEqual(user.rol, 'DEPORTISTA')

    def test_rol_dueño_se_guarda_correctamente(self):
        datos = {**self.datos_validos, 'rol': 'DUEÑO', 'username': 'dueno_user', 'email': 'dueno@test.com'}
        self.client.post(self.url, datos)
        user = CustomUser.objects.get(username='dueno_user')
        self.assertEqual(user.rol, 'DUEÑO')

    def test_email_duplicado_falla(self):
        """Edge case: mismo email no puede registrarse dos veces."""
        self.client.post(self.url, self.datos_validos)
        datos2 = {**self.datos_validos, 'username': 'otro_user'}
        response = self.client.post(self.url, datos2)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertContains(response, 'ya está registrado')

    def test_username_duplicado_falla(self):
        """Edge case: username único."""
        self.client.post(self.url, self.datos_validos)
        datos2 = {**self.datos_validos, 'email': 'otro@test.com'}
        response = self.client.post(self.url, datos2)
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_passwords_no_coinciden_falla(self):
        """Edge case: confirmación de contraseña incorrecta."""
        datos = {**self.datos_validos, 'password2': 'OtraClave456!'}
        response = self.client.post(self.url, datos)
        self.assertEqual(CustomUser.objects.count(), 0)

    def test_campos_requeridos_vacios_falla(self):
        """Edge case: formulario vacío no crea usuario."""
        response = self.client.post(self.url, {})
        self.assertEqual(CustomUser.objects.count(), 0)
