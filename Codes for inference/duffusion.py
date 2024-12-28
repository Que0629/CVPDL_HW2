import torch
from diffusers import StableDiffusionGLIGENPipeline
from diffusers.utils import load_image
import os

import time
import json
# C:\Users\andy5\Desktop\cvpdl_hw3\visualiztion_200.json
# with open("C:/Users/andy5/Desktop/cvpdl_hw3/visualiztion_200.json", "r") as f:
#     json_data = json.load(f)
with open("output.json", "r") as f:
    json_data = json.load(f)
from diffusers import DiffusionPipeline

pipe = StableDiffusionGLIGENPipeline.from_pretrained(
    "masterful/gligen-1-4-generation-text-box", variant="fp16", torch_dtype=torch.float16
)
pipe = pipe.to("cuda")
for entry in json_data:
    image_name = entry["image"]
    prompts = {
        # "normal": entry["generated_text"],
        "label": entry["prompt_w_label"],
        "suffix": entry["prompt_w_suffix"]
    }
    save_folders = {
        # "normal":"generated_normal",
        "label": "generation_label",
        "suffix": "generation_suffix"
    }
    for i in range(2):
        for prompt_type, prompt_text in prompts.items():
            

            start_time = time.time()
            

            prompt = prompt_text
            
            
            if i==0:
                phrases=[""]
                boxes=[[0.0, 0.0, 1.0, 1.0]] 
            else:
                phrases = entry["labels"]
                boxes = entry["bboxes"]
                image_width = 512  # 圖片寬度
                image_height = 512 # 圖片高度
                # 如果 boxes 是以像素坐標傳遞，則將其轉換為相對坐標
                # 假設 `boxes` 是 [x_min, y_min, x_max, y_max] 的形式
                boxes = [
                    [x_min / image_width, y_min / image_height, x_max / image_width, y_max / image_height]
                    for x_min, y_min, x_max, y_max in boxes
                ]
            # print(boxes)
            # exit()
            input_image = load_image(
                "https://hf.co/datasets/huggingface/documentation-images/resolve/main/diffusers/gligen/livingroom_modern.png"
            )
            images = pipe(
                prompt=prompt,
                gligen_phrases=phrases,
                gligen_boxes=boxes,
                gligen_scheduled_sampling_beta=1,
                output_type="pil",
                num_inference_steps=100,
            ).images
            if i==0:
                images[0].save(save_folders[prompt_type]+'_onlytext/'+entry["image"])
            else:
                images[0].save(save_folders[prompt_type]+'/'+entry["image"])
            print(images)

