from PIL import Image, ImageDraw, ImageFont
import os

card_w, card_h = 700, 950
img = Image.new('RGB', (card_w, card_h), color='#160512')
draw = ImageDraw.Draw(img)

# Background subtle vignette / border
for i in range(80):
    r = int(45 - i * 0.3)
    g = int(12 - i * 0.1)
    b = int(30 - i * 0.2)
    draw.rectangle([i*2, i*2, card_w - i*2, card_h - i*2], outline=(r, g, b), width=2)

# Outer Border
draw.rounded_rectangle([25, 25, card_w - 25, card_h - 25], radius=35, outline='#e11d48', width=3)
draw.rounded_rectangle([32, 32, card_w - 32, card_h - 32], radius=30, outline='#fda4af', width=1)

# Badge Header
draw.rounded_rectangle([190, 60, card_w - 190, 105], radius=22, fill='#3b0f2a', outline='#f43f5e', width=2)

# Load fonts
try:
    font_badge = ImageFont.truetype('arial.ttf', 16)
    font_title = ImageFont.truetype('arialbd.ttf', 30)
    font_sub = ImageFont.truetype('georgiai.ttf', 20)
    font_code = ImageFont.truetype('arialbd.ttf', 22)
    font_sign = ImageFont.truetype('brushsci.ttf', 38)
except Exception:
    font_badge = font_title = font_sub = font_code = font_sign = ImageFont.load_default()

def draw_center_text(y, text, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    draw.text(((card_w - w) // 2, y), text, font=font, fill=fill)

draw_center_text(73, 'A PRIVATE GIFT FOR LEENA ❤️', font_badge, '#fda4af')
draw_center_text(135, 'Scan With Your Phone Camera', font_title, '#ffffff')
draw_center_text(180, 'A world crafted only for you, waiting to be unlocked.', font_sub, '#fbcfe8')

# QR Code Box
qr_size = 400
qr_x = (card_w - qr_size) // 2
qr_y = 230

# White backing frame with pink border
draw.rounded_rectangle([qr_x - 15, qr_y - 15, qr_x + qr_size + 15, qr_y + qr_size + 15], radius=25, fill='#ffffff', outline='#f43f5e', width=5)

# Paste QR Code
qr_source = r'C:\Users\Admin\Downloads\Leena_QR_Code.png'
qr_img = Image.open(qr_source).resize((qr_size, qr_size))
img.paste(qr_img, (qr_x, qr_y))

# Center Heart Emblem in QR
heart_cx = card_w // 2
heart_cy = qr_y + qr_size // 2
r_c = 34
draw.ellipse([heart_cx - r_c, heart_cy - r_c, heart_cx + r_c, heart_cy + r_c], fill='#e11d48', outline='#ffffff', width=3)
draw.polygon([(heart_cx - 18, heart_cy - 2), (heart_cx + 18, heart_cy - 2), (heart_cx, heart_cy + 18)], fill='#ffffff')
draw.ellipse([heart_cx - 18, heart_cy - 12, heart_cx + 2, heart_cy + 4], fill='#ffffff')
draw.ellipse([heart_cx - 2, heart_cy - 12, heart_cx + 18, heart_cy + 4], fill='#ffffff')

# Secret Passcode Box
draw.rounded_rectangle([160, 690, card_w - 160, 745], radius=25, fill='#2e0b20', outline='#fb7185', width=2)
draw_center_text(706, 'Secret Passcode:   0 7 1 0', font_code, '#ffffff')

# Signature & Footnote
draw_center_text(780, 'Forever Yours, Jeevanantham ❤️', font_sign, '#f472b6')
draw_center_text(855, 'https://mygirl-bday.netlify.app', font_badge, '#fda4af')

dst_path = r'C:\Users\Admin\Downloads\Leena_Heart_Gift_Card.png'
img.save(dst_path, quality=95)
dst_path2 = r'C:\Users\Admin\.gemini\antigravity\scratch\client\Leena_Heart_Gift_Card.png'
img.save(dst_path2, quality=95)
print('GIFT_CARD_GENERATED_SUCCESSFULLY at:', dst_path)
