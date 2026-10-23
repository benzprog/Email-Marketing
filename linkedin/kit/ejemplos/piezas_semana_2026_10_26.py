import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # kit/
from PIL import Image, ImageDraw
from pana_style import *

OUT = os.path.dirname(os.path.abspath(__file__))
GRIS_OSC = (40, 40, 40)      # líneas sobre negro
AMARILLO_SUAVE = (255, 236, 168)


def title(d, y, lines, color, size=72):
    f = font(size, 700)
    for i, ln in enumerate(lines):
        tight(d, (M, y + i * int(size * 1.12)), ln, f, color, -0.03)
    return y + len(lines) * int(size * 1.12)


def para(d, xy, text, fnt, fill, max_w, lh=1.35):
    x, y = xy
    for ln in wrap(d, text, fnt, max_w):
        d.text((x, y), ln, font=fnt, fill=fill)
        y += int(fnt.size * lh)
    return y


def bottom_band(d, top, text, dark_bg=True, cta=True):
    d.rectangle([0, top, W, H], fill=NEGRO)
    y = para(d, (M, top + 44), text, font(30, 500), BLANCO, W - 2 * M, 1.38)
    if cta:
        tracked(d, (W - M, H - 66), "CONSULTANOS →", font(22, 600), AMARILLO, 0.18, anchor="right")
        d.text((M, H - 68), "Pana Iluminación", font=font(24, 600), fill=GRIS_CLARO)


def save(img, name):
    p = os.path.join(OUT, name)
    img.save(p, "PNG", optimize=True)
    print(name, os.path.getsize(p))


# ---------------------------------------------------------------- 01 IRC
def irc():
    img, d = canvas(HUESO)
    header(img, d, "Especificación")
    tracked(d, (M, 214), "ÍNDICE DE REPRODUCCIÓN CROMÁTICA", font(22, 500), GRIS, 0.2)
    y = title(d, 254, ["El número que casi", "nadie mira: el IRC."], NEGRO, 70)
    d.rectangle([M, y + 18, M + 70, y + 22], fill=AMARILLO)

    # Muestras de color de prueba (aproximadas)
    tcs = [(181, 143, 139), (158, 154, 100), (139, 167, 90), (115, 169, 138),
           (120, 169, 181), (129, 151, 200), (163, 141, 191), (187, 139, 170)]
    r9 = (181, 33, 42)
    sy = y + 70
    sw, gap = 82, 10
    for i, c in enumerate(tcs):
        x = M + i * (sw + gap)
        d.rectangle([x, sy, x + sw, sy + sw], fill=c)
        d.text((x + 8, sy + sw + 10), f"R{i+1}", font=font(20, 600), fill=GRIS)
    # R9 separado
    x9 = M + 8 * (sw + gap) + 34
    d.rectangle([x9, sy, x9 + sw, sy + sw], fill=r9)
    d.text((x9 + 8, sy + sw + 10), "R9", font=font(20, 700), fill=NEGRO)
    # llave del promedio
    by = sy + sw + 46
    x_end = M + 8 * (sw + gap) - gap
    d.line([(M, by), (x_end, by)], fill=NEGRO, width=2)
    d.line([(M, by - 10), (M, by)], fill=NEGRO, width=2)
    d.line([(x_end, by - 10), (x_end, by)], fill=NEGRO, width=2)
    d.text((M, by + 14), "Ra = promedio de estos 8 colores", font=font(26, 600), fill=NEGRO)
    d.text((x9 - 6, by + 14), "Fuera del", font=font(22, 500), fill=GRIS)
    d.text((x9 - 6, by + 42), "promedio", font=font(22, 500), fill=GRIS)
    d.text((M, by + 86), "Colores de muestra aproximados.", font=font(20, 400), fill=GRIS)

    # Tabla de uso
    ty = by + 140
    rows = [
        ("IRC 80", "Circulaciones, depósitos y la mayoría de las oficinas."),
        ("IRC 90+", "Gastronomía, carnicerías y verdulerías, indumentaria, showrooms y vivienda."),
        ("R9 alto", "Rojos vivos: carnes, frutas y telas. Pedilo en la ficha."),
    ]
    rh = 108
    d.line([(M, ty), (W - M, ty)], fill=NEGRO, width=2)
    for i, (k, v) in enumerate(rows):
        ry = ty + i * rh
        tight(d, (M, ry + 28), k, font(38, 700), NEGRO, -0.02)
        para(d, (M + 230, ry + 28), v, font(26, 400), NEGRO, W - 2 * M - 230, 1.3)
        d.line([(M, ry + rh), (W - M, ry + rh)], fill=GRIS_CLARO if i < 2 else NEGRO, width=2)
    bottom_band(d, ty + 3 * rh + 44,
                "Antes de especificar, pedí la ficha técnica completa. Si no informa el IRC, desconfiá.")
    save(img, "01_irc.png")


