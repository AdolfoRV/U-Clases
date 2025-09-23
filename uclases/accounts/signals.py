from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

#lo dejo para acordarme luego de crear un perfil al crear un usuario
User = settings.AUTH_USER_MODEL