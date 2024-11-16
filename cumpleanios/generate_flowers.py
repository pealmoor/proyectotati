from PIL import Image, ImageDraw

# Crear una nueva imagen con fondo blanco
img = Image.new('RGB', (400, 400), color=(255, 255, 255))

# Crear un objeto de dibujo
draw = ImageDraw.Draw(img)

# Colores para las flores y el tallo
flower_color = (138, 43, 226)  # Color morado
center_color = (255, 215, 0)   # Color dorado para el centro
stem_color = (34, 139, 34)     # Color verde para el tallo

# Función para dibujar una flor con pétalos
def draw_flower(x, y, size):
    # Pétalos (dibujar 5 pétalos alrededor del centro)
    petal_size = size
    draw.ellipse([(x - petal_size, y - petal_size), (x + petal_size, y + petal_size)], fill=flower_color)
    draw.ellipse([(x - petal_size*1.5, y), (x + petal_size*1.5, y + petal_size*2)], fill=flower_color)
    draw.ellipse([(x, y - petal_size*1.5), (x + petal_size*2, y + petal_size*1.5)], fill=flower_color)
    draw.ellipse([(x + petal_size, y - petal_size), (x + petal_size*3, y + petal_size)], fill=flower_color)
    draw.ellipse([(x - petal_size, y + petal_size), (x + petal_size*3, y + petal_size*3)], fill=flower_color)
    
    # Centro de la flor
    draw.ellipse([(x - size // 4, y - size // 4), (x + size // 4, y + size // 4)], fill=center_color)

# Función para dibujar el tallo de la flor
def draw_stem(x, y):
    draw.line((x, y + 50, x, y + 200), fill=stem_color, width=5)

# Dibujar varias flores en la imagen
flower_positions = [(150, 100), (250, 150), (100, 250), (200, 300), (300, 200)]
flower_size = 30

for pos in flower_positions:
    draw_flower(pos[0], pos[1], flower_size)
    draw_stem(pos[0], pos[1])

# Guardar la imagen en un archivo
img.save('static/images/ramo_floras.png')

# Mostrar la imagen
img.show()
