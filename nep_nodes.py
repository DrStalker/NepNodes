"""
@author: Nepenthe
@title: NepNodes Custom Nodes for ComfyUI
@nickname: NepNodes
@description: Personal Nodes
"""


import torch
import json
import os
import comfy.sd
import folder_paths
#from datetime import datetime
#from PIL import Image, ImageOps, ImageSequence
#import numpy as np
#from PIL.PngImagePlugin import PngInfo
#from comfy.cli_args import args
#import torch.nn.functional as F



#---------------------------------------------------------------------------------------------------------------------------------------------------#

#Based on JPS SDXL resolution

class NepWan_Resolutions:
    resolution = ["480p square - 640x640","480p landscape - 848x480", "480p portrait - 480x848", "480p 4:3 landscape - 640x480","480p 4:3 portrait - 480x640"]
    
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "resolution": (s.resolution,),
            }
        }
    RETURN_TYPES = ("INT","INT",)
    RETURN_NAMES = ("width", "height")
    FUNCTION = "get_resolutions"

    CATEGORY="NepNodes"

    def get_resolutions(self,resolution):
        width = 1024
        height = 1024
        width = int(width)
        height = int(height)
        if(resolution == "480p square - 640x640"):
            width = 640
            height = 640
        if(resolution == "480p landscape - 848x480"):
            width = 848
            height = 480
        if(resolution == "480p portrait - 480x848"):
            width = 480
            height = 848
        if(resolution == "480p 4:3 landscape - 640x480"):
            width = 640
            height = 480
        if(resolution == "480p 4:3 portrait - 480x640"):
            width = 480
            height = 640
        return(int(width),int(height))

#---------------------------------------------------------------------------------------------------------------------------------------------------#

# based on JPS tools multiply
class NepXOR_INT_INT:

    def init(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "int_a": ("INT", {"default": 1,}),
                "int_b": ("INT", {"default": 1,}),
            }
        }

    RETURN_TYPES = ("INT")
    RETURN_NAMES = ("xor")
    FUNCTION = "get_xor_int_int"

    CATEGORY="NepNodes"

    def get_xor_int_int(self,int_a,int_b):
        xor = int(int_a) ^ int(int_b)        

        return(int(xor))

#---------------------------------------------------------------------------------------------------------------------------------------------------#


class NepRemoveFirstOrLastImageFromBatch:
    # from comfyUI_LLM
    #"""
    #删除图片batch的首帧或末帧，输出剩余IMAGE batch。
    #"""
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_batch": ("IMAGE", {}),
                "mode": (["first", "last"], {"default": "first"}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image_batch",)
    FUNCTION = "remove"
    CATEGORY="NepNodes"

    def remove(self, image_batch, mode="first"):
        import torch
        if image_batch.dim() == 3:
            # 只有一张，删除后为空batch
            return (torch.empty((0, *image_batch.shape), dtype=image_batch.dtype, device=image_batch.device),)
        if image_batch.shape[0] == 0:
            return (image_batch,)
        if mode == "first":
            return (image_batch[1:],)
        else:
            return (image_batch[:-1],)
