"""Infografías animadas de la semana del 16/11/2026. Ejecutar: python3 animadas.py [02|03]  (OUT=carpeta opcional)"""
import os, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
from kit_animado import *

OUT = os.environ.get("OUT", AQUI)
QUE = sys.argv[1:] or ["02", "03"]
C = COLORES
SOBRE = ('<svg viewBox="0 0 24 18" width="{w}" height="{h}"><rect x="1" y="1" width="22" height="16" rx="3" fill="{c}"/>'
         '<path d="M2 3l10 7 10-7" fill="none" stroke="#0d0f14" stroke-width="2"/></svg>')

# =====================================================================================
# 02 · Cómo reclamar un pago atrasado con IA (versión para quien nunca usó IA)
# =====================================================================================
if "02" in QUE:
    PEDIDO = ("Escribí un mail amable para recordarle a un cliente que tiene una factura vencida hace 10 días. "
              "Que sea corto.")
    RESP = ["Hola [nombre]:", "Te recuerdo que la factura [número] venció el [fecha].",
            "¿Nos confirmás la fecha de pago?", "Saludos."]

    def chatbox(idt, alto=86, ph="Escribí acá, como en WhatsApp…"):
        return (f'<div style="position:absolute;left:16px;right:16px;bottom:16px;min-height:{alto}px;border-radius:20px;background:#232a3a;'
                f'border:2px solid #39425a;padding:12px 64px 12px 16px;font-size:21px;line-height:1.3;font-weight:600;color:#fff">'
                f'<span id="{idt}"></span><span id="{idt}ph" style="color:#7f889c">{ph}</span></div>')

    def enviar(idt):
        return (f'<div id="{idt}" style="position:absolute;right:28px;bottom:28px;width:44px;height:44px;border-radius:50%;background:#3a4258;'
                f'display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:900;color:#0d0f14">↑</div>')

    # 1 · entrar a la página
    v1 = ('<div style="position:absolute;left:0;right:0;top:0;height:58px;background:#e9ecf1;display:flex;align-items:center;gap:8px;padding:0 14px">'
          '<i style="width:12px;height:12px;border-radius:50%;background:#ff5f57"></i><i style="width:12px;height:12px;border-radius:50%;background:#febc2e"></i>'
          '<i style="width:12px;height:12px;border-radius:50%;background:#28c840"></i>'
          '<div style="flex:1;margin-left:8px;height:38px;border-radius:19px;background:#fff;color:#1f2430;font-size:22px;font-weight:700;'
          'display:flex;align-items:center;padding:0 16px"><span id="url"></span><span id="urlc" style="width:2px;height:24px;background:#1f2430;margin-left:2px"></span></div></div>'
          '<div id="pg1" style="position:absolute;left:0;right:0;top:58px;bottom:0">'
          '<div style="position:absolute;left:0;right:0;top:40px;text-align:center;font-size:26px;font-weight:800">¿En qué te ayudo?</div>'
          + chatbox("x1", 60) + "</div>")
    # 2 · escribir el pedido
    v2 = chatbox("x2", 170) + enviar("e2")
    # 3 · enviar y recibir el mail
    v3 = (f'<div id="u3" class="burb" style="right:14px;top:14px;width:300px;background:#2b3245;border-radius:18px 18px 4px 18px;font-size:19px;'
          f'white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{PEDIDO}</div>'
          '<div id="r3" class="burb" style="left:14px;top:64px;right:14px;background:#1c2230;border:1px solid #303850;border-radius:18px 18px 18px 4px;'
          'font-size:19px;line-height:1.3">'
          + "".join(f'<div id="rl{k}" style="margin-top:{0 if k == 0 else 6}px">{t}</div>' for k, t in enumerate(RESP))
          + '<div id="cp" style="display:inline-block;margin-top:10px;padding:6px 12px;border-radius:8px;background:#2a3142;font-size:18px;font-weight:800">Copiar</div></div>'
          + CURSOR.format(id="cu3"))
    # 4 · pegarlo en el mail y completar
    v4 = ('<div style="position:absolute;inset:0;background:#fff;color:#1f2430">'
          '<div style="height:44px;background:#f2f4f8;display:flex;align-items:center;padding:0 16px;font-size:20px;font-weight:800">Mensaje nuevo</div>'
          '<div style="padding:8px 16px;border-bottom:1px solid #e6e8ec;font-size:20px;color:#6b7280">Para: <b style="color:#1f2430">cliente@empresa.com</b></div>'
          '<div style="padding:10px 16px;font-size:20px;line-height:1.35;font-weight:500" id="cuerpo">'
          '<div id="m0">Hola <span id="f0" class="hueco">[nombre]</span>:</div>'
          '<div id="m1">Te recuerdo que la factura <span id="f1" class="hueco">[número]</span> venció el <span id="f2" class="hueco">[fecha]</span>.</div>'
          '<div id="m2">¿Nos confirmás la fecha de pago?</div></div>'
          f'<div id="env" style="position:absolute;left:16px;bottom:14px;padding:9px 22px;border-radius:20px;background:#0b57d0;color:#fff;font-size:20px;font-weight:800">Enviar</div>'
          f'<div id="ok4" style="position:absolute;right:16px;bottom:20px;font-size:21px;font-weight:800;color:{C[3]}">Enviado ✓</div></div>'
          + CURSOR.format(id="cu4"))

    tarjetas = [
        tarjeta(1, "Entrá a ChatGPT o a Claude", v1, "Escribí <b>chatgpt.com</b> o <b>claude.ai</b> en el navegador. Son gratis.", C[0]),
        tarjeta(2, "Escribí lo que necesitás", v2, "En el cuadro de abajo, <b>como si mandaras un WhatsApp</b>.", C[1]),
        tarjeta(3, "Tocá la flecha y esperá", v3, "Te escribe el mail. Si no te gusta, pedile <b>“más corto”</b>.", C[2]),
        tarjeta(4, "Copialo en tu correo", v4, "Completá <b>nombre, factura y fecha</b> y envialo.", C[3]),
    ]
    html = pieza('Cómo reclamar un pago<br>atrasado <em>con IA</em>', "Aunque nunca la hayas usado. 4 pasos, gratis.",
                 tarjetas, "<b>Ojo:</b> no pongas datos del cliente en el chat.")
    html = html.replace("</div></div></div>", "</div></div></div>", 1)
    css_extra = ".hueco { background:#fde68a; border-radius:5px; padding:0 4px; font-weight:700; }"
    js = f"""
    document.head.insertAdjacentHTML('beforeend', '<style>{css_extra}</style>');
    const PEDIDO = {PEDIDO!r};
    const REAL = ['Juan', '0012', '05/11'];
    const HUECO = ['[nombre]', '[número]', '[fecha]'];
    function frame(t) {{
      const out = 1 - seg(t, .94, 1);
      // 1 · se escribe la dirección y aparece la página
      $('url').textContent = typed('chatgpt.com', seg(t, .03, .2));
      set('urlc', {{opacity: t < .24 && (Math.floor(t*40) % 2 === 0) ? 1 : 0}});
      const p1 = ease(seg(t, .24, .32)) * out;
      set('pg1', {{opacity:p1, transform:`translateY(${{(1-p1)*14}}px)`}});
      // 2 · se escribe el pedido en el cuadro
      const tx = typed(PEDIDO, seg(t, .08, .5));
      $('x2').textContent = tx; set('x2ph', {{display: tx ? 'none' : 'inline'}});
      set('e2', {{background: t > .5 ? '{C[1]}' : '#3a4258', transform:`scale(${{t > .55 && t < .6 ? .85 : 1}})`}});
      set('x2', {{opacity: out}});
      // 3 · llega el mail escrito
      set('u3', {{opacity: seg(t, .1, .14) * out}});
      set('r3', {{opacity: seg(t, .18, .22) * out}});
      for (let k = 0; k < 4; k++) set('rl'+k, {{opacity: seg(t, .22 + .07*k, .27 + .07*k)}});
      const cpOn = t > .62 && t < .7;
      set('cp', {{background: cpOn ? '{C[2]}' : '#2a3142', color: cpOn ? '#0d0f14' : '#fff'}});
      const m3 = ease(seg(t, .5, .62));
      set('cu3', {{left: mix(330, 75, m3) + 'px', top: mix(40, 240, m3) + 'px', opacity: out, transform:`scale(${{cpOn && t < .65 ? .82 : 1}})`}});
      // 4 · se completa y se envía
      for (let k = 0; k < 3; k++) set('m'+k, {{opacity: seg(t, .1 + .05*k, .15 + .05*k) * out}});
      for (let k = 0; k < 3; k++) {{
        const ok = t > .35 + .1*k;
        const f = $('f'+k); f.textContent = ok ? REAL[k] : HUECO[k];
        f.style.background = ok ? '#bbf7d0' : '#fde68a';
      }}
      const m4 = ease(seg(t, .66, .76)); const envOn = t > .76 && t < .84;
      set('cu4', {{left: mix(300, 70, m4) + 'px', top: mix(90, 200, m4) + 'px', opacity: out, transform:`scale(${{envOn && t < .79 ? .82 : 1}})`}});
      set('env', {{background: envOn ? '#0842a0' : '#0b57d0'}});
      set('ok4', {{opacity: seg(t, .8, .84) * out}});
    }}
    """
    render_anim(html, js, f"{OUT}/02_reclamar_pago_con_ia", portada_t=0.86)
