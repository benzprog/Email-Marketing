import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PIL import Image, ImageDraw
from pana_style import font, logo, tight, tracked, W, H, M, AMARILLO, BLANCO

FOTO = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "fotos", "frente_apliques_noche.png")
OUT = "pana_quienes_somos.jpg"

# Foto a sangre, 1080 x 1350
ph = Image.open(FOTO).convert("RGB")
scale = max(W / ph.width, H / ph.height)
ph = ph.resize((round(ph.width * scale), round(ph.height * scale)), Image.LANCZOS)
x0 = (ph.width - W) // 2
ph = ph.crop((x0, 0, x0 + W, H))

# Velos: arriba para el logo, abajo para el texto
veil = Image.new("RGBA", (W, H), (0, 0, 0, 0))
vd = ImageDraw.Draw(veil)
for y in range(H):
    a = 0
    if y < 300:
        a = int(140 * (1 - y / 300) ** 1.6)
    if y > 560:
        t = (y - 560) / (H - 560)
        a = max(a, int(242 * min(1, t ** 1.15 * 1.25)))
    vd.line([(0, y), (W, y)], fill=(10, 10, 10, a))
img = Image.alpha_composite(ph.convert("RGBA"), veil)
d = ImageDraw.Draw(img)

# Logo
lg = logo("blanco", 250)
img.paste(lg, (M, 76), lg)

# Puntos del logo como recurso: 8 puntos, el último amarillo
dy = 872
for i in range(8):
    cx = M + 7 + i * 26
    col = AMARILLO if i == 7 else (255, 255, 255, 150)
    d.ellipse([cx - 6, dy - 6, cx + 6, dy + 6], fill=col)

d.text((M, 904), "Especialistas en iluminación LED", font=font(26, 500), fill=AMARILLO)
hf = font(76, 700)
tight(d, (M, 948), "Luz bien elegida,", hf, BLANCO, -0.035)
tight(d, (M, 1032), "obra bien terminada.", hf, BLANCO, -0.035)
d.text((M, 1140), "Venta minorista y mayorista, cotizaciones para obra", font=font(26, 400), fill=(225, 223, 219))
d.text((M, 1176), "y envíos a todo el país.", font=font(26, 400), fill=(225, 223, 219))

# Marcas y contacto
d.line([(M, 1240), (W - M, 1240)], fill=(78, 76, 73), width=1)
tracked(d, (M, 1270), "TENARUZ  ·  TREFI  ·  TBCIN  ·  VONDERK  ·  MAXILED", font(18, 500),
        (200, 198, 194), tracking=0.16)
num = "11 6288-3659"
nf = font(24, 700)
d.text((W - M - d.textlength(num, font=nf), 1265), num, font=nf, fill=BLANCO)

img.convert("RGB").save(OUT, "JPEG", quality=90, optimize=True, progressive=True)
print("ok", OUT, os.path.getsize(OUT))
