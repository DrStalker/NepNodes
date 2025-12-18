"""
@author: Nepenthe
@title: NepNodes Custom Nodes for ComfyUI
@nickname: NepNodes
@description: Personal Nodes
"""


import math
import re
import sys
import os
from decimal import Decimal, ROUND_HALF_UP, getcontext

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
    ratio = ["1:1", "5:4", "4:3", "3:2", "16:10","16:9","2:1","US Letter", "A4", "Force 1080p", "Force 2k"]
    orientation = ["portrait", "landscape"]
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ratio": (s.ratio,),
                "orientation": (s.orientation,),
                "megapixels": ("FLOAT", {"default": 1,"min":0.1,"max":100}),
            }
        }
    RETURN_TYPES = ("INT","INT","FLOAT","FLOAT")
    RETURN_NAMES = ("width", "height", "ratio", "megapixels")
    FUNCTION = "get_resolutions_from_ratio"

    CATEGORY="NepNodes"
    def get_resolutions_from_ratio(self,ratio,megapixels,orientation):
        
        megapixelsout=megapixels
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
        elif(ratio == "5:2"): 
            rationum = float(2.5)
        elif(ratio == "3:1"): 
            rationum = float(3)
        elif(ratio == "US Letter"): 
            rationum = float(11/8.5)
        elif(ratio == "A4"): 
            rationum = float(297/210)

        total_pixels = megapixels * 1024 * 1024
        width = math.sqrt(total_pixels * rationum)
        height = width / rationum
        def round16(x):
            return int(round(x / 16) * 16)  
        def round4(x):
            return int(round(x / 4) * 4)        
        width = round16(width)    # Z-Image likes multiples of 16, I think.
        height = round16(height)  
        if(ratio == "Force 1080p"): 
            width, height = 1920, 1080 # 1080 is not divisible  by 16, so might cause issues?  
            megapixelsout = (1920 * 1080) / (1024 * 1024) # 1.98
        elif(ratio == "Force 2k"): 
            width, height = 2560, 1440
            megapixelsout = (2560 * 1440) / (1024 * 1024) # 3.52

        if orientation  == "portrait":
            if width > height:
                width, height = height, width
        else:
            if height > width:
                width, height = height, width

        return(width, height, rationum, megapixelsout)

#---------------------------------------------------------------------------------------------------------------------------------------------------#

# based on JPS tools multiply
class NepXOR_INT_INT:

    def __init__(self):
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

class NepSwitchIntsOnBool:

    def __init__(self):
        pass    

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "true1": ("INT", {"default": 0,"min":-1000000000000000,"max":1000000000000000}),
                "true2": ("INT", {"default": 0,"min":-1000000000000000,"max":1000000000000000}),
                "true3": ("INT", {"default": 0,"min":-1000000000000000,"max":1000000000000000}),
                "true4": ("INT", {"default": 0,"min":-1000000000000000,"max":1000000000000000}),
                "false1": ("INT", {"default": 0,"min":-1000000000000000,"max":1000000000000000}),
                "false2": ("INT", {"default": 0,"min":-1000000000000000,"max":1000000000000000}),
                "false3": ("INT", {"default": 0,"min":-1000000000000000,"max":1000000000000000}),
                "false4": ("INT", {"default": 0,"min":-1000000000000000,"max":1000000000000000}),
                "mode": ("BOOLEAN", {"default": False,}),                
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT", "INT",)
    RETURN_NAMES = ("out1", "out2", "out3", "out4", )
    FUNCTION = "chooseints"
    CATEGORY = "NepNodes"

    def chooseints(self, mode, true1, true2, true3, true4, false1, false2, false3, false4, ):
        if mode:
            return (true1, true2, true3, true4, )
        return (false1, false2, false3, false4,)
        
#---------------------------------------------------------------------------------------------------------------------------------------------------#

class NepSwitchOneFloatOnBool:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "float_true": ("FLOAT",),
                "float_false": ("FLOAT",),
                "mode": ("BOOLEAN", {"default": False,}), 
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "choosefloat"
    CATEGORY = "NepNodes"

    def choosefloat(self, float_true, float_false, mode=True):

        if mode:
            return (float_true, )
        else:
            return (float_false, )
        
#---------------------------------------------------------------------------------------------------------------------------------------------------#

class NepSwitchOneIntOnBool:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "int_true": ("INT",),
                "int_false": ("INT",),
                "mode": ("BOOLEAN", {"default": False,}), 
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "chooseint"
    CATEGORY = "NepNodes"

    def chooseint(self, int_true, int_false, mode=True):

        if mode:
            return (int_true, )
        else:
            return (int_false, )        
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
    #Replaces removed characters with a new string (shcih can be empty)
    #""""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": ""}),
                "replacement": ("STRING", {"multiline": False, "default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("clean_text",)
    FUNCTION = "maketextsafe"
    CATEGORY = "NepNodes"

    INVALID_CHARS = r'[\\/:*?"<>|\n\r\t]'

    def maketextsafe(self, text,replacement=""):
        if len(text) > 100:  #Max 100 characters
            text = text[:100]
        cleaned = re.sub(self.INVALID_CHARS, replacement, text)
        cleaned = cleaned.strip()
        return (cleaned,)


#---------------------------------------------------------------------------------------------------------------------------------------------------
class NepTooManyInputs:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "threshold": ("INT", {"default": 1, "min": 0}),
            },
            "optional": {
                "value1": ("*",""),   # accept ANY type
                "value2": ("*",""),
                "value3": ("*",""),
                "value4": ("*",""),
            }            
        }

    RETURN_TYPES = ("BOOL",)
    RETURN_NAMES = ("result",)
    FUNCTION = "compute"
    CATEGORY = "NepNodes"

    def compute(self, value1, value2, value3, value4, threshold):
        # Count how many inputs are NOT None
        non_none_count = sum(v is not None for v in (value1, value2, value3, value4))
        return (non_none_count > threshold,)




