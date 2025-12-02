"""
@author: Nepenthe
@title: NepNodes Custom Nodes for ComfyUI
@nickname: NepNodes
@description: Personal Nodes
"""


import math
import re



#---------------------------------------------------------------------------------------------------------------------------------------------------#

# Based on JPS SDXL resolution

class NepWanResolutions:
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


class NepRatioResolution:
    ratio = ["1:1", "5:4", "4:3", "3:2", "16:10","16:9","2:1","21:9"]
    orientation = ["portrait", "landscape"]
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ratio": (s.ratio,),
                "orientation": (s.orientation,),
                "megapixels": ("FLOAT", {"default": 1,"min":0.01,"max":100}),
            }
        }
    RETURN_TYPES = ("INT","INT","FLOAT")
    RETURN_NAMES = ("width", "height", "ratio")
    FUNCTION = "get_resolutions_from_ratio"

    CATEGORY="NepNodes"
    def get_resolutions_from_ratio(self,ratio,megapixels,orientation):
        #print("ratio:",ratio,"megapixels:",megapixels,"orientation:",orientation)

        rationum = float(1) # fallback to 1 if things break weirdly
        if(ratio == "5:4"): 
            rationum = float(5/4)        
        elif(ratio == "4:3"): 
            rationum = float(4/3)
        elif(ratio == "3:2"): 
            rationum = float(3/2)
        elif(ratio == "16:9"): 
            rationum = float(16/9)
        elif(ratio == "16:10"): 
            rationum = float(16/10)
        elif(ratio == "2:1"): 
            rationum = float(2)
        elif(ratio == "21:9"): 
            rationum = float(21/9)

        total_pixels = megapixels * 1024 * 1024
        width = math.sqrt(total_pixels * rationum)
        height = width / rationum
        def round16(x):
            return int(round(x / 16) * 16)  
        def round4(x):
            return int(round(x / 4) * 4)        
        width = round16(width)    # Z-Image likes multiples of 16, I think.
        height = round16(height)  #

        if orientation  == "portrait":
            if width > height:
                width, height = height, width
        else:
            if height > width:
                width, height = height, width
        #print("width:", width, "height:",height,)
        return(width, height, rationum)

#---------------------------------------------------------------------------------------------------------------------------------------------------#

# based on JPS tools multiply
class NepXOR_INT_INT:

    def init(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "int_a": ("INT", {"default": 1,"min":0,"max":1000000000000000}),
                "int_b": ("INT", {"default": 1,"min":0,"max":1000000000000000}),
            }
        }
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("xor",)
    FUNCTION = "get_xor_int_int"
    CATEGORY="NepNodes"
    OUTPUT_TOOLTIPS = ("xor (INT)",)

    def get_xor_int_int(self,int_a,int_b):
        xor = int_a ^ int_b   
        return (int(xor),)


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
                "mode": (["first", "last", "none"], {"default": "none"}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image_batch",)
    FUNCTION = "remove"
    CATEGORY = "NepNodes"

    def remove(self, image_batch, mode="none"):
        import torch
        if image_batch.dim() == 3:
            # 只有一张，删除后为空batch
            return (torch.empty((0, *image_batch.shape), dtype=image_batch.dtype, device=image_batch.device),)
        if image_batch.shape[0] == 0:
            return (image_batch,)
        if mode == "first":
            return (image_batch[1:],)
        if mode == "last":
            return (image_batch[:-1],)        
        else:
            return (image_batch,)
#---------------------------------------------------------------------------------------------------------------------------------------------------#


class NepSafeString:
    #"""
    #Makes a string safe for use in filenames
    #""""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("clean_text",)
    FUNCTION = "maketextsafe"
    CATEGORY = "NepNodes"

    INVALID_CHARS = r'[\\/:*?"<>|\n\r\t]'

    def maketextsafe(self, text):
        if len(text) > 100:  #Max 100 characters
            text = text[:100]
        cleaned = re.sub(self.INVALID_CHARS, "", text)
        cleaned = cleaned.strip()
        return (cleaned,)




#---------------------------------------------------------------------------------------------------------------------------------------------------
#class NepPipeIn 
 
#---------------------------------------------------------------------------------------------------------------------------------------------------
#class NepPipeOut
 
#---------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------------------



NODE_CLASS_MAPPINGS = {
    "NepXOR_INT_INT": NepXOR_INT_INT,
    "Remove First or Last From Batch (NEP)": NepRemoveFirstOrLastImageFromBatch,
    "Resolution from Ratio (NEP)": NepRatioResolution,
    "NepWanResolutions": NepWanResolutions, 
    "NepSafeString": NepSafeString,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NepXOR_INT_INT": "XOR (Nep)",
    "NepRemoveFirstOrLastImageFromBatch": "Remove First or Last From Batch (NEP)",
    "NepRatioResolution": "Resolution from Ratio (NEP)",
    "NepWanResolutions": "WAN Resolutions (NEP)",
    "NepSafeString": "Safe String (NEP)",
}