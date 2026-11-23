import os
from PIL import Image

# Folder mein maujood image file khud dhoondhna
image_files = [f for f in os.listdir(".") if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp")) and "ready" not in f.lower() and "logo" not in f.lower()]

if not image_files:
    print("Error: 'D:\Python 3D' folder mein koi banner image nahi mili! Pehle image ko is folder mein copy karein.")
else:
    input_file = image_files[0]
    print(f"File mil gayi: {input_file} -> Resize ho rahi hai...")
    
    img = Image.open(input_file).convert("RGB")

    # YouTube ka exact banner canvas (2560 x 1440) aur dark background color
    canvas = Image.new("RGB", (2560, 1440), (5, 2, 20))

    # Design ko chota karke safe-zone ke mutabiq fit karna
    new_width = 1650
    new_height = int((new_width / img.width) * img.height)
    resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Bilkul center mein paste karna
    x = (2560 - new_width) // 2
    y = (1440 - new_height) // 2
    canvas.paste(resized_img, (x, y))

    canvas.save("youtube_banner_ready.png")
    print("Done! Ab 'youtube_banner_ready.png' ko YouTube par upload karein.")
