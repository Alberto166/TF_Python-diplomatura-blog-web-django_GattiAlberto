from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=250, blank=True, null=True)
    contenido = models.TextField()
    # Guardará las imágenes en la carpeta 'media/blog_imagenes/' de forma dinámica
    imagen = models.ImageField(upload_to='blog_imagenes/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f"{self.titulo} | por {self.autor.username}"
