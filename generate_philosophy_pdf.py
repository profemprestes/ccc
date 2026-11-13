from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Register fonts from public/fuentes
font_dir = r"D:\repositorios\ccc\public\fuentes"

# Register Anton SC (display)
anton_path = os.path.join(font_dir, "Anton_SC", "AntonSC-Regular.ttf")
if os.path.exists(anton_path):
    pdfmetrics.registerFont(TTFont("AntonSC", anton_path))

# Register Bebas Neue (subheading)
bebas_path = os.path.join(font_dir, "Bebas_Neue", "BebasNeue-Regular.ttf")
if os.path.exists(bebas_path):
    pdfmetrics.registerFont(TTFont("BebasNeue", bebas_path))

# Register Outfit (body)
outfit_path = os.path.join(font_dir, "Outfit", "Outfit-VariableFont_wght.ttf")
if os.path.exists(outfit_path):
    pdfmetrics.registerFont(TTFont("Outfit", outfit_path))

# Register Geist Mono (mono)
geist_path = os.path.join(font_dir, "Geist_Mono", "GeistMono-VariableFont_wght.ttf")
if os.path.exists(geist_path):
    pdfmetrics.registerFont(TTFont("GeistMono", geist_path))

# Colors from DosRuedas design system
BLUE = HexColor("#0950F6")
BLUE_DARK = HexColor("#031811")
YELLOW = HexColor("#FFEC01")
WHITE = HexColor("#FFFFFF")
BLUE_50 = HexColor("#E6EEFE")
BLUE_100 = HexColor("#BACEFD")
BLUE_300 = HexColor("#628FF9")
BLUE_400 = HexColor("#3570F8")

# Page setup
WIDTH, HEIGHT = A4
MARGIN = 3 * cm

def draw_hero_band(c):
    """Draw the full-bleed blue hero band with dot grid and route curves"""
    # Blue background
    c.setFillColor(BLUE)
    c.rect(0, HEIGHT - 18*cm, WIDTH, 18*cm, fill=1, stroke=0)

    # Subtle dot grid pattern
    c.setFillColor(HexColor("#0950F6"))
    c.setStrokeColor(HexColor("#1a5fff"))
    dot_spacing = 24
    for x in range(0, int(WIDTH), dot_spacing):
        for y in range(int(HEIGHT - 18*cm), int(HEIGHT), dot_spacing):
            c.circle(x, y, 1.2, fill=1, stroke=0)

    # Dashed yellow route curves (SVG-inspired)
    c.setStrokeColor(YELLOW)
    c.setLineWidth(2.5)
    c.setDash([12, 16], 0)

    # Curve 1 - sweeping from left
    p = c.beginPath()
    p.moveTo(2*cm, HEIGHT - 5*cm)
    p.curveTo(6*cm, HEIGHT - 2*cm, 12*cm, HEIGHT - 8*cm, 18*cm, HEIGHT - 4*cm)
    c.drawPath(p, fill=0, stroke=1)

    # Curve 2 - from right
    p = c.beginPath()
    p.moveTo(WIDTH - 2*cm, HEIGHT - 8*cm)
    p.curveTo(WIDTH - 6*cm, HEIGHT - 12*cm, WIDTH - 14*cm, HEIGHT - 6*cm, WIDTH - 20*cm, HEIGHT - 10*cm)
    c.drawPath(p, fill=0, stroke=1)

    # Route node dots
    c.setFillColor(YELLOW)
    c.setDash([], 0)
    for pt in [(6*cm, HEIGHT - 2*cm), (12*cm, HEIGHT - 8*cm), (WIDTH - 6*cm, HEIGHT - 12*cm), (WIDTH - 14*cm, HEIGHT - 6*cm)]:
        c.circle(pt[0], pt[1], 5, fill=1, stroke=0)