# ------------------------------------------------------- 03 Dicroica 12 V
def dicroica():
    img, d = canvas(NEGRO)
    header(img, d, "Diagnóstico", dark=True)
    tracked(d, (M, 214), "SISTEMA 12 V", font(22, 500), GRIS_CLARO, 0.2)
    y = title(d, 254, ["¿Tu dicroica LED titila?", "Casi nunca es la lámpara."], BLANCO, 64)
    d.rectangle([M, y + 18, M + 70, y + 22], fill=AMARILLO)

    # Medidor de carga
    gy = y + 76
    d.text((M, gy), "Carga sobre un transformador electrónico para halógenas",
           font=font(25, 500), fill=GRIS_CLARO)
    bar_l, bar_r = M, W - M
    scale = (bar_r - bar_l) / 55.0  # 0 a 55 W
    rows = [("Dicroica halógena", 50, BLANCO, "50 W"), ("Dicroica LED", 5, AMARILLO, "5 W")]
    for i, (lab, w, col, txt) in enumerate(rows):
        ry = gy + 56 + i * 92
        d.text((bar_l, ry), lab, font=font(24, 500), fill=BLANCO)
        d.rectangle([bar_l, ry + 38, bar_r, ry + 64], fill=GRIS_OSC)
        d.rectangle([bar_l, ry + 38, bar_l + w * scale, ry + 64], fill=col)
        tw = d.textlength(txt, font=font(24, 700))
        d.text((bar_r - tw, ry), txt, font=font(24, 700), fill=col)
    # zona de carga mínima (sin valor numérico: depende del equipo)
    zx = bar_l + 18 * scale
    top_y, bot_y = gy + 56 + 30, gy + 56 + 92 + 72
    for yy in range(top_y, bot_y, 14):
        d.line([(zx, yy), (zx, yy + 7)], fill=AMARILLO, width=3)
    d.text((zx + 12, bot_y + 4), "Carga mínima del transformador (varía según el equipo)",
           font=font(21, 500), fill=AMARILLO)

    # Antes / Solución
    cy = bot_y + 84
    colw = (W - 2 * M - 30) // 2
    boxes = [
        ("ANTES", "Transformador electrónico + MR16 LED",
         ["Queda por debajo de la carga mínima", "Titileo o encendido intermitente", "Zumbido"], GRIS_CLARO, "x"),
        ("SOLUCIÓN", "Fuente switching 12 V de tensión continua",
         ["Alimentación estable", "Sin parpadeo", "Más vida útil"], AMARILLO, "ok"),
    ]
    for i, (lab, head, items, col, mark) in enumerate(boxes):
        bx = M + i * (colw + 30)
        d.rounded_rectangle([bx, cy, bx + colw, cy + 372], radius=4,
                            outline=col if i else GRIS_OSC, width=2, fill=NEGRO)
        tracked(d, (bx + 30, cy + 34), lab, font(20, 600), col, 0.22)
        yy = para(d, (bx + 30, cy + 74), head, font(28, 600), BLANCO, colw - 60, 1.25)
        for it in items:
            mx, my = bx + 32, yy + 30
            if mark == "x":
                d.line([(mx, my - 8), (mx + 16, my + 8)], fill=col, width=3)
                d.line([(mx, my + 8), (mx + 16, my - 8)], fill=col, width=3)
            else:
                d.line([(mx, my), (mx + 6, my + 7), (mx + 18, my - 9)], fill=col, width=3, joint="curve")
            yy = para(d, (bx + 64, yy + 18), it, font(23, 400), GRIS_CLARO, colw - 94, 1.25)
            yy += 6
    # pie
    fy = H - 112
    d.line([(M, fy), (W - M, fy)], fill=GRIS_OSC, width=2)
    d.text((M, fy + 36), "En Pana: MR16 LED 12 V · 5 W + fuente switching 12 V",
           font=font(24, 500), fill=BLANCO)
    tracked(d, (W - M, fy + 38), "CONSULTANOS →", font(22, 600), AMARILLO, 0.18, anchor="right")
    save(img, "03_dicroica_12v.png")


