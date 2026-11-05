"""Arma un carrusel (documento PDF) para LinkedIn a partir de láminas 1080 x 1350.

Uso:
    from carrusel import exportar
    exportar([img1, img2, ...], "semana-AAAA-MM-DD/01_tema.pdf")

- Cada lámina es una imagen PIL de 1080 x 1350 (usar canvas() y header() de pana_style).
- Guarda el PDF y, al lado, la portada en JPG (..._portada.jpg) para usar como miniatura
  (thumbnailUrl) al programar el documento en Buffer.
- Recomendado: 6 a 9 láminas. Lámina 1 = gancho (una frase grande), última = cierre con
  pregunta o "Guardalo para la próxima obra" + CONSULTANOS.
"""
import os
from PIL import Image


def exportar(laminas, ruta_pdf):
    laminas = [im.convert("RGB") for im in laminas]
    for im in laminas:
        assert im.size == (1080, 1350), f"lámina de {im.size}, tiene que ser 1080 x 1350"
    os.makedirs(os.path.dirname(os.path.abspath(ruta_pdf)), exist_ok=True)
    # 1080 px a 150 ppp = 7,2 pulgadas: el PDF pesa poco y se ve nítido en el feed
    laminas[0].save(ruta_pdf, "PDF", save_all=True, append_images=laminas[1:], resolution=150)
    portada = os.path.splitext(ruta_pdf)[0] + "_portada.jpg"
    laminas[0].save(portada, "JPEG", quality=88, optimize=True)
    print(ruta_pdf, os.path.getsize(ruta_pdf), "bytes,", len(laminas), "láminas")
    return ruta_pdf, portada