#---------------------------------------------------------------------------------------------------------------------------------------------------
class NepPrintStringIfTrue:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "trigger": ("BOOL", {"default": False}),
                "text": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "run"
    CATEGORY = "NepNodes"

    def run(self, trigger, text):
        if trigger:
            # ANSI 
            color_code = "\033[96m"   # bright cyan
            reset_code = "\033[0m"
            print(f"{color_code}{text}{reset_code}", file=sys.stdout, flush=True)

        return (text,)
 
#---------------------------------------------------------------------------------------------------------------------------------------------------
class NepStripFileExtension:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "filename": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("basename",)
    FUNCTION = "strip_ext"
    CATEGORY = "NepNodes"

    def strip_ext(self, filename):
        # Extract file name without extension
        base = os.path.splitext(filename)[0]
        return (base,)
 
#---------------------------------------------------------------------------------------------------------------------------------------------------
class RegexReplace:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": "", "multiline": True}),
                "pattern": ("STRING", {"default": ""}),
                "replacement": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply_regex"
    CATEGORY = "NepNodes"

    def apply_regex(self, text, pattern, replacement):
        try:
            output = re.sub(pattern, replacement, text)
        except re.error as e:
            output = f"[REGEX ERROR] {e}"
        return (output,)
#---------------------------------------------------------------------------------------------------------------------------------------------------


class NepRegexReplace:
    """
    returns re.sub(pattern, replacement, text)
    no being helpful, no screwing around with the output, just a simple and effective regular expession node.
    Provided you know how to write the expression you need.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": "", "multiline": True}),
                "pattern": ("STRING", {"default": ""}),
                "replacement": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("result",)
    FUNCTION = "apply_regex"
    CATEGORY = "NepNodes"

    def apply_regex(self, text, pattern, replacement):
        try:
            output = re.sub(pattern, replacement, text)
        except re.error as e:
            output = f"[REGEX ERROR] {e}"
        return (output,)


#---------------------------------------------------------------------------------------------------------------------------------------------------


class NepFloatRounderWithString:

    """
    A ComfyUI custom node that converts a float to a string with specified decimal places.
    Uses Decimal for precision handling to avoid floating point rounding issues.
    Also outputs the rounded float because that was useful one time in one workflow.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value": ("FLOAT", {"default": 0.0, "min": -1e10, "max": 1e10, "step": 0.05,"display": "number"}),
                "precision": ("INT", {"default": 2, "min": 0, "max": 16}),
            }
        }

    RETURN_TYPES = ("STRING","FLOAT")
    RETURN_NAMES = ("result_string","result_float")
    FUNCTION = "round_float"
    CATEGORY = "NepNodes"

    def round_float(self, value, precision):
        # Convert float to Decimal using string to avoid FP precision issues
        d = Decimal(str(value))
        # Set precision high enough to safely round
        getcontext().prec = max(28, precision + 5)
        # Create quantization pattern, e.g. "0.01"
        quant = Decimal("1").scaleb(-precision)
        # Round using HALF_UP (human-expected rounding)
        rounded = d.quantize(quant, rounding=ROUND_HALF_UP)
        # Format with fixed decimal places
        fmt = f"{{:.{precision}f}}"
        return (fmt.format(rounded),float(rounded))


#---------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------------------


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
    "NepSwitchIntsOnBool": NepSwitchIntsOnBool,
    "NepSwitchOneFloatOnBool": NepSwitchOneFloatOnBool,
    "NepSwitchOneIntOnBool": NepSwitchOneIntOnBool,
    "NepTooManyInputs": NepTooManyInputs,
    "NepPrintStringIfTrue": NepPrintStringIfTrue,
    "NepStripFileExtension": NepStripFileExtension,
    "NepRegexReplace": NepRegexReplace,
    "NepFloatRounderWithString": NepFloatRounderWithString,
}

NODE_DISPLAY_NAME_MAPPINGS = {

    "NepXOR_INT_INT": "XOR (Nep)",
    "NepRemoveFirstOrLastImageFromBatch": "Remove First or Last From Batch (NEP)",
    "NepRatioResolution": "Resolution from Ratio (NEP)",
    "NepWanResolutions": "WAN Resolutions (NEP)",
    "NepSafeString": "Safe String (NEP)",
    "NepSwitchIntsOnBool": "Switch 4xInts on bool (Nep)",
    "NepSwitchOneFloatOnBool": "Simple Float Switch (NEP)",
    "NepSwitchOneIntOnBool": "Simple Int Switch (NEP)",
    "NepTooManyInputs": "Nep Too Many Inputs (NEP)",
    "NepPrintStringIfTrue": "Print String If True (NEP)",
    "NepStripFileExtension": "Strip File Extension (NEP)",
    "NepRegexReplace": "Regex Replace (Nep)",
    "NepFloatRounderWithString": "Float2String (Nep)",
}