# ------------------------------------------------------------- 05 Dimmer
def wave(d, x, y, w, h, cut, color, base):
    """Media onda senoidal con el tramo conducido relleno.
    cut='leading': conduce desde 1/3 hasta el final. 'trailing': desde el inicio hasta 2/3."""
    pts = []
    n = 60
    for i in range(n + 1):
        t = i / n
        pts.append((x + t * w, y + h - math.sin(math.pi * t) * h))
    d.line(pts, fill=base, width=3)
    lo, hi = (1 / 3, 1.0) if cut == "leading" else (0.0, 2 / 3)
    poly = [(x + lo * w, y + h)]
    for i in range(n + 1):
        t = lo + (hi - lo) * i / n
        poly.append((x + t * w, y + h - math.sin(math.pi * t) * h))
    poly.append((x + hi * w, y + h))
    d.polygon(poly, fill=color)
    d.line([(x - 6, y + h), (x + w + 6, y + h)], fill=base, width=2)


def dimmer():
    img, d = canvas(HUESO)
    header(img, d, "Guía rápida")
    tracked(d, (M, 214), "DIMMER + LED", font(22, 500), GRIS, 0.2)
    y = title(d, 254, ["3 chequeos antes de", "regular una LED."], NEGRO, 70)
    d.rectangle([M, y + 18, M + 70, y + 22], fill=AMARILLO)

    sy = y + 64
    num_f = font(26, 700)

    def step(n, yy, head, body):
        d.line([(M, yy), (W - M, yy)], fill=GRIS_CLARO, width=2)
        d.text((M, yy + 26), n, font=num_f, fill=(176, 140, 0))
        d.text((M + 60, yy + 22), head, font=font(32, 700), fill=NEGRO)
        return para(d, (M + 60, yy + 68), body, font(25, 400), GRIS, W - 2 * M - 60, 1.32)

    e = step("01", sy, "¿La lámpara dice “dimerizable”?",
             "Una LED común en un circuito con dimmer puede fallar antes de tiempo.")
    e = step("02", e + 24, "¿Qué tipo de dimmer es?",
             "Lo que regula es qué parte de cada media onda le llega a la lámpara.")
    # ondas
    wy = e + 20
    ww, wh = 300, 110
    for i, (cut, lab, sub, col) in enumerate([
        ("leading", "Corte al inicio", "Dimmer clásico: suele fallar con LED", GRIS_CLARO),
        ("trailing", "Corte al final", "Dimmer para LED: el recomendado", AMARILLO),
    ]):
        wx = M + 60 + i * (ww + 120)
        wave(d, wx, wy, ww, wh, cut, col, NEGRO)
        d.text((wx, wy + wh + 16), lab, font=font(25, 700), fill=NEGRO)
        d.text((wx, wy + wh + 50), sub, font=font(21, 400), fill=GRIS)
    e = step("03", wy + wh + 100, "¿Llegás a la carga mínima del dimmer?",
             "Muchos dimmers piden una potencia mínima conectada:")
    # comparación de carga
    cy = e + 14
    d.text((M + 60, cy), "3 × 50 W halógena = 150 W", font=font(26, 500), fill=GRIS)
    d.text((M + 60, cy + 40), "3 × 5 W LED = 15 W", font=font(26, 700), fill=NEGRO)
    d.text((M + 400, cy + 40), "→ puede quedar por debajo", font=font(26, 500), fill=NEGRO)
    bottom_band(d, cy + 100, "Compatibles entre sí: regulación suave, sin zumbido.")
    save(img, "05_dimmer.png")


