
environment details:
系統:Windows 11 家用版，64 位元作業系統，x64 型處理器

GPU:NVDIA Geforce RTX3060 12GB

Package                Version
---------------------- ------------
matplotlib             3.9.2
numpy                  1.26.4
torch                  2.4.0+cu124
torchaudio             2.4.0+cu124
torchmetrics           1.4.2
torchvision            0.19.0+cu124
transformers           4.47.0

#####Python 3.10.11 #####
---------------------------------------------------------------------------------------------------
How to run your code:

1.Image Captioning:

使用generate.ipynb直接run就可以了

可以調整
-json_path = 'label.json'  # 請替換為你的label.json路徑
-images_dir = 'images'  # 圖片的目錄，請確保包含label.json中的圖片
-output_path = 'output_blip2-flan-t5-xl.jsonl'

2.Text-to-Image Generation

pytohn3 duffusion.py

-with open("output.json", "r") as f:#這邊調整json黨的路徑

3.計算FID
git clone https://github.com/mseitzer/pytorch-fid.git
pip install pytorch-fid
執行:
python -m --device cuda:0 --num-workers 0 --batch-size 16 pytorch_fid path/to/dataset1 path/to/dataset2
(--device cuda:0 --num-workers 0 --batch-size 16 可調整batch-size設太大會爆炸)

----------其他小程式
python3 resize_img.py 調整原圖大小跑計算FID時才不會抱錯