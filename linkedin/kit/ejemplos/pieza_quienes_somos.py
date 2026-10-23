import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from piezas_semana_2026_10_26 import *  # helpers + paleta de Pana


def quienes():
    img, d = canvas(NEGRO)
    lg = logo("amarillo", 300)
    img.paste(lg, (M, 80), lg)
    tracked(d, (W - M, 112), "QUIÉNES SOMOS", font(20, 500), GRIS_CLARO, 0.22, anchor="right")

    y = title(d, 250, ["Especialistas en", "iluminación LED."], BLANCO, 72)
    d.rectangle([M, y + 18, M + 70, y + 22], fill=AMARILLO)
    para(d, (M, y + 44), "Acompañamos proyectos de vivienda, comercio, obra y alumbrado público, desde la consulta hasta la entrega.",
         font(27, 400), GRIS_CLARO, W - 2 * M, 1.35)

    # Qué hacemos / Para quién
    sy = y + 170
    colw = (W - 2 * M - 40) // 2
    blocks = [
        ("QUÉ HACEMOS", ["Venta minorista y mayorista", "Cotizaciones para obras y proyectos",
                         "Asesoramiento técnico", "Envíos a todo el país"]),
        ("PARA QUIÉN", ["Casas de electricidad y distribuidores", "Constructoras y obra",
                        "Estudios y comercios", "Municipios"]),
    ]
    for i, (lab, items) in enumerate(blocks):
        bx = M + i * (colw + 40)
        tracked(d, (bx, sy), lab, font(20, 600), AMARILLO, 0.22)
        yy = sy + 40
        for it in items:
            d.line([(bx, yy), (bx + colw, yy)], fill=GRIS_OSC, width=2)
            yy = para(d, (bx, yy + 14), it, font(24, 500), BLANCO, colw, 1.25) + 12
        d.line([(bx, yy), (bx + colw, yy)], fill=GRIS_OSC, width=2)

    # Marcas
    my = sy + 40 + 4 * 66 + 46
    d.rectangle([0, my, W, H], fill=HUESO)
    tracked(d, (M, my + 40), "MARCAS QUE TRABAJAMOS", font(20, 600), (176, 140, 0), 0.22)
    brands = [("Tenaruz", "Línea LED"), ("TREFI", "Lámparas LED"), ("TBCIN", "Tubos LED T8"),
              ("Vonderk", "Spots empotrables"), ("MAXILED", "Alumbrado público")]
    cw = (W - 2 * M) / 5
    for k, (b, sub) in enumerate(brands):
        bx = M + k * cw
        tight(d, (bx, my + 82), b, font(30, 700), NEGRO, -0.02)
        para(d, (bx, my + 124), sub, font(20, 400), GRIS, cw - 12, 1.25)

    # Destacado + contacto
    hy = my + 236
    d.rectangle([M, hy, M + 12, hy + 12], fill=AMARILLO)
    d.text((M + 26, hy - 8), "Comercios: compra sin mínimo en toda la línea Tenaruz.", font=font(26, 600), fill=NEGRO)
    d.line([(M, H - 104), (W - M, H - 104)], fill=GRIS_CLARO, width=2)
    d.text((M, H - 70), "11 6288-3659", font=font(28, 700), fill=NEGRO)
    tracked(d, (W - M, H - 66), "CONSULTANOS →", font(22, 600), NEGRO, 0.18, anchor="right")
    save(img, "pana_quienes_somos.png")


if __name__ == "__main__":
    quienes()
