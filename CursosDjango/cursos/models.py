from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField("Nombre del Curso", max_length=50)
    descripcion = models.TextField("Descripción", blank=True, null=True)
    duracion_horas = models.PositiveIntegerField("Duración (horas)")
    precio = models.DecimalField("Precio", max_digits=8, decimal_places=2)
    activo = models.BooleanField("Curso activo", default=True)
    categoria = models.CharField("Categoría", max_length=50, default="General")
    imagen = models.ImageField("Imagen", upload_to="cursos/", blank=True, null=True)
    fecha_creacion = models.DateTimeField("Fecha de creación", auto_now_add=True)

    def __str__(self):
        return self.nombre
    
class Actividad(models.Model):
    clave=models.AutoField(primary_key=True,verbose_name="Clave")
    curso=models.ForeignKey(Curso,
                            on_delete=models.CASCADE,verbose_name="Curso")
    descripcion=models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    act=RichTextField(verbose_name="Actividad")

    class Meta:
        verbose_name="Actividad"
        verbose_name_plural="Actividades"
        ordering=["-created"]

    def __str__(self):
        return self.act

