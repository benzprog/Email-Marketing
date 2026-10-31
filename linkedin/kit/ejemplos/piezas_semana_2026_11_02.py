import os, sys
KIT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, KIT)
from PIL import Image, ImageDraw
from pana_style import *

OUT = os.path.join(os.path.dirname(KIT), "semana-2026-11-02")
os.makedirs(OUT, exist_ok=True)
GRIS_OSC = (48, 48, 48)

def dots(d, x, y, dark=False, r=6, step=26):
    for i in range(8):
        cx = x + r + i * step
        col = AMARILLO if i == 7 else ((255, 255, 255, 150) if dark else (60, 60, 60))
        d.ellipse([cx - r, y - r, cx + r, y + r], fill=col)

def title(d, y, lines, color, size=70):
    f = font(size, 700)
    for i, ln in enumerate(lines):
        tight(d, (M, y + i * int(size * 1.1)), ln, f, color, -0.03)
    return y + len(lines) * int(size * 1.1)

def para(d, xy, text, fnt, fill, max_w, lh=1.35):
    x, y = xy
    for ln in wrap(d, text, fnt, max_w):
        d.text((x, y), ln, font=fnt, fill=fill)
        y += int(fnt.size * lh)
    return y

def footer(d, dark):
    line = GRIS_OSC if dark else GRIS_CLARO
    d.line([(M, H - 110), (W - M, H - 110)], fill=line, width=2)
    d.text((M, H - 74), "Pana Iluminación", font=font(24, 600), fill=GRIS_CLARO if dark else NEGRO)
    s = "CONSULTANOS →"
    f = font(22, 600)
    # sin tracking para no sumar etiquetas espaciadas; ancho manual
    d.text((W - M - d.textlength(s, font=f), H - 72), s, font=f, fill=AMARILLO if dark else NEGRO)

