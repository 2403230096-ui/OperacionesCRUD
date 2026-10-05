from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Juego


class JuegoCRUDTests(APITestCase):
    def setUp(self):
        self.datos = {
            "titulo": "The Legend of Zelda: Ocarina of Time",
            "plataforma": "Nintendo 64",
            "genero": "Aventura",
            "anio_lanzamiento": 1998,
            "completado": True,
            "calificacion": "10.0",
        }
        self.juego = Juego.objects.create(
            titulo="Mega Man ZX", plataforma="Nintendo DS",
            genero="Acción", anio_lanzamiento=2006,
        )
        self.url_lista = reverse("juego-lista")
        self.url_detalle = reverse("juego-detalle", args=[self.juego.pk])

    # ---------- CREATE ----------
    def test_crear_juego(self):
        r = self.client.post(self.url_lista, self.datos, format="json")
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Juego.objects.count(), 2)
        self.assertEqual(r.data["titulo"], self.datos["titulo"])
        self.assertIn("id", r.data)

    def test_crear_sin_titulo_falla(self):
        self.datos.pop("titulo")
        r = self.client.post(self.url_lista, self.datos, format="json")
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("titulo", r.data)

    def test_crear_con_calificacion_invalida_falla(self):
        self.datos["calificacion"] = "11"
        r = self.client.post(self.url_lista, self.datos, format="json")
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("calificacion", r.data)

    def test_crear_titulo_en_blanco_falla(self):
        self.datos["titulo"] = "   "
        r = self.client.post(self.url_lista, self.datos, format="json")
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)

    # ---------- READ ----------
    def test_listar_juegos(self):
        r = self.client.get(self.url_lista)
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(len(r.data), 1)

    def test_detalle_juego(self):
        r = self.client.get(self.url_detalle)
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(r.data["titulo"], "Mega Man ZX")

    def test_detalle_inexistente_404(self):
        r = self.client.get(reverse("juego-detalle", args=[9999]))
        self.assertEqual(r.status_code, status.HTTP_404_NOT_FOUND)

    # ---------- UPDATE ----------
    def test_actualizar_put(self):
        r = self.client.put(self.url_detalle, self.datos, format="json")
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.juego.refresh_from_db()
        self.assertEqual(self.juego.titulo, self.datos["titulo"])
        self.assertTrue(self.juego.completado)

    def test_actualizar_patch(self):
        r = self.client.patch(self.url_detalle, {"completado": True}, format="json")
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.juego.refresh_from_db()
        self.assertTrue(self.juego.completado)
        self.assertEqual(self.juego.titulo, "Mega Man ZX")  # no cambió

    def test_actualizar_con_datos_invalidos_falla(self):
        r = self.client.patch(self.url_detalle, {"anio_lanzamiento": 1800}, format="json")
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)

    def test_actualizar_inexistente_404(self):
        r = self.client.put(reverse("juego-detalle", args=[9999]), self.datos, format="json")
        self.assertEqual(r.status_code, status.HTTP_404_NOT_FOUND)

    # ---------- DELETE ----------
    def test_eliminar_juego(self):
        r = self.client.delete(self.url_detalle)
        self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Juego.objects.filter(pk=self.juego.pk).exists())

    def test_eliminar_inexistente_404(self):
        r = self.client.delete(reverse("juego-detalle", args=[9999]))
        self.assertEqual(r.status_code, status.HTTP_404_NOT_FOUND)
