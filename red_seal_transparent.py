from PIL import Image
import sys
import os

def is_red(color, hue_threshold=10/360):
    r, g, b = color[:3]
    r, g, b = [x/255.0 for x in (r, g, b)]
    
    max_val = max(r, g, b)
    min_val = min(r, g, b)
    delta = max_val - min_val
    
    if max_val == min_val:
        h = 0
    else:
        if max_val == r:
            h = (g - b) / delta
        elif max_val == g:
            h = 2 + (b - r) / delta
        else:
            h = 4 + (r - g) / delta
        h *= 60
        if h < 0:
            h += 360
    h /= 360
    
    is_red1 = (h <= hue_threshold or h >= (360-10)/360)
    return is_red1

def render_ink_red(rgb_color):
    r, g, b = rgb_color
    # 印泥红目标值 (RGB: 220, 20, 60 左右)
    return (220, 20, 60, 255)

def extract_red_seal(input_path, output_path=None):
    try:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"输入文件不存在: {input_path}")
            
        img = Image.open(input_path).convert("RGBA")
        width, height = img.size
        transparent_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        
        for x in range(width):
            for y in range(height):
                pixel = img.getpixel((x, y))
                if is_red(pixel):
                    new_rgb = render_ink_red(pixel[:3])
                    transparent_img.putpixel((x, y), new_rgb)
                else:
                    transparent_img.putpixel((x, y), (0, 0, 0, 0))
                    
        if output_path is None:
            base_name, ext = os.path.splitext(input_path)
            output_path = f"{base_name}_印泥红.png"
        transparent_img.save(output_path, "PNG")
        return output_path
        
    except Exception as e:
        print(f"处理图片时出错: {e}")
        return None

if __name__ == "__main__":
    input_file = "1.png"
    output_file = "1_印泥红.png"
    result = extract_red_seal(input_file, output_file)
    if result:
        print(f"成功生成印泥红公章: {result}")