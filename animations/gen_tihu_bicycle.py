"""生成「醍醐骑自行车」SVG 动画：python3 gen_tihu_bicycle.py > tihu_bicycle.svg"""
import math

FRAMES = 48
CRANK = (390, 300)
CRANK_LEN = 26
HIP = (366, 206)
THIGH, SHIN = 64, 62
PEDAL_DUR = "0.9s"


def knee(hip, foot):
    """两段腿的逆运动学，取膝盖朝前（+x）的解。"""
    dx, dy = foot[0] - hip[0], foot[1] - hip[1]
    d = min(math.hypot(dx, dy), THIGH + SHIN - 0.01)
    a = (THIGH ** 2 - SHIN ** 2 + d ** 2) / (2 * d)
    h = math.sqrt(max(THIGH ** 2 - a ** 2, 0))
    ux, uy = dx / d, dy / d
    mx, my = hip[0] + a * ux, hip[1] + a * uy
    k1 = (mx - h * uy, my + h * ux)
    k2 = (mx + h * uy, my - h * ux)
    return k1 if k1[0] > k2[0] else k2


def leg_frames(phase):
    legs, pedals = [], []
    for i in range(FRAMES + 1):
        t = 2 * math.pi * i / FRAMES + phase
        foot = (CRANK[0] + CRANK_LEN * math.cos(t), CRANK[1] + CRANK_LEN * math.sin(t))
        k = knee(HIP, foot)
        legs.append(f"M{HIP[0]},{HIP[1]} L{k[0]:.1f},{k[1]:.1f} L{foot[0]:.1f},{foot[1]:.1f}")
        pedals.append(f"{foot[0] - 9:.1f},{foot[1] - 3:.1f}")
    return ";".join(legs), pedals


def leg_svg(phase, pants, shoe):
    d_values, pedals = leg_frames(phase)
    px = ";".join(p.split(",")[0] for p in pedals)
    py = ";".join(p.split(",")[1] for p in pedals)
    shoe_x = ";".join(f"{float(p.split(',')[0]) - 2:.1f}" for p in pedals)
    shoe_y = ";".join(f"{float(p.split(',')[1]) - 7:.1f}" for p in pedals)
    return f"""
    <path fill="none" stroke="{pants}" stroke-width="15" stroke-linecap="round" stroke-linejoin="round">
      <animate attributeName="d" dur="{PEDAL_DUR}" repeatCount="indefinite" values="{d_values}"/>
    </path>
    <rect width="18" height="6" rx="2" fill="#333">
      <animate attributeName="x" dur="{PEDAL_DUR}" repeatCount="indefinite" values="{px}"/>
      <animate attributeName="y" dur="{PEDAL_DUR}" repeatCount="indefinite" values="{py}"/>
    </rect>
    <rect width="24" height="10" rx="5" fill="{shoe}">
      <animate attributeName="x" dur="{PEDAL_DUR}" repeatCount="indefinite" values="{shoe_x}"/>
      <animate attributeName="y" dur="{PEDAL_DUR}" repeatCount="indefinite" values="{shoe_y}"/>
    </rect>"""


def wheel(cx, cy):
    spokes = "".join(
        f'<line x1="{cx}" y1="{cy}" x2="{cx + 58 * math.cos(math.radians(a)):.1f}" '
        f'y2="{cy + 58 * math.sin(math.radians(a)):.1f}"/>'
        for a in range(0, 360, 30)
    )
    return f"""
    <g>
      <circle cx="{cx}" cy="{cy}" r="62" fill="none" stroke="#2b2b2b" stroke-width="9"/>
      <circle cx="{cx}" cy="{cy}" r="57" fill="none" stroke="#9aa5ad" stroke-width="2"/>
      <g stroke="#c9d1d6" stroke-width="1.6">{spokes}</g>
      <circle cx="{cx}" cy="{cy}" r="6" fill="#555"/>
      <circle cx="{cx + 40}" cy="{cy}" r="3" fill="#ffcf3f"/>
      <animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="0.55s" repeatCount="indefinite"/>
    </g>"""


def tree(x, s=1.0):
    return (
        f'<g transform="translate({x},258) scale({s})">'
        '<rect x="-5" y="-10" width="10" height="34" fill="#8a5a3b"/>'
        '<circle cx="0" cy="-30" r="26" fill="#4caf50"/>'
        '<circle cx="-14" cy="-18" r="18" fill="#43a047"/>'
        '<circle cx="14" cy="-18" r="18" fill="#66bb6a"/>'
        "</g>"
    )


def cloud(x, y, s):
    return (
        f'<g transform="translate({x},{y}) scale({s})" fill="#fff" opacity="0.92">'
        '<ellipse cx="0" cy="0" rx="40" ry="18"/><circle cx="-16" cy="-10" r="18"/>'
        '<circle cx="12" cy="-16" r="22"/></g>'
    )


