from PIL import Image
import os
import sys

def convert_jpg_to_png(input_path, output_path=None):
    try:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"输入文件不存在: {input_path}")

        file_extension = os.path.splitext(input_path)[1].lower()
        if file_extension not in ['.jpg', '.jpeg']:
            raise ValueError(f"输入文件并非JPG格式: {input_path}")

        if output_path is None:
            base_name = os.path.splitext(input_path)[0]
            output_path = f"{base_name}.png"

        with Image.open(input_path) as img:
            img.save(output_path, 'PNG')

        return output_path

    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"错误: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用方法: python jpg_to_png.py <input.jpg> [output.png]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    result = convert_jpg_to_png(input_file, output_file)
    if result:
        print(f"成功转换为: {result}")