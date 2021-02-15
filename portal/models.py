from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Lugar(models.Model):
    departamento = models.CharField(max_length=50, null=False)
    ciudad = models.CharField(max_length=50, null=False)

    class Meta:
        verbose_name_plural = "Lugares"

    def __str__(self) -> str:
        return f'{self.departamento}, {self.ciudad}'


class Deportista(models.Model):
    user = models.OneToOneField(to=User,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                verbose_name='Usuario')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    peso = models.FloatField(validators=[MinValueValidator(0.0)],
                             help_text='Peso del Deportista')
    estatura = models.FloatField(validators=[MinValueValidator(0.0)],
                                 help_text='Estatura del Deportista')
    entrenador = models.CharField(max_length=128,
                                  help_text='Entrenador del Deportista')
    imagen = models.ImageField('Uploaded image')
    lugar_nacimiento = models.ForeignKey(to=Lugar, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Deportistas'

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'


class UsuarioRegistrado(models.Model):
    user = models.OneToOneField(to=User,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                verbose_name='Usuario')
    email = models.EmailField(help_text='Correo electrónico del Usuario')

    class Meta:
        verbose_name_plural = 'Usuarios Registrados'

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'


class Deporte(models.Model):
    nombre = models.CharField(max_length=220)
    descripcion = models.CharField(max_length=220)
    tipo = models.CharField(max_length=220)
    icono = models.CharField(max_length=220)

    class Meta:
        verbose_name_plural = 'Deportes'

    def __str__(self) -> str:
        return self.nombre


class Participacion(models.Model):
    fecha = models.DateField(verbose_name='Fecha')
    hora = models.TimeField(verbose_name='Hora')
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    deportista = models.ForeignKey(Deportista, on_delete=models.CASCADE)
    modalidad = models.CharField(max_length=220)
    resultado = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Participaciones'

    def __str__(self) -> str:
        return f'{self.deporte} - {self.deportista}'


class Video(models.Model):
    url = models.URLField(verbose_name="Video", help_text="URL del video")
    participacion = models.OneToOneField(Participacion,
                                         on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Videos"

    def __str__(self) -> str:
        return self.url


class Comentario(models.Model):
    texto = models.CharField(max_length=1000)
    usuario_registrado = models.ForeignKey(UsuarioRegistrado,
                                           on_delete=models.CASCADE)
    fecha = models.DateTimeField(null=False)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Comentarios"

    def __str__(self) -> str:
        return f'{self.usuario_registrado} ({self.fecha})'