def scroll(content, width, dur):
    return f"""
  <g>
    <g>{content}</g>
    <g transform="translate({width},0)">{content}</g>
    <animateTransform attributeName="transform" type="translate" from="0 0" to="-{width} 0" dur="{dur}" repeatCount="indefinite"/>
  </g>"""


def main():
    clouds = cloud(80, 70, 1) + cloud(330, 50, 0.7) + cloud(600, 90, 1.2)
    hills = (
        '<path d="M0,250 Q100,150 200,240 T400,230 T600,220 T800,250 L800,300 L0,300 Z" fill="#a5d6a7"/>'
    )
    hills_near = (
        '<path d="M0,265 Q150,200 300,262 T600,255 T800,265 L800,300 L0,300 Z" fill="#81c784"/>'
    )
    trees = tree(60) + tree(240, 0.8) + tree(470, 1.1) + tree(690, 0.9)
    flowers = "".join(
        f'<circle cx="{x}" cy="{y}" r="4" fill="{c}"/>'
        for x, y, c in [(40, 392, "#ff8a80"), (180, 388, "#fff176"), (330, 394, "#f48fb1"),
                        (520, 390, "#ffffff"), (650, 393, "#ffcc80"), (770, 389, "#ce93d8")]
    )
    dashes = "".join(f'<rect x="{x}" y="368" width="40" height="5" rx="2" fill="#fff"/>' for x in range(0, 800, 80))

    far_leg = leg_svg(math.pi, "#1f4e79", "#c0392b")
    near_leg = leg_svg(0, "#2e6da4", "#e74c3c")

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="800" height="420">
  <title>醍醐骑自行车</title>
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#7ec8f2"/>
      <stop offset="1" stop-color="#d9f1ff"/>
    </linearGradient>
  </defs>

  <rect width="800" height="420" fill="url(#sky)"/>
  <g>
    <circle cx="690" cy="70" r="34" fill="#ffd54f"/>
    <circle cx="690" cy="70" r="46" fill="#ffd54f" opacity="0.3">
      <animate attributeName="r" values="42;52;42" dur="3s" repeatCount="indefinite"/>
    </circle>
  </g>
  {scroll(clouds, 800, "40s")}
  {scroll(hills, 800, "24s")}
  {scroll(hills_near, 800, "12s")}
  {scroll(trees, 800, "5s")}
  <rect y="290" width="800" height="130" fill="#7cb342"/>
  <rect y="340" width="800" height="62" fill="#5d5d66"/>
  {scroll(dashes, 800, "2.2s")}
  {scroll(flowers, 800, "2.2s")}

  <!-- 速度线 -->
  <g stroke="#ffffff" stroke-width="3" stroke-linecap="round" opacity="0.8">
    <line x1="150" y1="200" x2="200" y2="200"><animate attributeName="opacity" values="0;1;0" dur="0.8s" repeatCount="indefinite"/></line>
    <line x1="130" y1="240" x2="190" y2="240"><animate attributeName="opacity" values="0;1;0" dur="0.8s" begin="0.3s" repeatCount="indefinite"/></line>
    <line x1="160" y1="160" x2="200" y2="160"><animate attributeName="opacity" values="0;1;0" dur="0.8s" begin="0.5s" repeatCount="indefinite"/></line>
  </g>

  <!-- 整体轻微颠簸 -->
  <g>
    <animateTransform attributeName="transform" type="translate" values="0 0;0 -2;0 0;0 1;0 0" dur="0.45s" repeatCount="indefinite"/>

    <ellipse cx="400" cy="366" rx="150" ry="8" fill="#000" opacity="0.18"/>

    <!-- 小旗：醍醐 -->
    <line x1="282" y1="238" x2="262" y2="120" stroke="#666" stroke-width="3"/>
    <path fill="#ff7043" stroke="#e64a19" stroke-width="1.5">
      <animate attributeName="d" dur="0.6s" repeatCount="indefinite"
        values="M263,122 Q230,118 205,128 Q228,140 268,152 Z;
                M263,122 Q232,128 203,122 Q226,146 268,152 Z;
                M263,122 Q230,118 205,128 Q228,140 268,152 Z"/>
    </path>
    <text x="238" y="141" font-size="15" font-weight="bold" fill="#fff" text-anchor="middle"
      font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" transform="rotate(-6 238 141)">醍醐</text>

    <!-- 远侧腿 -->
    <g opacity="0.85">{far_leg}</g>

    {wheel(290, 300)}
    {wheel(510, 300)}

    <!-- 车架 -->
    <g stroke="#e53935" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none">
      <path d="M290,300 L390,300 L470,200 L362,210 Z"/>
      <path d="M390,300 L356,196"/>
      <path d="M470,200 L510,300"/>
      <path d="M290,300 L362,210"/>
    </g>
    <g stroke="#444" stroke-width="5" stroke-linecap="round" fill="none">
      <path d="M470,200 L475,180 Q478,170 492,172"/>
      <path d="M282,238 L330,238" stroke-width="4"/>
    </g>
    <path d="M335,193 Q356,186 378,192 Q372,200 340,199 Z" fill="#333"/>
    <circle cx="390" cy="300" r="13" fill="#888" stroke="#555" stroke-width="2"/>
    <circle cx="390" cy="300" r="22" fill="none" stroke="#777" stroke-width="2" stroke-dasharray="3 3">
      <animateTransform attributeName="transform" type="rotate" from="0 390 300" to="360 390 300" dur="{PEDAL_DUR}" repeatCount="indefinite"/>
    </circle>
    <g>
      <line x1="364" y1="300" x2="416" y2="300" stroke="#555" stroke-width="5" stroke-linecap="round"/>
      <animateTransform attributeName="transform" type="rotate" from="0 390 300" to="360 390 300" dur="{PEDAL_DUR}" repeatCount="indefinite"/>
    </g>
    <path d="M520,215 L532,218 L530,228 L518,225 Z" fill="#ffeb3b" stroke="#999"/>

    <!-- 上半身随踩踏起伏 -->
    <g>
      <animateTransform attributeName="transform" type="translate" values="0 0;0 2;0 0;0 2;0 0" dur="{PEDAL_DUR}" repeatCount="indefinite"/>

      <!-- 远侧手臂 -->
      <path d="M418,142 Q448,168 484,174" fill="none" stroke="#e0a77a" stroke-width="10" stroke-linecap="round" opacity="0.85"/>

      <!-- 身体 -->
      <path d="M358,206 Q372,150 412,128 Q434,138 432,156 Q406,180 386,214 Z" fill="#ffb300"/>
      <path d="M398,140 L410,190" stroke="#ff8f00" stroke-width="3"/>

      <!-- 围巾 -->
      <path fill="#26a69a">
        <animate attributeName="d" dur="0.5s" repeatCount="indefinite"
          values="M408,126 Q380,124 350,120 Q330,118 318,128 Q340,134 372,134 Q392,136 410,136 Z;
                  M408,126 Q378,114 350,124 Q330,132 316,120 Q338,140 372,138 Q392,138 410,136 Z;
                  M408,126 Q380,124 350,120 Q330,118 318,128 Q340,134 372,134 Q392,136 410,136 Z"/>
      </path>
      <path d="M402,124 Q418,122 432,130 Q420,140 404,136 Z" fill="#00897b"/>

      <!-- 头 -->
      <g>
        <animateTransform attributeName="transform" type="rotate" values="0 425 100;3 425 100;0 425 100;-2 425 100;0 425 100" dur="1.8s" repeatCount="indefinite"/>
        <circle cx="428" cy="98" r="30" fill="#ffd9b8"/>
        <path d="M396,94 Q398,60 432,60 Q462,62 462,92 Q446,80 428,82 Q410,82 396,94 Z" fill="#3949ab"/>
        <path d="M410,66 L420,64 M432,62 L442,63 M450,68 L456,72" stroke="#fff" stroke-width="3" stroke-linecap="round"/>
        <path d="M462,90 Q470,92 472,96 L458,96 Z" fill="#283593"/>
        <path d="M402,98 Q404,118 412,124" stroke="#3949ab" stroke-width="2" fill="none"/>
        <ellipse cx="444" cy="98" rx="3.2" ry="4.2" fill="#333">
          <animate attributeName="ry" values="4.2;4.2;0.4;4.2" keyTimes="0;0.92;0.96;1" dur="3s" repeatCount="indefinite"/>
        </ellipse>
        <circle cx="445" cy="96.5" r="1.1" fill="#fff"/>
        <ellipse cx="447" cy="110" rx="6" ry="3.5" fill="#ff8a80" opacity="0.6"/>
        <path d="M442,114 Q450,120 457,112" fill="none" stroke="#a0522d" stroke-width="2.4" stroke-linecap="round"/>
        <path d="M456,100 Q461,104 457,106" fill="none" stroke="#d9a57e" stroke-width="2"/>
      </g>

      <!-- 近侧手臂 -->
      <path d="M408,146 Q440,176 486,176" fill="none" stroke="#ffb300" stroke-width="13" stroke-linecap="round"/>
      <path d="M440,168 Q462,178 486,176" fill="none" stroke="#ffd9b8" stroke-width="10" stroke-linecap="round"/>
      <circle cx="488" cy="175" r="7" fill="#ffd9b8"/>
    </g>

    <!-- 近侧腿 -->
    {near_leg}
  </g>

  <text x="400" y="408" font-size="16" fill="#fff" text-anchor="middle" opacity="0.9"
    font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif">醍醐出发啦～</text>
</svg>
"""
    print(svg)


if __name__ == "__main__":
    main()
