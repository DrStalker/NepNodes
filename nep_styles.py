import comfy.utils
from .style_presets import STYLE_PRESETS 
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

    def addStyle(self,style,prompt):
        prefix = STYLE_PRESETS[style]["prefix"]  
        suffix = STYLE_PRESETS[style]["suffix"] 
        stylename = style
        base = prompt.strip() if prompt else ""
        result = f"{prefix}\n{base}\n{suffix}"
        return (result,prefix,suffix,stylename)
        

#---------------------------------------------------------------------------------------------------------------------------------------------------#

NODE_CLASS_MAPPINGS = {
    "NepStyles": NepStyles,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NepStyles": "Styles (Nep)",

}