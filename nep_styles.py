from .style_presets import STYLE_PRESETS 
from .style_presets_cat import STYLE_PRESETS as STYLE_PRESETS_CAT
#---------------------------------------------------------------------------------------------------------------------------------------------------#

class NepStyles:
    """
    A node that lets the user choose a style preset (prefix + suffix)
    and optionally attaches them around an incoming prompt.
    """    
    def init(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "style": (list(STYLE_PRESETS.keys()),),
            },
            "optional": {
                "prompt": ("STRING", {"default": "", "multiline": True}),                
            }
        }
    RETURN_TYPES = ("STRING","STRING","STRING","STRING",)
    RETURN_NAMES = ("prompt","prefix","suffix","stylename",)
    FUNCTION = "addStyle"
    CATEGORY="NepNodes"
    OUTPUT_TOOLTIPS = ("The styled prompt","the style's prefix","the styles suffix")

    def addStyle(self,style,prompt=""):
        prefix = STYLE_PRESETS[style]["prefix"]  
        suffix = STYLE_PRESETS[style]["suffix"] 
        stylename = style
        base = prompt.strip() if prompt else ""
        result = f"{prefix}\n{base}\n{suffix}"
        return (result,prefix,suffix,stylename)
        

#---------------------------------------------------------------------------------------------------------------------------------------------------#

class NepStylesNoApply:
    """
    A node that lets the user choose a style preset (prefix + suffix)
    """    
    def init(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "style": (list(STYLE_PRESETS.keys()),),
            },
        }
    RETURN_TYPES = ("STRING","STRING","STRING",)
    RETURN_NAMES = ("prefix","suffix","stylename",)
    FUNCTION = "getStyle"
    CATEGORY="NepNodes"
    OUTPUT_TOOLTIPS = ("the style's prefix","the styles suffix","the name of the chosen style")

    def addStyle(self,style,):
        prefix = STYLE_PRESETS[style]["prefix"]  
        suffix = STYLE_PRESETS[style]["suffix"] 
        stylename = style
        return (prefix,suffix,stylename)

#---------------------------------------------------------------------------------------------------------------------------------------------------#
#This doesn't hook up to the style combo box so I need to figure out how to make the input/out tyles match, like "sampler" and other stuff that is chosen from a list matches.
class NepStylesPicker:
    def init(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "style": (list(STYLE_PRESETS.keys()),),
            },
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("style",)
    FUNCTION = "retStyle"
    CATEGORY="NepNodes"
    OUTPUT_TOOLTIPS = ("The styled prompt","the style's prefix","the styles suffix")
    def retStyle(self,style):
        return(style)
#---------------------------------------------------------------------------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------------------------------------------------------------------------#

NODE_CLASS_MAPPINGS = {
    "NepStyles": NepStyles,
    "NepStylesNoApply": NepStylesNoApply,
    "NepStylesPicker": NepStylesPicker,

}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NepStyles": "Styles (NEP)",
    "NepStylesNoApply": "Styles No Apply (NEP)",
    "NepStylesPicker": "Style Picker (NEP)"

}