# --------------------------------------------------------------- 07 L70
def l70():
    img, d = canvas(NEGRO)
    header(img, d, "Especificación", dark=True)
    tracked(d, (M, 214), "VIDA ÚTIL LED", font(22, 500), GRIS_CLARO, 0.2)
    y = title(d, 254, ["50.000 horas no es", "cuando se apaga."], BLANCO, 70)
    d.rectangle([M, y + 18, M + 70, y + 22], fill=AMARILLO)

    # gráfico
    gx0, gx1 = M + 70, W - M - 10
    gy0, gy1 = y + 80, y + 430  # arriba / abajo
    tmax = 60000
    def px(t): return gx0 + (gx1 - gx0) * t / tmax
    def py(v): return gy1 - (gy1 - gy0) * (v - 50) / 50  # eje de 50% a 100%
    # grilla
    for v in (100, 90, 80, 70, 60, 50):
        d.line([(gx0, py(v)), (gx1, py(v))], fill=GRIS_OSC, width=1)
        lab = f"{v}%"
        d.text((gx0 - 16 - d.textlength(lab, font=font(20, 500)), py(v) - 12), lab,
               font=font(20, 500), fill=GRIS_CLARO)
    for t in (0, 10000, 20000, 30000, 40000, 50000, 60000):
        lab = f"{t//1000}k"
        d.text((px(t) - d.textlength(lab, font=font(20, 500)) / 2, gy1 + 12), lab,
               font=font(20, 500), fill=GRIS_CLARO)
    d.text((gx1 - d.textlength("horas", font=font(20, 500)), gy1 + 42), "horas",
           font=font(20, 500), fill=GRIS_CLARO)
    # curva ilustrativa
    k = math.log(1 / 0.7) / 50000
    pts = [(px(t), py(100 * math.exp(-k * t))) for t in range(0, tmax + 1, 500)]
    d.line(pts, fill=BLANCO, width=5)
    # marca L70
    xL, yL = px(50000), py(70)
    for xx in range(int(gx0), int(xL), 16):
        d.line([(xx, yL), (xx + 8, yL)], fill=AMARILLO, width=2)
    for yy in range(int(yL), int(gy1), 16):
        d.line([(xL, yy), (xL, yy + 8)], fill=AMARILLO, width=2)
    d.ellipse([xL - 11, yL - 11, xL + 11, yL + 11], fill=AMARILLO)
    lx = xL - 290
    tracked(d, (lx, yL + 22), "L70 · 50.000 h", font(24, 700), AMARILLO, 0.06)
    d.text((lx, yL + 56), "Sigue encendida,", font=font(22, 500), fill=BLANCO)
    d.text((lx, yL + 84), "con 30% menos de luz", font=font(22, 500), fill=BLANCO)
    d.text((gx0, gy1 + 42), "Curva ilustrativa.", font=font(20, 400), fill=GRIS_CLARO)

    # definiciones
    dy = gy1 + 110
    defs = [
        ("L70", "Horas hasta que la luz cae al 70% de la inicial. L80 es más exigente."),
        ("B50", "La mitad de las unidades puede estar por debajo de ese valor. B10: solo el 10%."),
        ("Calor", "Lo que más acorta la vida real: artefactos cerrados y drivers sin ventilación."),
    ]
    for i, (k_, v) in enumerate(defs):
        ry = dy + i * 92
        d.line([(M, ry), (W - M, ry)], fill=GRIS_OSC, width=2)
        tight(d, (M, ry + 24), k_, font(32, 700), AMARILLO if i < 2 else BLANCO, -0.01)
        para(d, (M + 150, ry + 24), v, font(24, 400), GRIS_CLARO, W - 2 * M - 150, 1.3)
    d.line([(M, dy + 3 * 92), (W - M, dy + 3 * 92)], fill=GRIS_OSC, width=2)
    tracked(d, (W - M, H - 66), "CONSULTANOS →", font(22, 600), AMARILLO, 0.18, anchor="right")
    d.text((M, H - 68), "Pana Iluminación", font=font(24, 600), fill=GRIS_CLARO)
    save(img, "07_l70.png")


