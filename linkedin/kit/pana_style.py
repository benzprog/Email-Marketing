"""Kit visual de Pana Iluminación para piezas de LinkedIn (1080 x 1350).

Tomado del paquete de contenido de Pana: fondo hueso o negro, amarillo de
acento, tipografía Archivo, etiquetas en mayúsculas espaciadas.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, "fonts", "Archivo-VF.ttf")

W, H = 1080, 1350
M = 80  # margen lateral

# Paleta (muestreada del PDF de identidad)
HUESO = (244, 243, 241)
NEGRO = (19, 19, 19)
GRIS = (92, 89, 85)
GRIS_CLARO = (214, 211, 207)
AMARILLO = (255, 206, 31)
BLANCO = (255, 255, 255)

_font_cache = {}


def font(size, weight=400, width=100):
    key = (size, weight, width)
    if key not in _font_cache:
        f = ImageFont.truetype(FONT, size)
        f.set_variation_by_axes([weight, width])
        _font_cache[key] = f
    return _font_cache[key]


def logo(variant="negro", width=230):
    im = Image.open(os.path.join(HERE, f"logo_{variant}.png")).convert("RGBA")
    h = round(im.height * width / im.width)
    return im.resize((width, h), Image.LANCZOS)


def tracked(draw, xy, text, fnt, fill, tracking=0.18, anchor="left"):
    """Texto en mayúsculas con espaciado entre letras (estilo etiquetas de Pana)."""
    sp = fnt.size * tracking
    total = sum(draw.textlength(c, font=fnt) for c in text) + sp * (len(text) - 1)
    x, y = xy
    if anchor == "right":
        x -= total
    for c in text:
        draw.text((x, y), c, font=fnt, fill=fill)
        x += draw.textlength(c, font=fnt) + sp
    return total


def tight(draw, xy, text, fnt, fill, tracking=-0.02):
    """Titulares con interletrado apretado, como en las piezas de Pana."""
    sp = fnt.size * tracking
    x, y = xy
    for c in text:
        draw.text((x, y), c, font=fnt, fill=fill)
        x += draw.textlength(c, font=fnt) + sp
    return x - xy[0]


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=fnt) <= max_w:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def canvas(bg=HUESO):
    img = Image.new("RGB", (W, H), bg)
    return img, ImageDraw.Draw(img)


def header(img, draw, label, dark=False):
    lg = logo("blanco" if dark else "negro", 210)
    img.paste(lg, (M, 78), lg)
    tracked(draw, (W - M, 98), label.upper(), font(20, 500), GRIS_CLARO if dark else GRIS,
            tracking=0.22, anchor="right")
