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

class NepStylesCat:
    """
    A node that organizes styles into categories and applies prefix/suffix.
    """

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        categories = list(STYLE_PRESETS_CAT.keys())

        return {
            "required": {
                "category": (categories, {}),
                "style": ([], {"dynamic": True}),
            },
            "optional": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("prompt", "prefix", "suffix", "category","stylename")
    FUNCTION = "addStyle"
    CATEGORY = "NepNodes"
    OUTPUT_TOOLTIPS = ("The styled prompt", "prefix", "suffix")

    @classmethod
    def VALIDATE_INPUTS(cls, category, style, **kwargs):
        """Dynamically regenerate the style dropdown when category changes."""
        if category is None:
            return {}
        styles = list(STYLE_PRESETS[category].keys())
        return {"style": styles}

    def addStyle(self, category, style, prompt=""):
        prefix = STYLE_PRESETS_CAT[category][style]["prefix"]
        suffix = STYLE_PRESETS_CAT[category][style]["suffix"]
        stylename = f"{category}-{style}"

        base = prompt.strip() if prompt else ""
        result = f"{prefix}\n{base}\n{suffix}"

        return (result, prefix, suffix, category, stylename)

#---------------------------------------------------------------------------------------------------------------------------------------------------#

NODE_CLASS_MAPPINGS = {
    "NepStyles": NepStyles,
    "NepStylesCat": NepStylesCat,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NepStyles": "Styles (NEP)",
    "NepStylesCat": "Styles II (NEP)",
}