# ------------------------------------------------------ 09 Ángulo apertura
def angulo():
    img, d = canvas(HUESO)
    header(img, d, "Guardá este post")
    tracked(d, (M, 214), "ÁNGULO DE APERTURA", font(22, 500), GRIS, 0.2)
    y = title(d, 254, ["Mismo spot, misma altura.", "Otro resultado."], NEGRO, 64)
    d.rectangle([M, y + 18, M + 70, y + 22], fill=AMARILLO)

    s = 100  # px por metro
    h_m = 2.5
    top = y + 90
    ceil_y = top
    floor_y = top + h_m * s
    left = M + 70
    colw = (W - M - left) / 3
    d.line([(left - 10, ceil_y), (W - M, ceil_y)], fill=NEGRO, width=3)
    d.line([(left - 10, floor_y), (W - M, floor_y)], fill=GRIS_CLARO, width=2)
    # cota 2,5 m
    cx = M + 20
    d.line([(cx, ceil_y), (cx, floor_y)], fill=GRIS, width=2)
    for yy in (ceil_y, floor_y):
        d.line([(cx - 8, yy), (cx + 8, yy)], fill=GRIS, width=2)
    lab = Image.new("RGBA", (120, 40), (0, 0, 0, 0))
    ImageDraw.Draw(lab).text((0, 0), "2,5 m", font=font(22, 600), fill=GRIS)
    lab = lab.rotate(90, expand=True)
    img.paste(lab, (int(cx - 34), int((ceil_y + floor_y) / 2 - 30)), lab)

    data = [(24, "Acento"), (36, "Dirigida"), (60, "General")]
    for i, (ang, uso) in enumerate(data):
        xc = left + colw * (i + 0.5)
        diam = 2 * h_m * math.tan(math.radians(ang / 2))
        half = diam * s / 2
        cone = Image.new("RGBA", img.size, (0, 0, 0, 0))
        cd = ImageDraw.Draw(cone)
        cd.polygon([(xc, ceil_y + 14), (xc - half, floor_y), (xc + half, floor_y)],
                   fill=AMARILLO + (95,))
        img.paste(cone, (0, 0), cone)
        d = ImageDraw.Draw(img)
        d.rectangle([xc - 16, ceil_y, xc + 16, ceil_y + 16], fill=NEGRO)
        d.line([(xc - half, floor_y), (xc + half, floor_y)], fill=NEGRO, width=5)
        ty = floor_y + 34
        big = f"{ang}°"
        tight(d, (xc - d.textlength(big, font=font(56, 700)) / 2, ty), big, font(56, 700), NEGRO, -0.02)
        dm = f"Ø {diam:.2f} m".replace(".", ",")
        d.text((xc - d.textlength(dm, font=font(28, 600)) / 2, ty + 74), dm, font=font(28, 600), fill=NEGRO)
        d.text((xc - d.textlength(uso, font=font(24, 400)) / 2, ty + 114), uso, font=font(24, 400), fill=GRIS)

    band = floor_y + 34 + 180
    d.rectangle([0, band, W, H], fill=NEGRO)
    tracked(d, (M, band + 44), "LA CUENTA", font(20, 600), AMARILLO, 0.22)
    d.text((M, band + 82), "Ø = 2 × distancia × tan(ángulo ÷ 2)", font=font(34, 600), fill=BLANCO)
    para(d, (M, band + 140), "El ángulo se mide hasta donde la intensidad cae a la mitad. Un ángulo cerrado no da más luz: la concentra.",
         font(24, 400), GRIS_CLARO, W - 2 * M, 1.35)
    d.line([(M, H - 112), (W - M, H - 112)], fill=GRIS_OSC, width=2)
    tracked(d, (W - M, H - 66), "CONSULTANOS →", font(22, 600), AMARILLO, 0.18, anchor="right")
    d.text((M, H - 68), "Pana Iluminación", font=font(24, 600), fill=GRIS_CLARO)
    save(img, "09_angulo_apertura.png")