def draw_philosophy_text(c, y_start):
    """Draw the Sistema Lúcido philosophy text with proper typography"""
    x = MARGIN
    max_width = WIDTH - 2*MARGIN
    y = y_start
    line_height = 14

    # Title
    c.setFont("AntonSC", 42)
    c.setFillColor(BLUE)
    c.drawString(x, y, "SISTEMA LÚCIDO")
    y -= 55

    # Subtitle
    c.setFont("BebasNeue", 24)
    c.setFillColor(BLUE_400)
    c.drawString(x, y, "A Design Philosophy for Clarity Through Rigorous Distillation")
    y -= 45

    # Yellow accent line
    c.setStrokeColor(YELLOW)
    c.setLineWidth(3)
    c.line(x, y, x + 8*cm, y)
    y -= 30

    # Philosophy paragraphs
    paragraphs = [
        ("Philosophy",
         "Sistema Lúcido is a design philosophy built on the conviction that clarity is not the absence of complexity but its rigorous distillation. It treats visual systems as living architectures—each token, each curve, each shadow a deliberate decision that serves both function and feeling. The system does not decorate; it discloses. Every color ramp, every typographic scale, every spacing rhythm exists because it earned its place through iteration and scrutiny. The result feels inevitable, as though it could not have been otherwise, though it emerged from countless hours of painstaking refinement by hands that understand the weight of a single pixel."),

        ("Space and Form",
         "Space in Sistema Lúcido is not empty—it is structured breath. The grid is felt before it is seen, a subtle architecture that aligns without announcing itself. Forms obey a quiet geometry: radii progress in measured steps, containers nest with mathematical harmony, and the double-bezel card—outer tinted shell embracing inner white surface—becomes a signature motif that repeats across scales. Nothing floats without anchor; nothing touches without intention. The composition rewards sustained viewing, revealing its logic layer by layer to the patient eye."),

        ("Color and Material",
         "Color is never arbitrary. A single accent hue—electric blue, acid lime, chartreuse, ember orange—carries the system's emotional weight, rationed like a precious resource. It appears in hairlines, in selection highlights, in the glow of a primary CTA, in the tint of every elevation shadow. Neutrals are not gray; they are the accent hue desaturated, warmed, cooled—blue-tinted whites, blue-tinted shadows—so the entire palette breathes as one organism. Surfaces have weight: the matte white of a card interior, the translucent veil of a glass tile, the deep saturation of a hero band. Each material catches light differently, and the system defines exactly how."),

        ("Scale and Rhythm",
         "Typography speaks in distinct voices that never blur: a display face for proclamation (Anton, Archivo Black, Epilogue at 760 weight), a condensed subheading for structure (Bebas Neue, Formular), a geometric sans for reading (Outfit, Inter, GT Walsheim), a monospace for precision (Geist Mono, Input Mono, JetBrains Mono). Each scale step is calibrated—line heights, letter-spacing, text transforms—so that hierarchy emerges from rhythm alone, not size brute force. Vertical spacing follows a base unit that compounds: 8px, 24px, 80px, 120px. The page breathes in multiples, never in guesses."),

        ("Composition and Balance",
         "Asymmetry is the default symmetry. Hero bands split 7/5, service grids alternate 2/3 columns, footer columns distribute unevenly by design. The eye is led, not pushed. White space is not passive background—it is active counterweight. A headline's negative tracking pulls it tight; a card's generous padding pushes its content inward. The double-bezel frame creates depth without shadow theater. Every component exists in multiple states—rest, hover, focus, pressed, disabled—each transition choreographed at 300ms with custom cubic-bezier curves that feel human, not mechanical."),

        ("Visual Hierarchy",
         "Information architecture is visual architecture. The most important element claims the strongest contrast: yellow on blue, white on blue, blue on white. Secondary actions recede into outline pills, ghost buttons, muted labels. Data—tracking IDs, cut-off times, prices—wears its monospace badge proudly. Status accents (WhatsApp green, success mint) are scoped to their domain, never leaking into general UI. The system guards its own boundaries: no neutral grays for body text on light surfaces, no black-tinted shadows, no accent sprawl. These guardrails are not constraints—they are the discipline that makes freedom possible."),

        ("Craftsmanship",
         "Sistema Lúcido is the product of deep expertise, labored over with painstaking attention, meticulously crafted down to the last token. Every cubic-bezier curve was tuned by hand. Every color stop in every gradient was eyeballed at 200% zoom. Every font weight was tested across viewports, across languages, across light and dark modes. The specification documents themselves—YAML frontmatter married to prose—are artifacts of the same care: machine-readable tokens for the build pipeline, human-readable rationale for the next designer. This is not a framework. It is a covenant between intention and execution. The work shows the hours. The work shows the hands.")
    ]

    for heading, body in paragraphs:
        # Heading
        c.setFont("BebasNeue", 18)
        c.setFillColor(BLUE)
        c.drawString(x, y, heading.upper())
        y -= 26

        # Body text - wrapped
        c.setFont("Outfit", 10.5)
        c.setFillColor(BLUE_DARK)

        words = body.split()
        line = ""
        for word in words:
            test_line = line + (" " if line else "") + word
            if c.stringWidth(test_line, "Outfit", 10.5) > max_width:
                c.drawString(x, y, line)
                y -= line_height
                line = word
            else:
                line = test_line
        if line:
            c.drawString(x, y, line)
            y -= line_height

        y -= 18  # Paragraph spacing

        # Check if we need a new page
        if y < 4*cm:
            c.showPage()
            draw_hero_band(c)
            y = HEIGHT - 20*cm

    return y