def save(img, name):
    p = os.path.join(OUT, name)
    img = img.convert("RGB")
    if name.endswith(".jpg"):
        img.save(p, "JPEG", quality=90, optimize=True, progressive=True)
    else:
        q = img.quantize(colors=96, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
        q.save(p, "PNG", optimize=True)
    print(name, os.path.getsize(p), Image.open(p).size)

# ------------------------------------------------ Lunes: cable fuente-tira
def cable():
    img, d = canvas(NEGRO)
    header(img, d, "Cálculo en obra", dark=True)
    d.text((M, 214), "Del tablero a la tira", font=font(26, 500), fill=AMARILLO)
    y = title(d, 256, ["El cable también", "consume voltios."], BLANCO, 72)
    dots(d, M, y + 34, dark=True)
    d.text((M, y + 74), "Mismos 120 W, mismo cable: 10 m de 1,5 mm² (ida y vuelta: 20 m de cobre).",
           font=font(25, 400), fill=GRIS_CLARO)
    # barras a escala: 0..24 V
    bx0, bx1 = M, W - M
    sc = (bx1 - bx0) / 24.0
    rows = [("Sistema 24 V  ·  5 A", 24, 1.15, "llegan 22,9 V", "pierde 4,8 %"),
            ("Sistema 12 V  ·  10 A", 12, 2.30, "llegan 9,7 V", "pierde 19 %")]
    ry = y + 170
    for lab, v, dv, ok, loss in rows:
        d.text((bx0, ry), lab, font=font(30, 700), fill=BLANCO)
        top = ry + 54
        d.rectangle([bx0, top, bx0 + (v - dv) * sc, top + 70], fill=BLANCO)
        d.rectangle([bx0 + (v - dv) * sc, top, bx0 + v * sc, top + 70], fill=AMARILLO)
        d.text((bx0, top + 86), ok, font=font(26, 500), fill=GRIS_CLARO)
        lf = font(26, 700)
        d.text((bx0 + v * sc - d.textlength(loss, font=lf), top + 86), loss, font=lf, fill=AMARILLO)
        ry = top + 170
    # escala
    for v in (0, 6, 12, 18, 24):
        x = bx0 + v * sc
        d.line([(x, ry - 6), (x, ry + 6)], fill=GRIS, width=2)
        t = f"{v} V"; f = font(20, 500)
        tx = min(max(x - d.textlength(t, font=f) / 2, bx0), bx1 - d.textlength(t, font=f))
        d.text((tx, ry + 14), t, font=f, fill=GRIS)
    d.line([(bx0, ry), (bx1, ry)], fill=GRIS, width=2)
    # leyenda
    ly = ry + 70
    d.rectangle([M, ly + 4, M + 22, ly + 26], fill=AMARILLO)
    d.text((M + 36, ly), "Lo que se queda en el cable", font=font(24, 500), fill=BLANCO)
    para(d, (M, ly + 60), "A igual potencia, 12 V lleva el doble de corriente: el cable pierde el doble de voltios y, en proporción, cuatro veces más.",
         font(27, 500), BLANCO, W - 2 * M, 1.35)
    footer(d, True)
    save(img, "01_seccion_cable.png")

# ------------------------------------------------ Martes: MacAdam
def macadam():
    img, d = canvas(HUESO)
    header(img, d, "Consistencia de color")
    d.text((M, 214), "Pasos MacAdam (SDCM)", font=font(26, 500), fill=GRIS)
    y = title(d, 256, ["Mismo pedido,", "¿mismo blanco?"], NEGRO, 74)
    dots(d, M, y + 34)
    # elipses concéntricas a escala relativa 1:3:6
    cx, cy = W // 2, y + 250
    a1, b1 = 50, 20
    for n, col, wdt in ((6, GRIS, 3), (3, NEGRO, 4), (1, AMARILLO, 0)):
        a, b = a1 * n, b1 * n
        box = [cx - a, cy - b, cx + a, cy + b]
        if wdt:
            d.ellipse(box, outline=col, width=wdt)
        else:
            d.ellipse(box, fill=col)
    # leyenda en tres columnas
    ly = cy + 6 * b1 + 60
    colw = (W - 2 * M) // 3
    items = [("1 paso", "No se ve diferencia", "fill", AMARILLO),
             ("3 pasos", "Apenas perceptible", "line", NEGRO),
             ("6 pasos", "Máximo que admite la UE", "line", GRIS)]
    for i, (t, sub, kind, col) in enumerate(items):
        x = M + i * colw
        if kind == "fill":
            d.ellipse([x, ly + 4, x + 44, ly + 24], fill=col)
        else:
            d.ellipse([x, ly + 4, x + 44, ly + 24], outline=col, width=3)
        d.text((x + 58, ly), t, font=font(26, 700), fill=NEGRO)
        d.text((x, ly + 42), sub, font=font(21, 400), fill=GRIS)
    d.text((M, ly + 100), "Elipses a escala entre sí: cada paso agranda la elipse en la misma proporción.",
           font=font(20, 400), fill=GRIS)
    cy = ly - 200
    # caja inferior
    by = ly + 160
    d.rectangle([0, by, W, H], fill=NEGRO)
    para(d, (M, by + 48), "Desde 4 pasos la diferencia se nota a simple vista: dos lámparas \"iguales\", dos blancos distintos.",
         font(30, 600), BLANCO, W - 2 * M, 1.35)
    d.text((M, by + 150), "Pedí el dato en la ficha. Referencias: Reglamento (UE) 2019/2020 y ERCO.",
           font=font(22, 400), fill=GRIS_CLARO)
    d.line([(M, H - 110), (W - M, H - 110)], fill=GRIS_OSC, width=2)
    d.text((M, H - 74), "Pana Iluminación", font=font(24, 600), fill=GRIS_CLARO)
    s = "CONSULTANOS →"; f = font(22, 600)
    d.text((W - M - d.textlength(s, font=f), H - 72), s, font=f, fill=AMARILLO)
    save(img, "02_pasos_macadam.png")

# ------------------------------------------------ Miércoles: lm/W
def eficacia():
    img, d = canvas(NEGRO)
    header(img, d, "Eficacia", dark=True)
    d.text((M, 214), "Etiqueta energética de la UE para fuentes de luz", font=font(26, 500), fill=AMARILLO)
    big = font(250, 800)
    tight(d, (M - 8, 250), "210", big, BLANCO, -0.04)
    d.text((M + 520, 330), "lm/W", font=font(64, 700), fill=AMARILLO)
    d.text((M + 520, 410), "para ser clase A", font=font(30, 500), fill=GRIS_CLARO)
    # escala a lo largo de 0..240 lm/W
    y0 = 600
    x0, x1 = M, W - M
    sc = (x1 - x0) / 240.0
    cl = [("G", 0, 85), ("F", 85, 110), ("E", 110, 135), ("D", 135, 160), ("C", 160, 185), ("B", 185, 210), ("A", 210, 240)]
    for i, (k, a, b) in enumerate(cl):
        col = AMARILLO if k == "A" else (GRIS_OSC if i % 2 == 0 else (70, 70, 70))
        d.rectangle([x0 + a * sc, y0, x0 + b * sc - 2, y0 + 64], fill=col)
        f = font(28, 700)
        cxm = x0 + (a + b) / 2 * sc
        d.text((cxm - d.textlength(k, font=f) / 2, y0 + 14), k, font=f, fill=NEGRO if k == "A" else BLANCO)
    for v in (85, 110, 135, 160, 185, 210):
        x = x0 + v * sc
        t = str(v); f = font(18, 500)
        d.text((x - d.textlength(t, font=f) / 2, y0 + 76), t, font=f, fill=GRIS_CLARO)
    d.text((x0, y0 + 76), "0", font=font(18, 500), fill=GRIS_CLARO)
    # ejemplo
    ey = y0 + 150
    d.text((M, ey), "Dos lámparas de 9 W:", font=font(30, 700), fill=BLANCO)
    ex = [("806 lm", 806 / 9, "90 lm/W · clase F"), ("1055 lm", 1055 / 9, "117 lm/W · clase E")]
    for j, (lm, eff, txt) in enumerate(ex):
        yy = ey + 60 + j * 110
        d.text((M, yy), lm, font=font(26, 700), fill=BLANCO)
        d.text((M + 150, yy), txt, font=font(26, 400), fill=GRIS_CLARO)
        d.rectangle([x0, yy + 44, x0 + eff * sc, yy + 72], fill=AMARILLO if j else GRIS_CLARO)
    para(d, (M, ey + 300), "Mismos watts, 30 % más de luz. Compará lúmenes por watt, no watts.",
         font(32, 700), BLANCO, W - 2 * M, 1.3)
    d.text((M, ey + 405), "En lámparas que van directo a 220 V, la eficacia es lúmenes ÷ watts.",
           font=font(22, 400), fill=GRIS_CLARO)
    d.text((M, ey + 437), "Clases según el Reglamento (UE) 2019/2015.", font=font(22, 400), fill=GRIS_CLARO)
    footer(d, True)
    save(img, "03_eficacia_lmw.png")

# ------------------------------------------------ Jueves: método de lúmenes
def lumenes():
    img, d = canvas(HUESO)
    header(img, d, "Cálculo rápido")
    d.text((M, 214), "Método de los lúmenes", font=font(26, 500), fill=GRIS)
    y = title(d, 256, ["¿Cuántas luminarias", "lleva una oficina?"], NEGRO, 68)
    dots(d, M, y + 34)
    # fórmula
    fy = y + 100
    f1 = font(40, 700)
    d.text((M, fy), "N =", font=f1, fill=NEGRO)
    nx = M + d.textlength("N = ", font=f1)
    num = "500 lx × 48 m²"; den = "5000 lm × 0,6 × 0,8"
    fw = max(d.textlength(num, font=font(34, 600)), d.textlength(den, font=font(34, 600)))
    d.text((nx, fy - 26), num, font=font(34, 600), fill=NEGRO)
    d.line([(nx, fy + 24), (nx + fw, fy + 24)], fill=NEGRO, width=3)
    d.text((nx, fy + 32), den, font=font(34, 600), fill=NEGRO)
    d.text((nx + fw + 24, fy), "= 10", font=f1, fill=NEGRO)
    # leyenda
    ly = fy + 112
    leg = [("500 lx", "nivel de referencia para escribir y leer (EN 12464-1)"),
           ("0,6", "factor de utilización (depende del local y la luminaria)"),
           ("0,8", "factor de mantenimiento (polvo y pérdida de flujo)")]
    for i, (k, v) in enumerate(leg):
        d.text((M, ly + i * 40), k, font=font(23, 700), fill=NEGRO)
        d.text((M + 110, ly + i * 40), v, font=font(23, 400), fill=GRIS)
    # plano a escala 8 x 6 m
    py = ly + 150
    pw = 560; s = pw / 8.0; ph = 6 * s
    px = (W - pw) // 2 + 120
    d.rectangle([px, py, px + pw, py + ph], outline=NEGRO, width=4, fill=BLANCO)
    for i in range(5):
        for j in range(2):
            cx = px + (i + 0.5) * 8 / 5 * s
            cy = py + (j + 0.5) * 6 / 2 * s
            d.rectangle([cx - 21, cy - 21, cx + 21, cy + 21], fill=AMARILLO, outline=NEGRO, width=2)
    d.text((px + pw / 2 - 25, py + ph + 12), "8 m", font=font(22, 600), fill=NEGRO)
    d.text((px - 60, py + ph / 2 - 12), "6 m", font=font(22, 600), fill=NEGRO)
    d.text((M, py + 20), "10", font=font(110, 800), fill=NEGRO)
    d.text((M, py + 140), "luminarias de", font=font(24, 500), fill=GRIS)
    d.text((M, py + 172), "5000 lm", font=font(24, 700), fill=NEGRO)
    d.text((M, py + ph - 40), "Ubicación a escala:", font=font(20, 400), fill=GRIS)
    d.text((M, py + ph - 12), "1,6 m × 3 m entre centros.", font=font(20, 400), fill=GRIS)
    footer(d, False)
    save(img, "04_metodo_lumenes.png")

# ------------------------------------------------ Viernes: luz de acento (foto)
def acento():
    ph = Image.open(os.path.join(KIT, "fotos", "comedor_colgante.png")).convert("RGB")
    scale = max(W / ph.width, H / ph.height)
    ph = ph.resize((round(ph.width * scale), round(ph.height * scale)), Image.LANCZOS)
    x0 = (ph.width - W) // 2
    ph = ph.crop((x0, 0, x0 + W, H))
    veil = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    vd = ImageDraw.Draw(veil)
    for yy in range(H):
        a = 0
        if yy < 300:
            a = int(150 * (1 - yy / 300) ** 1.6)
        if yy > 520:
            t = (yy - 520) / (H - 520)
            a = max(a, int(245 * min(1, t ** 1.1 * 1.3)))
        vd.line([(0, yy), (W, yy)], fill=(10, 10, 10, a))
    img = Image.alpha_composite(ph.convert("RGBA"), veil)
    d = ImageDraw.Draw(img)
    lg = logo("blanco", 210)
    img.paste(lg, (M, 78), lg)
    tracked(d, (W - M, 98), "LUZ DE ACENTO", font(20, 500), (230, 228, 224), tracking=0.22, anchor="right")
    tight(d, (M - 6, 760), "10:1", font(230, 800), BLANCO, -0.04)
    dots(d, M, 1010, dark=True)
    d.text((M, 1040), "Para que la luz de acento se note,", font=font(40, 700), fill=BLANCO)
    d.text((M, 1090), "el objeto necesita unas diez veces", font=font(40, 700), fill=BLANCO)
    d.text((M, 1140), "más luz que su entorno.", font=font(40, 700), fill=BLANCO)
    d.text((M, 1205), "Con 2:1 casi no se distingue.", font=font(26, 500), fill=AMARILLO)
    d.line([(M, H - 92), (W - M, H - 92)], fill=(78, 76, 73), width=1)
    d.text((M, H - 66), "Pana Iluminación", font=font(24, 600), fill=(225, 223, 219))
    s = "CONSULTANOS →"; f = font(22, 600)
    d.text((W - M - d.textlength(s, font=f), H - 64), s, font=f, fill=AMARILLO)
    save(img, "05_luz_acento.jpg")

for fn in (cable, macadam, eficacia, lumenes, acento):
    fn()
