import os
from PIL import Image

def resize_images_in_folder(input_folder, output_folder, size=(512, 512)):
    # 檢查輸出資料夾是否存在，如果不存在就創建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 遍歷資料夾中的所有圖像文件
    for filename in os.listdir(input_folder):
        # 構建完整的檔案路徑
        file_path = os.path.join(input_folder, filename)
        
        # 確保這是圖像文件
        if os.path.isfile(file_path) and filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
            try:
                # 開啟圖像
                img = Image.open(file_path)
                # 調整圖像大小
                img_resized = img.resize(size)
                # 保存到新的資料夾中
                img_resized.save(os.path.join(output_folder, filename))
                print(f"Resized and saved: {filename}")
            except Exception as e:
                print(f"Could not process {filename}: {e}")

# 使用範例
input_folder = r'C:/Users/andy5/Desktop/cvpdl_hw3/images'  # 原始資料夾路徑
output_folder = r'C:/Users/andy5/Desktop/cvpdl_hw3/resized_images'  # 輸出資料夾路徑

resize_images_in_folder(input_folder, output_folder)
