'''
@Project ：COMFYUI-form 
@File    ：Text.py
@Author  ：Deer
@Email   ：wanglu4@37.com
@Date    ：2024/3/18 16:06 
'''
'''
@Project ：ComfyUI-I2VGEN_XL 
@File    ：I2VGenXL.py
@Author  ：Deer
@Email   ：wanglu4@37.com
@Date    ：2024/3/11 15:19 
'''
import os
import cv2
import torch
import numpy as np
import folder_paths

current_directory = os.path.dirname(os.path.abspath(__file__))

class DisplayText:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            },
            "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    OUTPUT_NODE = True
    FUNCTION = "display_text"

    CATEGORY = "Deer模块组✨"

    def display_text(self, text, prompt=None, extra_pnginfo=None):
        return {"ui": {"string": [text, ]}, "result": (text,)}

NODE_CLASS_MAPPINGS = {
    "Text_Showcase": Text_Showcase,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Text_Showcase": "📽Text_Showcase",
}