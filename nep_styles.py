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
        "Digital Art Vibrant": {
            "prefix": "a highly detailed digital artwork, vibrant color grading, smooth shading, high contrast, cinematic contrast, semi-illustrated, semi-realistic",
            "suffix": ""},
        "Medium Format": {
            "prefix": "medium-format film photograph, movie-still aesthetic", 
            "suffix": "cinematic key and rim lighting, soft film grain, shallow depth of field, soft film grain and Kodak Portra tones."},
        "1800s photo": {
            "prefix": "1800s photographic plate",
            "suffix": "sepia daguerreotype style, aged texture, damaged film, antique photographic imperfections"},
        "gothic": {
            "prefix": "gothic, dramatic chiaroscuro lighting",
            "suffix": "heavy shadows,"},    
        "horror": {
            "prefix": "gothic horror, dramatic chiaroscuro lighting",
            "suffix": "heavy shadows, oppressive atmosphere, dark cinematic tone"},    
        "cel shaded": {
            "prefix": "high-quality cel-shaded illustration, bold stylized linework,",
            "suffix": "vibrant palette, crisp outlines, polished cel-animation aesthetic"},
        "gothic couture": {    
            "prefix": "cinematic high-fashion editorial photograph, dramatic posing and lighting",
            "suffix": "moody rich palette, gothic couture, baroque fashion aesthetic, hyper-real textures, 8k detail, shot on 35mm film with shallow depth of field and soft bokeh"},
        "Anime": {
            "prefix": "high-quality anime illustration, clean linework, expressive lighting,",
            "suffix": "soft shading, vibrant color palette, polished modern anime aesthetic"
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

        "Studio Trigger-Like": {
            "prefix": "dynamic anime action aesthetic with bold silhouettes and energetic shapes,",
            "suffix": "high-contrast cel shading, extreme motion exaggeration, neon highlights"
        },

        "Greg-Rutkowski-Like": {
            "prefix": "high-fantasy digital painting with dramatic lighting and richly rendered detail,",
            "suffix": "epic composition, intricate highlights, atmospheric depth"
        },

        "Syd Mead-Like": {
            "prefix": "sleek retro-futurist industrial design illustration, clean functional geometry,",
            "suffix": "polished surfaces, advanced tech motifs, cinematic sci-fi scale"
        },

        "Giger-Like": {
            "prefix": "biomechanical dark surrealism with intricate organic machinery,",
            "suffix": "cold metallic textures, gothic techno-organic atmosphere"
        },    
        "80s-Cartoons": {
            "prefix": "1980s Saturday-morning cartoon aesthetic, bold cel outlines, limited animation style,",
            "suffix": "flat color fills, chunky shading, retro TV palette, grainy analog softness, heroic dramatic poses"
        },	
        
        "80s-Toy-Commercial-Cartoon": {
            "prefix": "1980s toy-commercial action cartoon aesthetic, heroic exaggerated proportions, bold cel linework,",
            "suffix": "vivid saturated toy-like colors, chunky shadow blocks, dramatic freeze-frame poses, retro analog softness, high-energy action framing"
        },	
        "Dark-Fantasy-Painterly": {
            "prefix": "dark high-fantasy digital painting, brooding atmosphere, dramatic shadows,",
            "suffix": "epic scale, mystical lighting, richly rendered environments"
        },

        "Epic-Concept-Art": {
            "prefix": "cinematic AAA concept art style, sweeping vistas, detailed structures,",
            "suffix": "heroic composition, atmospheric depth, ultra-polished rendering"
        },

        "Painterly-Dragon-Concept": {
            "prefix": "fantasy creature concept art, powerful dragon forms, dramatic lighting,",
            "suffix": "scaled textures, atmospheric smoke and embers"
        },

        "SciFi-Hard-Surface": {
            "prefix": "sleek hard-surface sci-fi illustration, advanced materials,",
            "suffix": "polished metallic detailing, industrial futuristic design"
        },

        "Cyber-Fantasy": {
            "prefix": "neon-lit cyber-fantasy illustration combining magic and tech,",
            "suffix": "glowing sigils, holographic elements, arcane energy effects"
        },

        "Painterly-Steampunk": {
            "prefix": "steampunk fantasy painting, brass machinery, Victorian industrial mood,",
            "suffix": "cogs, rivets, warm antique metal tones"
        },

        "Retro-Space-Opera": {
            "prefix": "retro space-opera aesthetic, vibrant pulp sci-fi colors,",
            "suffix": "heroic cosmic scenes, vintage futurism"
        },

        "Organic-Biotech": {
            "prefix": "organic biomechanical sci-fi illustration, flowing bio-metal structures,",
            "suffix": "alien textures, eerie synthetic-organic fusion"
        },

        "90s-Anime-OVA": {
            "prefix": "1990s OVA anime aesthetic, sharp cel outlines, retro color palette,",
            "suffix": "grainy film texture, dramatic highlights, nostalgic shading style"
        },

        "2000s-Cel-Digital-Hybrid": {
            "prefix": "early-2000s anime hybrid cel/digital look, bright saturated colors,",
            "suffix": "clean digital gradients, crisp character silhouettes"
        },	
        
        "Retro-VHS-Anime": {
            "prefix": "retro VHS anime aesthetic, soft analog blur, muted colors,",
            "suffix": "chromatic bleeding, scanlines, tape noise artifacts"
        },	
        
        "Cute-Chibi": {
            "prefix": "adorable chibi-style illustration, oversized expressive faces,",
            "suffix": "simple round shapes, playful pastel colors"
        },

        "Painterly-Anime-Fantasy": {
            "prefix": "anime-inspired painterly fantasy style, lush magical settings,",
            "suffix": "soft light scattering, ornate atmospheric effects"
        },

        "Cel-Anime-Flat": {
            "prefix": "classical cel-anime flat shading, bold outlines, limited tone variations,",
            "suffix": "solid color fills, crisp character silhouettes"
        },	
        

        "Baroque": {
            "prefix": "dramatic baroque painting style, deep contrast, rich ornamental detail,",
            "suffix": "intense chiaroscuro lighting, grand expressive composition"
        },

        "Renaissance": {
            "prefix": "renaissance classical painting style, balanced composition, naturalistic anatomy,",
            "suffix": "soft sfumato shading, muted warm tones, detailed drapery"
        },

        "Rococo": {
            "prefix": "light and ornate rococo painting style, pastel elegance, decorative curls,",
            "suffix": "playful romantic atmosphere, intricate ornamentation"
        },

        "Symbolist": {
            "prefix": "symbolist painting aesthetic, dreamlike imagery, poetic abstraction,",
            "suffix": "mystical motifs, rich evocative color symbolism"
        },

        "Fauvist": {
            "prefix": "bold fauvist painting, expressive wild brushstrokes, intense non-natural colors,",
            "suffix": "vivid contrast, emotional chromatic energy"
        },

        "Cubist": {
            "prefix": "geometric cubist abstraction, fragmented perspectives,",
            "suffix": "angular shapes, layered overlapping planes, muted analytical palette"
        },

        "Surrealist": {
            "prefix": "surrealist dreamlike environment, uncanny juxtapositions,",
            "suffix": "symbolic imagery, ethereal and irrational atmosphere"
        },	
        
        "Sitcom-1950s": {
            "prefix": "1950s sitcom aesthetic, black-and-white broadcast look, bright three-point stage lighting,",
            "suffix": "flat theatrical studio sets, low contrast, soft analog tube-camera grain, classic TV framing"
        },

        "Sitcom-1960s": {
            "prefix": "1960s sitcom aesthetic, warm early color television look, theatrical multi-cam lighting,",
            "suffix": "saturated painted sets, mild analog softness, simplified mid-century décor"
        },

        "Sitcom-1970s": {
            "prefix": "1970s sitcom aesthetic, film-to-tape broadcast look, warm earthy tones, practical lighting,",
            "suffix": "wood paneling, orange-brown retro palette, analog grain, wide studio framing"
        },

        "Sitcom-1980s": {
            "prefix": "1980s sitcom aesthetic, bright multi-camera studio look, crisp tube-camera highlights,",
            "suffix": "bold pastel set colors, fluorescent lighting, VHS-level softness, laugh-track framing"
        },

        "Sitcom-1990s": {
            "prefix": "1990s sitcom aesthetic, polished network multi-cam production, clean broadcast color science,",
            "suffix": "apartment and suburban sets, soft edge lighting, light analog grain"
        },

        "Sitcom-2000s": {
            "prefix": "2000s sitcom aesthetic, sharp early-digital broadcast look, clean modern lighting,",
            "suffix": "minimal grain, bright contemporary sets, high-key multi-cam framing"
        },

        "British-Sitcom-1970s": {
            "prefix": "1970s British sitcom aesthetic, low-budget studio lighting, muted color palette,",
            "suffix": "basic practical sets, soft analog video texture, theatrical staging"
        },

        "British-Sitcom-1980s": {
            "prefix": "1980s British sitcom broadcast look, flat multi-cam lighting, grey and beige set tones,",
            "suffix": "tube-camera softness, minimalistic set dressing, understated comedic framing"
        },

        "British-Sitcom-1990s": {
            "prefix": "1990s British sitcom aesthetic, early digital-to-tape look, muted naturalistic colors,",
            "suffix": "modest apartment or pub sets, subtle grain, restrained multi-cam lighting"
        },

        "British-Sitcom-2000s": {
            "prefix": "2000s British sitcom aesthetic, clean digital studio look, neutral color grading,",
            "suffix": "bright but simple sets, minimal grain, straightforward multi-camera composition"
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