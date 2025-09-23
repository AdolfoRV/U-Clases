from django.utils.translation import gettext_lazy as _

ERROR_MESSAGES = {
    "required": _("Este campo es obligatorio."),
    "invalid_email": _("Introduce un correo electrónico válido."),
    "email_in_use": _("Este correo electrónico ya está en uso."),
    "username_in_use": _("Este nombre de usuario ya está en uso."),
    "pwd_mismatch": _("Las contraseñas no coinciden."),
    "invalid_password": _("El nombre de usuario o la contraseña son incorrectos."),
    "password_confirmation_required": _("Confirma tu contraseña."),
    # Mensajes específicos para la validación de contraseña
    "password_too_similar": _("Tu contraseña no puede ser similar a tu nombre de usuario por seguridad."),
    "password_too_short": _("La contraseña debe tener al menos 8 caracteres."),
    "password_too_common": _("La contraseña es demasiado común, elige una más segura."),
    "password_entirely_numeric": _("La contraseña debe incluir letras y al menos un carácter especial."),
    # Mensajes adicionales de validación
    "password_no_spaces": _("La contraseña no puede contener espacios."),
    "password_no_consecutive": _("La contraseña no puede contener caracteres consecutivos repetidos (ej: 111, aaa)."),
    "password_require_special": _("La contraseña debe contener al menos un carácter especial (!@#$%^&*)."),
    "password_require_number": _("La contraseña debe contener al menos un número."),
    "password_require_uppercase": _("La contraseña debe contener al menos una letra mayúscula."),
    "password_require_lowercase": _("La contraseña debe contener al menos una letra minúscula.")
}