def draw_typography_specimen(c, y_start):
    """Draw a typography specimen page showing the font system"""
    x = MARGIN
    y = y_start

    c.setFont("AntonSC", 28)
    c.setFillColor(BLUE)
    c.drawString(x, y, "TYPOGRAPHY SYSTEM")
    y -= 40

    c.setStrokeColor(YELLOW)
    c.setLineWidth(2)
    c.line(x, y, x + 6*cm, y)
    y -= 30

    specimens = [
        ("Anton SC — Display", "AntonSC", 48, "SISTEMA LÚCIDO", BLUE),
        ("Bebas Neue — Subheading", "BebasNeue", 28, "SPACE AND FORM", BLUE_400),
        ("Outfit — Headline", "Outfit", 32, "Clarity Through Distillation", BLUE_DARK),
        ("Outfit — Body Large", "Outfit", 16, "Every token serves both function and feeling.", BLUE_DARK),
        ("Outfit — Body Medium", "Outfit", 14, "The grid is felt before it is seen.", BLUE_DARK),
        ("Geist Mono — Data", "GeistMono", 14, "TRACK-ID: DSR-2026-0950F6  |  13:00 HS  |  $2.850", HexColor("#3570F8")),
    ]

    for label, font, size, text, color in specimens:
        c.setFont("Outfit", 9)
        c.setFillColor(BLUE_300)
        c.drawString(x, y, label)
        y -= 16

        c.setFont(font, size)
        c.setFillColor(color)
        c.drawString(x, y, text)
        y -= size + 12

    return y

def draw_color_palette(c, y_start):
    """Draw the color palette with swatches"""
    x = MARGIN
    y = y_start
    swatch_h = 1.8*cm
    swatch_w = 4*cm
    gap = 1*cm

    c.setFont("AntonSC", 28)
    c.setFillColor(BLUE)
    c.drawString(x, y, "COLOR PALETTE")
    y -= 40

    c.setStrokeColor(YELLOW)
    c.setLineWidth(2)
    c.line(x, y, x + 6*cm, y)
    y -= 30

    colors = [
        ("Electric Blue\n#0950F6", BLUE, WHITE),
        ("Blue 400\n#3570F8", BLUE_400, WHITE),
        ("Blue 300\n#628FF9", BLUE_300, BLUE_DARK),
        ("Blue 100\n#BACEFD", BLUE_100, BLUE_DARK),
        ("Blue 50\n#E6EEFE", BLUE_50, BLUE_DARK),
        ("Pure White\n#FFFFFF", WHITE, BLUE_DARK),
        ("High-Vis Yellow\n#FFEC01", YELLOW, BLUE_DARK),
        ("Yellow Hover\n#FFF12E", HexColor("#FFF12E"), BLUE_DARK),
        ("Deep Forest\n#031811", BLUE_DARK, YELLOW),
        ("WhatsApp Green\n#2ECC85", HexColor("#2ECC85"), WHITE),
    ]

    for i, (label, bg, text_color) in enumerate(colors):
        col = i % 5
        row = i // 5
        sx = x + col * (swatch_w + gap)
        sy = y - row * (swatch_h + 2*cm)

        # Swatch
        c.setFillColor(bg)
        c.roundRect(sx, sy - swatch_h, swatch_w, swatch_h, 8, fill=1, stroke=0)

        # Label
        c.setFont("Outfit", 9)
        c.setFillColor(text_color)
        lines = label.split('\n')
        for j, line in enumerate(lines):
            c.drawCentredString(sx + swatch_w/2, sy - swatch_h + 8 - j*12, line)

    return y - 2 * (swatch_h + 2*cm)

