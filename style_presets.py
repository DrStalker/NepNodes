
# Put a "/"  in the key for a style and rgthree's "show nested directories" will sort out putting things into folders.
FAV="Favorites/"
WIP="WIP/"
PHOTO="Photography/"
ART="Art/"
ANIME="Anime/"
ARTIST="Artists/"
MOOD="Mood/"
GEN="General/"
ERA="Era/"
MISC="Misc/"


STYLE_PRESETS = {
   
    # ------------------------------------------------------------------------------------
		"None": {"prefix":"","suffix":""}, #Keep this at the top so it's easy to turn off. Or maybe add a boolean to enable?
    # ------------------------------------------------------------------------------------
		FAV+"Photo": {
			"prefix": "A cinematic photograph, natural lighting",
			"suffix": "high contrast, professional photo, sharp focus"},    
      FAV + "Classic Film Photo": {
        "prefix": "A cinematic shot from a classic film with deep black shadows and warm earth tones. The film grain is visible. The scene, imbued with profound emotion, depicts: ", "suffix": ""},
		FAV+"Horror": {
			"prefix": "gothic horror, dramatic chiaroscuro lighting",
			"suffix": "heavy shadows, oppressive atmosphere, dark cinematic tone"},    
        FAV + "Horror Lite":{"prefix": "dramatic chiaroscuro lighting",
            "suffix": "heavy shadows, oppressive atmosphere,"},                
		FAV+"Digital Art Vibrant": {
			"prefix": "a highly detailed digital artwork, vibrant color grading, smooth shading, high contrast, cinematic contrast, semi-illustrated, semi-realistic",
			"suffix": ""},
        FAV + "Digital Art Dramatic":{"prefix": "digital painting, dramatic chiaroscuro lighting",
            "suffix": "heavy shadows, oppressive atmosphere,"},                

		FAV+"Greg-Rutkowski-Like": {
			"prefix": "high-fantasy digital painting with dramatic lighting and richly rendered detail,",
			"suffix": "epic composition, intricate highlights, atmospheric depth"},    
        FAV+"Flooded City":{
            "prefix": "digital illustration, A shadowy, atmospheric action scene, baroque gothic ornamentation, sketchy chaotic brushwork, red yellow rust palette, sulfurous yellows, blood reds, sickly greens, dark oppressive skies.  The composition uses extreme contrast and negative space to create dread and mystery, captured from a low, ominous angle that makes every figure loom like a monolith. fever-dream battlefield energy, ",
            "suffix": "Vingetting in the corners,  painterly grit and entropy  chaotic composition, textured traditional media feel, ink-smudged edges, raw painterly strokes, brutal gothic fantasy mood,"        },
        FAV+"Flooded City II":{
            "prefix": "most of the image is consumed by solid black ink, broken only by strategic silhouettes and dramatic spot colors digital illustration, A shadowy, atmospheric action scene, baroque gothic ornamentation, sketchy chaotic brushwork, red yellow rust palette, sulfurous yellows, blood reds, sickly greens, limited details in an otherwise black image.  The composition uses extreme negative space to create dread and mystery, captured from a low, ominous angle that makes every figure loom like a monolith. fever-dream battlefield energy, black skies, black background, extreme vignetting ",
            "suffix": "painterly grit and entropy  chaotic composition, textured traditional media feel, ink-smudged edges, raw painterly strokes, brutal gothic fantasy mood,"        },
        FAV + "horror sketch":{"prefix": "chaotic, punk-horror, ink-splatter illustration with rough, high-contrast black lines",
            "suffix": ""},    
        FAV + "Scribble Art": {
			"prefix": "(Loose spontaneous linework, continuous overlapping strokes, chaotic energetic contours, sketchy hand-drawn texture, abstract or semi-representational forms, ",
			"suffix": "dynamic movement, visible pressure variation, raw expressive mark-making with no clean outlines) "      },      
        FAV + "Bo-Golden":{
            "prefix": "bo-golden, dark fantasy,  a highly detailed digital artwork featureing a dark gothic fantasy theme ", # hyperrealistic photograph / cgi render, 
            "suffix": ""    },
		FAV+"Chiaroscuro Fantasy Sketch": {
		    "prefix": "Chiaroscuro Fantasy Sketch, extreme photorealistic style,  Rendered in bold, expressive pop-art style with halftone textures,",
		    "suffix": "low contrast, masterpiece, best quality, absurdres, highres, perfect anatomy, 8k wallpaper, ultra high quality, extremely detailed cg, perfect lighting, (sharp image) illustration),"},
		FAV+"Photo-oil": {
		    "prefix": "",
		    "suffix": "The photograph is rendered as oil painting on canvas with heavy brush strokes and deep rich colors, cinematic style reminiscent of Tim Burton's dark fantasy aesthetic. High-resolution detailing captures the gritty textures and intricacies in textures while maintaining a dreamlike quality to evoke a sense of fantasy and intrigue."},

    # ------------------------------------------------------------------------------------
		WIP+"SexyVintagePinup": {
			"prefix": "classic 1950s sexy pin-up illustration, retro glamour lighting, soft film grain, voluptuous curves, playful seductive pose, vintage color palette",
			"suffix": "sensual retro aesthetic, glossy magazine pin-up finish, painterly highlights, warm tones, elegant femininity, high detail"},
		WIP+"BurlesquePinup": {
			"prefix": "burlesque stage glamour, corsets and stockings, sultry theatrical lighting, vintage cabaret allure, exaggerated curves, sensual showgirl posing",
			"suffix": "glittering highlights, velvet textures, retro cabaret aesthetic, flirtatious drama, rich reds and golds, high detail"},
		WIP+"DarkNoirPinup": {
			"prefix": "sexy noir pin-up style, smoky shadows, moody low-key lighting, femme fatale pose, glossy red lips, dark film noir atmosphere",
			"suffix": "high contrast chiaroscuro, grainy noir texture, dramatic silhouettes, seductive tension, monochrome or muted palette, glossy finish"},
		WIP+"CheesecakePinup": {
			"prefix": "classic cheesecake pin-up art, playful innocent-sexy expression, bright soft lighting, pastel retro colors, exaggerated feminine curves",
			"suffix": "cute flirty tone, magazine-style polish, clean painterly finish, lighthearted glamour, smooth retro shading"},
		WIP+"ModernPinupFusion": {
			"prefix": "modern reinterpretation of vintage pin-up, contemporary glamour lighting, high-fashion sensual pose, bold colors, sleek modern styling blended with retro curves",
			"suffix": "ultra-polished beauty aesthetic, glossy highlights, high-resolution modern detailing, fusion-retro charm, vibrant and seductive"},
		WIP+"ExplicitNSFWPinup": {
			"prefix": "explicit erotic pin-up style, voluptuous curves in seductive NSFW posing, soft warm lighting, lustful expression, sultry vintage glamour with modern explicit edge",
			"suffix": "high-detail erotic finish, glossy sensual highlights, bold intimate framing, luxurious skin texture, intense sexual energy"},

        WIP+"Blanchitsu-Lite":{
 			"prefix": "digital illustration, red yellow rust palette, apocalyptic chaos aesthetic, scorched orange skies, baroque gothic ornamentation, sketchy chaotic brushwork, dirty parchment tones mixed with blood-red and rust,  skulls ornamentation,insanity and zealotry, fever-dream battlefield energy, painterly grit and entropy,",
			"suffix": "grimdark illustration, religious iconography ornamentation, chaotic composition, textured traditional media feel, ink-smudged edges, heavy contrast, stained parchment ambiance, raw painterly strokes, brutal gothic fantasy mood"},       


        WIP + "Cyberpunk Anime":{
        "prefix": "Cyberpunk Mecha Anime Style (Shirow Masamune/Katsuhiro Otomo influence, reminiscent of Ghost in the Shell or Akira), ",
        "suffix": "Cool, stark color palette dominated by deep blues, navy, and black in the background and shadows, strongly contrast between background and subjects"},                   
		WIP+"Cyberpunk anime II": {
		    "prefix": "anime, outlines, digital illustration, cyberpunk noir aesthetic, high-contrast teal-and-amber lighting, sharp graphic linework, metallic texture detailing, cinematic depth",
		    "suffix": "Lighting contrast divides the scene: teal one one side, amber on the other, both defining edges of clothing, plastic surfaces, dramatic dual-color lighting."},
		WIP+"Flash Photo": {
		    "prefix": "visible skin texture and micro-details, pronounced pore detail, minimal light diffusion, compact camera flash aesthetic, late 2000s to early 2010s digital photo style, ",
		    "suffix": "cool-to-neutral white balance, moderate digital noise in shadow areas, flat background separation, no cinematic grading, raw unfiltered realism, documentary snapshot look, true-to-life color but with flash-driven saturation, unsoftened texture."},
		#WIP+"Polaroid": {
		#    "prefix": "polaroid photo, light-leaking Polaroid filter,",
		#    "suffix": "Kodak Portra 400 look, subtle grain, vignette, warm-cool contrast, intimate cinematic portrait"},
		#WIP+"Hasselblad X2D": {
		#    "prefix": "Masterpiece photograph using a medium-format camera, depth of field, subsurface scattering, and perfect, cinematic, volumetric lighting.",
		#    "suffix": "Rich detail, textured fabrics, expressive faces, warm natural lighting, cinematic realism, subtle depth of field, high-resolution digital art"},
        WIP+"B&W classic portrait": { # Merge is some stuff from Illford Delta 3200??
            "prefix": "high-contrast black and white fine-art portrait photography, deep rich tonal range, precise zone-system exposure, crisp micro-detail, soft diffused key lighting, classic medium-format look, sculpted highlights and deep shadows, clean minimalist backdrop,",
            "suffix": "timeless fine-art realism, carefully controlled light and form, natural expression, strong textural definition, dramatic chiaroscuro, pure monochrome aesthetic, refined tonal control, gallery-quality portraiture"        },            


        # TO DO:
        # Oil paintings: https://www.reddit.com/r/StableDiffusion/comments/1phkr5i/zimage_feels_really_good_like_inpainting_with/
        

    # ------------------------------------------------------------------------------------
	    PHOTO+"Illford Delta 3200":{
            "prefix":"A black-and-white analog aged photograph",
            "suffix":"Illford Delta 3200 film, , push processing, film grain, high contrast, deep shadows and blown out highlights"},
    	PHOTO+"Medium Format": {
			"prefix": "medium-format film photograph, movie-still aesthetic", 
			"suffix": "cinematic lighting and rim lighting, soft film grain, shallow depth of field, soft film grain and Kodak Portra tones."},
    
        PHOTO+"Analog Photo": {
            "prefix": "analogue film photograph, grainy texture, soft contrast, warm tonal shifts,slight vignette, subtle chromatic aberration, shallow depth of field, vintage color palette,natural imperfections",
			"suffix": "captured on vintage film stock, gentle film grain, organic light falloff,faded highlights, muted shadows"},   

        PHOTO+"Dark Painterly Portrait": {
			"prefix": "moody painterly portrait style, dramatic chiaroscuro lighting, soft shadows,legant classical atmosphere,fine-art photography look, softly blended tones, cinematic depth",
			"suffix": "atmospheric vignette, soft falloff into darkness, highly sculpted light on the face, rich tonal contrast, refined fine-art mood"},   
        PHOTO+"Cinematic": {
            "prefix": "cinematic film still",
            "suffix": "shallow depth of field, vignette, highly detailed, high budget, bokeh, cinemascope, moody, epic, gorgeous, film grain, grainy"        },            
      PHOTO + "Vintage Candid Photo": { # from https://civitai.com/models/2181458/amazing-z-image-workflow
        "prefix": "A gritty, candid vintage photograph from a disposable camera, dark shadows and vibrant warm colors, featuring: ", "suffix": ""},
       PHOTO + "Casual Mobile Photo": { # from https://civitai.com/models/2181458/amazing-z-image-workflow
        "prefix": "# File Details\n * filename: DSC1000.JPG\n * source:  old Android phone\n\n# Photograph Details\n * Color  : vibrant\n * Style  : casual and amateur\n * Content: \n", "suffix": "\n"},
      PHOTO + "Lo-fi Mobile Photo": { # from https://civitai.com/models/2181458/amazing-z-image-workflow
        "prefix": "A raw documentary photograph taken with an old Android phone. This casual, low quality, amateur shot showcases ", "suffix": ""},
		PHOTO+"wet plate collodion portrait": {
		    "prefix": "wet plate collodion portrait, ultra-deep blacks, extreme high contrast, large-format tintype look, razor micro-detail, dramatic silver-gelatin tones, harsh falloff, soft halation, organic chemical artifacts, oxidized plate edges",
		    "suffix": "intense monochrome depth, crushed shadows, bright metallic highlights, chemical streaks, plate imperfections, plate streaking, historical analog texture, vintage chemical imperfections"},



    # ------------------------------------------------------------------------------------
		ART+"Digital Art": {
			"prefix": "masterpiece, best quality, amazing quality, highly detailed digital illustration, rich textures",
			"suffix": ""},      
		ART+"Epic-Concept-Art": {
			"prefix": "cinematic AAA concept art style, sweeping vistas, detailed structures,",
			"suffix": "heroic composition, atmospheric depth, ultra-polished rendering"},              
        ART+"Grim Baroque Engraving": {
            "prefix": "grimdark gothic fantasy aesthetic, scratchy ink textures, baroque cluttered details, medieval surrealism,",
            "suffix": "bleak palette, chaotic linework, decayed ornate motifs, brutal fantastical symbolism, antique occult atmosphere"        },         
		ART+"Victorian Storybook": {
		    "prefix": "whimsical fantasy sketch, style with loose expressive ink linework, soft sketchy contours, elongated and exaggerated character proportions, gentle watercolor washes in muted blues and earth tones, pale yellows, smoky grays, stained parchment background texture, playful yet slightly eerie atmosphere, ornate swirling costume details, lightly shaded forms with airy translucent layers,",
		    "suffix": "hand-drawn ink-and-watercolor aesthetic, textured paper grain, subtle ink bleed and splatter, warm antiqued color palette, soft gradients and uneven washes, lively expressive characters, dreamy storybook fantasy mood, traditional illustration finish."},
      ART + "Minimalist Sketchwash": { # from https://civitai.com/models/2181458/amazing-z-image-workflow
        "prefix": "A minimalist pencil sketch and watercolor painting, rendered with rough drawing style and pastel colors on a white background, featuring: . ", "suffix": ""},
      ART + "Simple Vector Illustration": { # from https://civitai.com/models/2181458/amazing-z-image-workflow
        "prefix": "A stylized digital illustration with a graphic design aesthetic, featuring flat, solid colors, no defined outlines, and a minimalist approach to composition, featuring: . ", "suffix": "Iconography style."},
		ART+"Comic Book": {
			"prefix": "Western comic-book illustration, bold outlines, graphic dramatic style,",
			"suffix": "halftone shading, vivid flat colors, dynamic heroic composition"},       
      ART + "Vintage Comic Panel": { # from https://civitai.com/models/2181458/amazing-z-image-workflow
        "prefix": "An old sheet of paper with a vintage erotic comic strip from 1950 painted in white, red, blue and black with freehand outlines, a detailed and dirty image featuring: ", "suffix": ""},
		ART+"Manga": {
			"prefix": "black-and-white manga illustration, strong inking, dramatic panel-style contrast,",
			"suffix": "screen-tone shading, stylized expressions, dynamic motion lines"},
        ART+"Digital Illustration": {
            "prefix": "Digital Illustration",
            "suffix": ""},              
        ART+"watercolor": {
            "prefix": "watercolor painting",
            "suffix": "vibrant, beautiful, painterly, detailed, textural, artistic"        },                
     # ------------------------------------------------------------------------------------
       
        ANIME + "Studio Anime": { # from https://civitai.com/models/2181458/amazing-z-image-workflow
        "prefix": "Epic anime filmed by Studio Ghibli, Japanese animation and hand-painted", "suffix": ""},
        ANIME + "Dark Anime": { # from https://civitai.com/models/2181458/amazing-z-image-workflow
            "prefix": "Dark fantasy masterpiece of cel_shading, with detailed anime violent style, featuring: ", "suffix": ""},
		ANIME+"90s-Anime-OVA": {
			"prefix": "1990s OVA anime aesthetic, sharp cel outlines, retro color palette,",
			"suffix": "grainy film texture, dramatic highlights, nostalgic shading style"},
		ANIME+"2000s-Cel-Digital-Hybrid": {
			"prefix": "early-2000s anime hybrid cel/digital look, bright saturated colors,",
			"suffix": "clean digital gradients, crisp character silhouettes"},	
		ANIME+"Retro-VHS-Anime": {
			"prefix": "retro VHS anime aesthetic, soft analog blur, muted colors,",
			"suffix": "chromatic bleeding, scanlines, tape noise artifacts"},	
        ANIME + "Red Rims":{ 
            "prefix": "A stylized digital illustration in comic line art style, rendered with professional, sleek, modern precision through vector graphics and graphic novel aesthetics. Employ a minimalist palette dominated by deep, enveloping shadows and negative space to evoke enigmatic stillness and cinematic tension, contrasted by saturated, vibrant highlights",
            "suffix": "faint red edge-lighting grazing contours, intense glowing accents piercing the darkness, and subtle glints of reflection along sharp, clean thick lines. Build quiet suspense with highly detailed yet restrained compositions, emphasizing stark contrasts between obscurity and luminous presence for a vibrant, graphic, and immersive visual impact."},
            

    # ------------------------------------------------------------------------------------
        ARTIST+"Blanchitsu-Like":{
 			"prefix": "digital illustration, red yellow rust palette, apocalyptic Warhammer chaos aesthetic, scorched orange skies, baroque gothic ornamentation, sketchy chaotic brushwork, dirty parchment tones mixed with blood-red and rust,  skulls and relics, ornate armor, insanity and zealotry, fever-dream battlefield energy, painterly grit and entropy,",
			"suffix": "grimdark illustration, medieval religious iconography, chaotic composition, textured traditional media feel, ink-smudged edges, heavy contrast, stained parchment ambiance, raw painterly strokes, brutal gothic fantasy mood, IN THE GRIM DARKNESS OF THE FAR FUTURE THERE IS ONLY WAR"},       
		ARTIST+"Dark Moebius-Like": {
			"prefix": "graphic surrealist fantasy with stark linework and eerie dreamlike architecture,",
			"suffix": "limited palette, angular compositions, uncanny atmospheric tension"},
		ARTIST+"Ghibli-Like": {
			"prefix": "whimsical hand-painted fantasy aesthetic with gentle storytelling atmosphere,",
			"suffix": "soft painterly lighting, warm palettes, lush environmental detail"},
		ARTIST+"Loish-Like": {
			"prefix": "smooth stylized character illustration with soft feminine shapes and warm expressive palettes,",
			"suffix": "painterly shading, gentle gradients, emotive storytelling focus"},
		ARTIST+"Syd Mead-Like": {
			"prefix": "sleek retro-futurist industrial design illustration, clean functional geometry,",
			"suffix": "polished surfaces, advanced tech motifs, cinematic sci-fi scale"},
		ARTIST+"Dark-Fantasy-Painterly": {
			"prefix": "dark high-fantasy digital painting, brooding atmosphere, dramatic shadows,",
			"suffix": "epic scale, mystical lighting, richly rendered environments"},
		ARTIST+"Renaissance": {
			"prefix": "renaissance classical painting style, balanced composition, naturalistic anatomy,",
			"suffix": "soft sfumato shading, muted warm tones, detailed drapery"},
		ARTIST+"Baroque": {
			"prefix": "dramatic baroque painting style, deep contrast, rich ornamental detail,",
			"suffix": "intense chiaroscuro lighting, grand expressive composition"},
		ARTIST+"Rococo": {
			"prefix": "light and ornate rococo painting style, pastel elegance, decorative curls,",
			"suffix": "playful romantic atmosphere, intricate ornamentation"},
		ARTIST+"Symbolist": {
			"prefix": "symbolist painting aesthetic, dreamlike imagery, poetic abstraction,",
			"suffix": "mystical motifs, rich evocative color symbolism"},
		ARTIST+"Fauvist": {
			"prefix": "bold fauvist painting, expressive wild brushstrokes, intense non-natural colors,",
			"suffix": "vivid contrast, emotional chromatic energy"},
		ARTIST+"Cubist": {
			"prefix": "geometric cubist abstraction, fragmented perspectives,",
			"suffix": "angular shapes, layered overlapping planes, muted analytical palette"},
        ARTIST+"Art Deco": {
            "prefix": "art deco style",
            "suffix": "geometric shapes, bold colors, luxurious, elegant, decorative, symmetrical, ornate, detailed"        },

    # ------------------------------------------------------------------------------------

        MOOD+"Gothic": {
            "prefix": "moody gothic atmosphere, muted desaturated colors, soft dramatic lighting, antique textures, somber yet readable tones,",
            "suffix": "subtle shadows, aged stone and weathered surfaces, baroque gloom, atmospheric depth without heavy darkness"},
        MOOD+"Dystopian": {
            "prefix": "dystopian style",
            "suffix": "bleak, post-apocalyptic, somber, dramatic, highly detailed"        },      
        MOOD+"Film Noir": {
            "prefix": "film noir style",
            "suffix": "monochrome, high contrast, dramatic shadows, 1940s style, mysterious, cinematic"        },
        MOOD+"Post-Apocalyptic": {
            "prefix": "post-apocalyptic wasteland aesthetic, ruined structures, scavenged gear, desolate landscapes,",
            "suffix": "dusty muted colors, broken machinery, survival-worn textures, bleak atmospheric haze"        },
        MOOD+"Grunge": {
            "prefix": "grunge aesthetic, dirty textured surfaces, raw distressed materials,",
            "suffix": "oversaturated shadows, gritty urban decay, rough handmade visual noise"        },
    # ------------------------------------------------------------------------------------

      GEN + "Cyberpunk Neon": { # from https://civitai.com/models/2181458/amazing-z-image-workflow
        "prefix": "Black cyberpunk landscape photograph with dark atmosphere and glowing neon lights with satured colors", "suffix": ""},
        GEN+"Cyberpunk": {
            "prefix": "neon-drenched cyberpunk future,  rain-soaked streets, sleek urban tech,",
            "suffix": "glowing circuitry, reflective surfaces, high-tech grit, electric atmosphere"        },
        GEN+"Solarpunk": {
            "prefix": "bright solarpunk utopia, organic architecture, lush greenery integrated with technology,",
            "suffix": "sunlit renewable energy systems, harmonious eco-design, soft optimistic tones"        },
        GEN+"Dieselpunk": {
            "prefix": "dieselpunk retro-industrial world, heavy machinery, 1930s–40s engineered aesthetics,",
            "suffix": "gritty oil-stained textures, brass fittings, smoky atmospheric haze"        },
        GEN+"Atompunk": {
            "prefix": "retro-futuristic atompunk aesthetic, mid-century modern sci-fi optimism, chrome curves,",
            "suffix": "atomic-age motifs, bright vintage colors, clean streamlined technology"        },
		GEN+"Steampunk": {
		    "prefix": "steampunk style ",
		    "suffix": "antique, mechanical, brass and copper tones, gears, intricate, detailed"},
		GEN+"Painterly-Steampunk": {
			"prefix": "steampunk fantasy painting, brass machinery, Victorian industrial mood,",
			"suffix": "cogs, rivets, warm antique metal tones"},            
        GEN+"Neonpunk": {
            "prefix": "neonpunk style",
            "suffix": "cyberpunk, vaporwave, neon, vibes, vibrant, stunningly beautiful, crisp, detailed, sleek, ultramodern, magenta highlights, dark purple shadows, high contrast, cinematic, ultra detailed, intricate, professional"        },
        GEN+"Futuristic Sci Fi": {
            "prefix": "sci-fi style",
            "suffix": "futuristic, technological, alien worlds, space themes, advanced civilizations"        },
        GEN+"Futuristic Vaporwave": {
            "prefix": "vaporwave style",
            "suffix": "retro aesthetic, cyberpunk, vibrant, neon colors, vintage 80s and 90s style, highly detailed"        },        
        GEN+"Nebula Witchcraft": {         # I ask an LLM to make the weirest styles it could think of....this is the only one that worth keeping
            "prefix": "cosmic witchcraft infused with nebula dust, swirling astral vapors, stellar incantations,",
            "suffix": "starfire glow, spectral spell trails, vast magical deep-space haze"        },        
		GEN+"SciFi-Hard-Surface": {
			"prefix": "sleek hard-surface sci-fi illustration, advanced materials,",
			"suffix": "polished metallic detailing, industrial futuristic design"},
		GEN+"Retro-Space-Opera": {
			"prefix": "retro space-opera aesthetic, vibrant pulp sci-fi colors,",
			"suffix": "heroic cosmic scenes, vintage futurism"},
        GEN+"sai-3d-model": {
            "prefix": "professional 3d model.",
            "suffix": "octane render, highly detailed, volumetric, dramatic lighting"},        
        GEN+"Ethereal Fantasy": {
            "prefix": "ethereal fantasy concept art of",
            "suffix": "magnificent, celestial, ethereal, painterly, epic, majestic, magical, fantasy art, cover art, dreamy"        },
        GEN+"Neon Noir": {   
            "prefix": "neon noir",
            "suffix": "cyberpunk, dark, rainy streets, neon signs, high contrast, low light, vibrant, highly detailed"        },

    # ------------------------------------------------------------------------------------

		ERA+"1800s photo": {
			"prefix": "1800s photographic plate",
			"suffix": "sepia daguerreotype style, aged texture, damaged film, antique photographic imperfections"},
		ERA+"1950s": {
			"prefix": "1950s aesthetic, black-and-white broadcast look, bright three-point stage lighting,",
			"suffix": "flat theatrical studio sets, low contrast, soft analog tube-camera grain, classic TV framing"},
		ERA+"1960s": {
			"prefix": "1960s aesthetic, warm early color television look, theatrical multi-cam lighting,",
			"suffix": "saturated painted sets, mild analog softness, simplified mid-century décor"},
		ERA+"1970s": {
			"prefix": "1970s aesthetic, film-to-tape broadcast look, warm earthy tones, practical lighting,",
			"suffix": "wood paneling, orange-brown retro palette, analog grain, wide studio framing"},
		ERA+"1980s": {
			"prefix": "1980s aesthetic, bright multi-camera studio look, crisp tube-camera highlights,",
			"suffix": "bold pastel set colors, fluorescent lighting, VHS-level softness, laugh-track framing"},
		ERA+"1990s": {
			"prefix": "1990s aesthetic, polished network multi-cam production, clean broadcast color science,",
			"suffix": "apartment and suburban sets, soft edge lighting, light analog grain"},
		ERA+"British-Sitcom": {
			"prefix": "1970s British sitcom aesthetic, low-budget studio lighting, muted color palette,",
			"suffix": "basic practical sets, soft analog video texture, theatrical staging"},
        
    # ------------------------------------------------------------------------------------

		MISC+"Pixel Art": {
			"prefix": "retro pixel art illustration, crisp pixel grid,",
			"suffix": "limited palette, 8-bit/16-bit aesthetic, nostalgic game style"},
        MISC+"Tilt Shift": {
            "prefix": "tilt-shift photo of",
            "suffix": "selective focus, miniature effect, blurred background, highly detailed, vibrant, perspective control"        },            
        MISC+"Cyberpunk Game": {
            "prefix": "cyberpunk game style",
            "suffix": "neon, dystopian, futuristic, digital, vibrant, detailed, high contrast, reminiscent of cyberpunk genre video games"        },
        MISC+"Fighting Game": {
            "prefix": "fighting game style",
            "suffix": "dynamic, vibrant, action-packed, detailed character design, reminiscent of fighting video games"        },
        MISC+"RPG Fantasy Game": {
            "prefix": "role-playing game (RPG) style fantasy",
            "suffix": "detailed, vibrant, immersive, reminiscent of high fantasy RPG games"        },
        MISC+"Stained Glass": {
            "prefix": "stained glass style",
            "suffix": "vibrant, beautiful, translucent, intricate, detailed"        },
        MISC+"Stacked Papercut": {
            "prefix": "stacked papercut art of",
            "suffix": "3D, layered, dimensional, depth, precision cut, stacked layers, papercut, high contrast"        },
        MISC+"Long Exposure": {
            "prefix": "long exposure photo of",
            "suffix": "Blurred motion, streaks of light, surreal, dreamy, ghosting effect, highly detailed"        },
}


		##"XXXX": {
		##    "prefix": "",
		##    "suffix": ""},

		##"XXXX": {
		##    "prefix": "",
		##    "suffix": ""},

		##"XXXX": {
		##    "prefix": "",
		##    "suffix": ""},


		##"XXXX": {
		##    "prefix": "",
		##    "suffix": ""},
   