import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from piezas_semana_2026_10_26 import *  # helpers + paleta de Pana


def ip():
    img, d = canvas(NEGRO)
    header(img, d, "Guardá este post", dark=True)
    tracked(d, (M, 214), "CÓDIGO IP", font(22, 500), GRIS_CLARO, 0.2)
    y = title(d, 254, ["IP65 no es sumergible.", "Cómo leer el código."], BLANCO, 66)
    d.rectangle([M, y + 18, M + 70, y + 22], fill=AMARILLO)

    # IP 6 5 desarmado
    cy = y + 70
    big = font(120, 700)
    tight(d, (M, cy), "IP", big, GRIS_CLARO, -0.02)
    x1 = M + d.textlength("IP", font=big) + 40
    tight(d, (x1, cy), "6", big, AMARILLO, 0)
    x2 = x1 + d.textlength("6", font=big) + 60
    tight(d, (x2, cy), "5", big, BLANCO, 0)
    lx = x2 + d.textlength("5", font=big) + 60
    d.text((lx, cy + 22), "1.er dígito: polvo", font=font(28, 600), fill=AMARILLO)
    d.text((lx, cy + 66), "2.º dígito: agua", font=font(28, 600), fill=BLANCO)

    # Tablas
    ty = cy + 180
    colw = (W - 2 * M - 40) // 2
    cols = [
        ("POLVO", AMARILLO, [("5", "Protegido contra el polvo"), ("6", "Hermético al polvo")]),
        ("AGUA", BLANCO, [("4", "Salpicaduras"), ("5", "Chorros de agua"), ("6", "Chorros potentes"),
                          ("7", "Inmersión temporal, hasta 1 m"), ("8", "Inmersión continua")]),
    ]
    for i, (lab, col, rows) in enumerate(cols):
        bx = M + i * (colw + 40)
        tracked(d, (bx, ty), lab, font(20, 600), col, 0.22)
        for j, (n, txt) in enumerate(rows):
            ry = ty + 40 + j * 54
            d.line([(bx, ry), (bx + colw, ry)], fill=GRIS_OSC, width=2)
            d.text((bx, ry + 12), n, font=font(30, 700), fill=col)
            d.text((bx + 44, ry + 16), txt, font=font(23, 400), fill=GRIS_CLARO)
        d.line([(bx, ty + 40 + len(rows) * 54), (bx + colw, ty + 40 + len(rows) * 54)], fill=GRIS_OSC, width=2)
        if i == 0:
            para(d, (bx, ty + 40 + 2 * 54 + 34),
                 "A la intemperie, buscá un 5 o un 6 en el primer dígito. Si aparece una X (IPX4), ese dato no se ensayó.",
                 font(22, 400), GRIS_CLARO, colw - 10, 1.35)

    # Guía de uso
    gy = ty + 40 + 5 * 54 + 50
    d.rectangle([0, gy, W, H], fill=HUESO)
    tracked(d, (M, gy + 40), "¿CUÁL VA EN CADA LUGAR?", font(20, 600), (176, 140, 0), 0.22)
    guide = [("IP20", "Interior seco"), ("IP44", "Galerías y aleros"), ("IP65", "Intemperie"),
             ("IP67", "Estacas de jardín"), ("IP68", "Piletas y fuentes")]
    cw = (W - 2 * M) / 5
    for k, (code, use) in enumerate(guide):
        gx = M + k * cw
        tight(d, (gx, gy + 84), code, font(34, 700), NEGRO, -0.02)
        para(d, (gx, gy + 132), use, font(21, 400), GRIS, cw - 14, 1.25)
    d.line([(M, H - 104), (W - M, H - 104)], fill=GRIS_CLARO, width=2)
    d.text((M, H - 68), "Pana Iluminación", font=font(24, 600), fill=NEGRO)
    tracked(d, (W - M, H - 66), "CONSULTANOS →", font(22, 600), NEGRO, 0.18, anchor="right")
    save(img, "02b_codigo_ip.png")


if __name__ == "__main__":
    ip()
