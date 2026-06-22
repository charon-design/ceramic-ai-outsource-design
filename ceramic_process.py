from PIL import Image, ImageEnhance, ImageFilter
import os

# 醴陵陶瓷文创外包图像处理工具
class CeramicImageTool:
    def __init__(self, input_dir="input", output_dir="output"):
        self.input_dir = input_dir
        self.output_dir = output_dir
        # 创建文件夹
        if not os.path.exists(self.input_dir):
            os.mkdir(self.input_dir)
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)

    # 1.图片高清修复、降噪
    def enhance_img(self, img_path, save_name):
        img = Image.open(img_path)
        # 降噪平滑
        img = img.filter(ImageFilter.SMOOTH_MORE)
        # 提升清晰度
        sharp = ImageEnhance.Sharpness(img)
        img = sharp.enhance(1.8)
        # 提升色彩饱和度（适配釉下彩）
        color = ImageEnhance.Color(img)
        img = color.enhance(1.3)
        save_path = os.path.join(self.output_dir, save_name)
        img.save(save_path, "CMYK")  # 转为印刷CMYK模式
        print(f"已处理并保存：{save_path}")

    # 2.批量处理文件夹内所有图片
    def batch_process(self):
        file_list = os.listdir(self.input_dir)
        for file in file_list:
            if file.endswith(("jpg", "png", "jpeg")):
                full_path = os.path.join(self.input_dir, file)
                self.enhance_img(full_path, file)

if __name__ == "__main__":
    tool = CeramicImageTool()
    # 执行批量瓷器图像修复调色，输出印刷专用图
    tool.batch_process()
