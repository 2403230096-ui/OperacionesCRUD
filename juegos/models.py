from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Juego(models.Model):
    titulo = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    plataforma = models.CharField(max_length=60)
    genero = models.CharField(max_length=60, blank=True)
    anio_lanzamiento = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1950), MaxValueValidator(2100)]
    )
    completado = models.BooleanField(default=False)
    calificacion = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creado_en", "-id"]

    def __str__(self):
        return f"{self.titulo} ({self.plataforma})"
