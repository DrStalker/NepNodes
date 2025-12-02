import comfy.utils

#---------------------------------------------------------------------------------------------------------------------------------------------------#

class NepStyles:
    """
    A node that lets the user choose a style preset (prefix + suffix)
    and optionally attaches them around an incoming prompt.
    """    
    STYLE_PRESETS = {
        "None": {"prefix":"","suffix":""},
        "Photo": {
            "prefix": "A cinematic photograph, natural lighting",
            "suffix": "high contrast, professional photo, sharp focus"},
        "Digital Art": {
            "prefix": "masterpiece, best quality, amazing quality, highly detailed digital illustration, rich textures",
            "suffix": ""},
        "Semi-real Art": {
            "prefix": "a highly detailed digital artwork, vibrant color grading, smooth shading, high contrast, cinematic contrast, semi-illustrated, semi-realistic",
            "suffix": ""},
        "Medium Format": {
            "prefix": "medium-format film photograph, movie-still aesthetic", 
            "suffix": "cinematic key and rim lighting, soft film grain, shallow depth of field, soft film grain and Kodak Portra tones."},
        "1800s photo": {
            "prefix": "1800s photographic plate",
            "suffix": "sepia daguerreotype style, aged texture, damaged film, antique photographic imperfections"},
        "dark gothic": {
            "prefix": "gritty gothic, dramatic chiaroscuro lighting",
            "suffix": "heavy shadows, oppressive atmosphere, dark cinematic tone"},    
        "cel shaded": {
            "prefix": "high-quality cel-shaded illustration, bold stylized linework,",
            "suffix": "vibrant palette, crisp outlines, polished cel-animation aesthetic"},
        "fashion": {    
            "prefix": "cinematic high-fashion editorial photograph, dramatic posing and lighting",
            "suffix": "moody rich palette (burgundy, mustard, midnight blue), gothic couture, baroque fashion aesthetic, hyper-real textures, 8k detail, shot on 35mm film with shallow depth of field and soft bokeh"},
        "Anime": {
            "prefix": "high-quality anime illustration, clean linework, expressive lighting,",
            "suffix": "soft shading, vibrant color palette, polished modern anime aesthetic"
        },

        "Ghibli": {
            "prefix": "Studio Ghibli-style illustration, painterly charm, warm whimsical atmosphere,",
            "suffix": "soft watercolor textures, gentle lighting, hand-painted backgrounds, magical realism"
        },

        "Manga": {
            "prefix": "black-and-white manga illustration, strong inking, dramatic panel-style contrast,",
            "suffix": "screen-tone shading, stylized expressions, dynamic motion lines"
        },

        "Comic Book": {
            "prefix": "Western comic-book illustration, bold outlines, graphic dramatic style,",
            "suffix": "halftone shading, vivid flat colors, dynamic heroic composition"
        },            
        "Cartoon": {
            "prefix": "cartoon-style illustration, bold outlines, exaggerated expressions,",
            "suffix": "flat colors, smooth shapes, playful and energetic aesthetic"
        },
        "Pixel Art": {
            "prefix": "retro pixel art illustration, crisp pixel grid,",
            "suffix": "limited palette, 8-bit/16-bit aesthetic, nostalgic game style"
        },
        "Moebius-Like": {
            "prefix": "clean-line graphic novel illustration with surreal sci-fi landscapes, flat yet vibrant colors,",
            "suffix": "precise contour lines, dreamy retro-futurist aesthetic, elegant minimalist shading"
        },
        "Dark Moebius-Like": {
            "prefix": "graphic surrealist fantasy with stark linework and eerie dreamlike architecture,",
            "suffix": "limited palette, angular compositions, uncanny atmospheric tension"
        },
        "Ghibli-Like": {
            "prefix": "whimsical hand-painted fantasy aesthetic with gentle storytelling atmosphere,",
            "suffix": "soft painterly lighting, warm palettes, lush environmental detail"
        },
        "Loish-Like": {
            "prefix": "smooth stylized character illustration with soft feminine shapes and warm expressive palettes,",
            "suffix": "painterly shading, gentle gradients, emotive storytelling focus"
        },

        "Studio Trigger-Style": {
            "prefix": "dynamic anime action aesthetic with bold silhouettes and energetic shapes,",
            "suffix": "high-contrast cel shading, extreme motion exaggeration, neon highlights"
        },

        "Greg-Rutkowski-Like": {
            "prefix": "high-fantasy digital painting with dramatic lighting and richly rendered detail,",
            "suffix": "epic composition, intricate highlights, atmospheric depth"
        },

        "Syd Mead-Inspired": {
            "prefix": "sleek retro-futurist industrial design illustration, clean functional geometry,",
            "suffix": "polished surfaces, advanced tech motifs, cinematic sci-fi scale"
        },

        "Giger-Like": {
            "prefix": "biomechanical dark surrealism with intricate organic machinery,",
            "suffix": "cold metallic textures, gothic techno-organic atmosphere"
        },    
        ##"XXXX": {
        ##    "prefix": "",
        ##    "suffix": ""},

    }       

    def init(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "style": (list(cls.STYLE_PRESETS.keys()),),
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
        prefix = self.STYLE_PRESETS[style]["prefix"]  
        suffix = self.STYLE_PRESETS[style]["suffix"] 
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