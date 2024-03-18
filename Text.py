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

class Text_Showcase:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "TXT": ("STRING", {
                    "default": "Distorted, discontinuous, Ugly, blurry, low resolution, motionless, static, disfigured, disconnected limbs, Ugly faces, incomplete arms",
                    "multiline": True}),
            }
        }

    RETURN_TYPES = ("MODEL",)
    RETURN_NAMES = ("pipe",)
    FUNCTION = "show txt"
    CATEGORY = "Deer"



NODE_CLASS_MAPPINGS = {
    "Text_Showcase": Text_Showcase,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Text_Showcase": "📽Text_Showcase",
}