def draw_component_specimens(c, y_start):
    """Draw component specimens: buttons, cards, double-bezel"""
    x = MARGIN
    y = y_start

    c.setFont("AntonSC", 28)
    c.setFillColor(BLUE)
    c.drawString(x, y, "COMPONENT SPECIMENS")
    y -= 40

    c.setStrokeColor(YELLOW)
    c.setLineWidth(2)
    c.line(x, y, x + 6*cm, y)
    y -= 30

    # Primary Yellow Button
    c.setFont("BebasNeue", 14)
    c.setFillColor(BLUE)
    c.drawString(x, y, "PRIMARY YELLOW PILL")
    y -= 22

    btn_y = y
    c.setFillColor(YELLOW)
    c.roundRect(x, btn_y - 10, 180, 36, 18, fill=1, stroke=0)
    # Glow effect simulation
    c.setFillColor(HexColor("#ffec0140"))
    c.roundRect(x - 2, btn_y - 12, 184, 40, 20, fill=1, stroke=0)
    c.setFillColor(YELLOW)
    c.roundRect(x, btn_y - 10, 180, 36, 18, fill=1, stroke=0)
    c.setFont("Outfit", 13)
    c.setFillColor(BLUE)
    c.drawCentredString(x + 90, btn_y + 2, "COTIZÁ AHORA")
    y -= 60

    # Secondary Blue Button
    c.setFont("BebasNeue", 14)
    c.setFillColor(BLUE)
    c.drawString(x, y, "SECONDARY BLUE PILL")
    y -= 22

    btn_y = y
    c.setFillColor(BLUE)
    c.roundRect(x, btn_y - 10, 180, 36, 18, fill=1, stroke=0)
    c.setFont("Outfit", 13)
    c.setFillColor(WHITE)
    c.drawCentredString(x + 90, btn_y + 2, "VER SERVICIOS")
    y -= 60

    # Outline Light Button
    c.setFont("BebasNeue", 14)
    c.setFillColor(BLUE)
    c.drawString(x, y, "OUTLINE LIGHT PILL")
    y -= 22

    btn_y = y
    c.setStrokeColor(HexColor("#ffffff73"))
    c.setLineWidth(1.5)
    c.roundRect(x, btn_y - 10, 180, 36, 18, fill=0, stroke=1)
    c.setFont("Outfit", 13)
    c.setFillColor(WHITE)
    c.drawCentredString(x + 90, btn_y + 2, "CONTACTAR")
    y -= 60

    # Double Bezel Card
    c.setFont("BebasNeue", 14)
    c.setFillColor(BLUE)
    c.drawString(x, y, "DOUBLE-BEZEL SERVICE CARD")
    y -= 22

    card_x = x
    card_y = y - 100
    # Outer bezel
    c.setFillColor(BLUE_50)
    c.roundRect(card_x, card_y, 220, 100, 24, fill=1, stroke=0)
    c.setStrokeColor(BLUE_100)
    c.setLineWidth(1)
    c.roundRect(card_x, card_y, 220, 100, 24, fill=0, stroke=1)
    # Inner surface
    c.setFillColor(WHITE)
    c.roundRect(card_x + 6, card_y + 6, 208, 88, 18, fill=1, stroke=0)
    # Shadow
    c.setFillColor(HexColor("#0950f61f"))
    c.roundRect(card_x + 4, card_y + 2, 220, 100, 24, fill=1, stroke=0)

    # Card content
    c.setFont("BebasNeue", 16)
    c.setFillColor(BLUE)
    c.drawString(card_x + 20, card_y + 65, "ENVÍOS EXPRESS")
    c.setFont("Outfit", 10)
    c.setFillColor(BLUE_DARK)
    c.drawString(card_x + 20, card_y + 45, "Entrega en 90 min • Mar del Plata")
    c.setFont("GeistMono", 12)
    c.setFillColor(BLUE_400)
    c.drawString(card_x + 20, card_y + 25, "$ 2.850")

    y = card_y - 20
    return y

def main():
    output_path = r"D:\repositorios\ccc\sistema-lucido.pdf"
    c = canvas.Canvas(output_path, pagesize=A4)

    # Page 1: Hero + Philosophy
    draw_hero_band(c)
    y = draw_philosophy_text(c, HEIGHT - 20*cm)

    # Page 2: Typography
    c.showPage()
    draw_hero_band(c)
    y = draw_typography_specimen(c, HEIGHT - 20*cm)

    # Color palette on page 2
    y = draw_color_palette(c, y - 2*cm)

    # Page 3: Components
    c.showPage()
    draw_hero_band(c)
    y = draw_component_specimens(c, HEIGHT - 20*cm)

    # Footer on last page
    c.setFont("Outfit", 8)
    c.setFillColor(BLUE_300)
    c.drawCentredString(WIDTH/2, 2*cm, "Sistema Lúcido — DosRuedas Electric Dispatch Design Philosophy")
    c.drawCentredString(WIDTH/2, 1.5*cm, "Meticulously crafted. The work shows the hours. The work shows the hands.")

    c.save()
    print(f"PDF generated: {output_path}")

if __name__ == "__main__":
    main()