# ------------------------------------------------------------ 04 PstLM / SVM
def pstlm():
    img, d = canvas(HUESO)
    header(img, d, "Criterio técnico")
    tracked(d, (M, 214), "ESTABILIDAD DE LA LUZ", font(22, 500), GRIS, 0.2)
    y = title(d, 254, ["Dos datos que casi nadie", "pide en la ficha técnica."], NEGRO, 64)
    d.rectangle([M, y + 18, M + 70, y + 22], fill=AMARILLO)
    d.text((M, y + 42), "Dicen si una luz LED es estable de verdad, aunque a simple vista no se note.",
           font=font(26, 400), fill=GRIS)

    cy = y + 96
    ch = 480
    colw = (W - 2 * M - 30) // 2
    cards = [
        ("PstLM", "Parpadeo perceptible",
         "Mide las variaciones lentas de la luz, las que el ojo llega a ver como parpadeo.",
         "Referencia UE: ≤ 1,0"),
        ("SVM", "Efecto estroboscópico",
         "Mide las variaciones rápidas: no se ven, pero aparecen cuando algo se mueve.",
         "Referencia UE: ≤ 0,4"),
    ]
    for i, (name, sub, body, ref) in enumerate(cards):
        bx = M + i * (colw + 30)
        d.rectangle([bx, cy, bx + colw, cy + ch], fill=BLANCO)
        d.rectangle([bx, cy, bx + colw, cy + 4], fill=NEGRO)
        tight(d, (bx + 32, cy + 30), name, font(54, 700), NEGRO, -0.02)
        d.text((bx + 32, cy + 98), sub, font=font(27, 600), fill=NEGRO)
        para(d, (bx + 32, cy + 142), body, font(22, 400), GRIS, colw - 64, 1.32)
        vx, vy, vw = bx + 32, cy + 262, colw - 64
        if i == 0:
            # variación lenta y amplia
            pts = [(vx + t, vy + 50 - 34 * math.sin(2 * math.pi * 2.2 * t / vw)) for t in range(0, vw + 1, 3)]
            d.line([(vx, vy + 50), (vx + vw, vy + 50)], fill=GRIS_CLARO, width=2)
            d.line(pts, fill=NEGRO, width=4)
            d.text((vx, vy + 98), "Lenta: se ve como parpadeo", font=font(19, 500), fill=GRIS)
        else:
            # objeto en movimiento: trazo continuo vs copias separadas
            d.text((vx, vy - 4), "Luz estable", font=font(19, 500), fill=GRIS)
            d.rounded_rectangle([vx + 150, vy, vx + vw, vy + 16], radius=8, fill=NEGRO)
            d.text((vx, vy + 50), "SVM alto", font=font(19, 500), fill=GRIS)
            n = 8
            step = (vw - 150 - 16) / (n - 1)
            for k in range(n):
                cx = vx + 150 + k * step
                d.ellipse([cx, vy + 52, cx + 16, vy + 68], fill=NEGRO)
            d.text((vx, vy + 98), "El movimiento se ve “partido”", font=font(19, 500), fill=GRIS)
        # referencia
        pw = d.textlength(ref, font=font(22, 600)) + 32
        d.rectangle([bx + 32, cy + ch - 66, bx + 32 + pw, cy + ch - 22], fill=AMARILLO)
        d.text((bx + 48, cy + ch - 58), ref, font=font(22, 600), fill=NEGRO)

    # insight
    iy = cy + ch + 24
    d.rectangle([M, iy, W - M, iy + 110], fill=NEGRO)
    d.rectangle([M, iy, M + 8, iy + 110], fill=AMARILLO)
    para(d, (M + 36, iy + 20), "Una lámpara puede tener PstLM bajo y SVM alto: a la vista no parpadea, pero el efecto aparece con máquinas que giran.",
         font(25, 500), BLANCO, W - 2 * M - 64, 1.32)

    # cierre
    fy = iy + 110 + 34
    tracked(d, (M, fy), "ANTES DE ESPECIFICAR", font(20, 600), (176, 140, 0), 0.22)
    tight(d, (M, fy + 34), "Pedí PstLM y SVM al proveedor.", font(36, 700), NEGRO, -0.02)
    d.line([(M, H - 104), (W - M, H - 104)], fill=GRIS_CLARO, width=2)
    d.text((M, H - 68), "Referencia: Reglamento (UE) 2019/2020", font=font(21, 400), fill=GRIS)
    tracked(d, (W - M, H - 66), "CONSULTANOS →", font(22, 600), NEGRO, 0.18, anchor="right")
    save(img, "04_pstlm_svm.png")


if __name__ == "__main__":
    which = sys.argv[1:] or ["irc", "dicroica", "dimmer", "l70", "angulo"]
    for w in which:
        globals()[w]()
