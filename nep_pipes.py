
import re
import comfy.samplers, comfy.supported_models


#---------------------------------------------------------------------------------------------------------------------------------------------------

# Taken from EasyUse and modified.

class NepPipeIn:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
             "required": {},
             "optional": {
                "pipe": ("NEPPIPELINE",),
                "model": ("MODEL",),
                "modelname": ("STRING",),
                "clip": ("CLIP",),
                "vae": ("VAE",),
                "steps": ("INT",),
                "cfg": ("FLOAT",),
                "sampler": ("STRING",),
                "samplername": ("STRING",),
                "scheduler": ("STRING",),
                "schedulername": ("STRING",),
            },
            "hidden": {"my_unique_id": "UNIQUE_ID"},
        }

    RETURN_TYPES = ("NEPPIPELINE",)
    RETURN_NAMES = ("pipe",)
    FUNCTION = "flush"

    CATEGORY = "EasyUse/Pipe"

    def flush(self, pipe=None, model=None, modelname=None, clip=None, vae=None, steps=None, cfg=None, sampler=None, samplername=None, scheduler=None, schedulername=None,  my_unique_id=None):

        if pipe is None:
            pipe = {"loader_settings": {"positive": "", "negative": "", "xyplot": None}}

        model =         model         if model is not None else pipe.get("model")
        modelname =     modelname     if (modelname is not None and modelname is not "") else pipe.get("modelname")
        clip =          clip          if clip is not None else pipe.get("clip")
        vae =           vae           if vae is not None else pipe.get("vae")
        steps =         steps         if (steps is not None and steps > 0) else pipe.get("steps")
        cfg =           cfg           if (cfg is not None and cfg > 0.0) else pipe.get("cfg")
        sampler =       sampler       if sampler is not None else pipe.get("sampler")
        samplername =   samplername   if (samplername is not None and samplername is not "") else pipe.get("samplername")
        scheduler =     scheduler     if scheduler is not None else pipe.get("scheduler")
        schedulername = schedulername if (schedulername is not None and schedulername is not "") else pipe.get("schedulername")




        new_pipe = {
            **pipe,
            "model":         model,         
            "modelname":     modelname,     
            "clip":          clip,          
            "vae":           vae,           
            "steps":          steps,         
            "cfg":           cfg,           
            "sampler":       sampler,       
            "samplername":   samplername,   
            "scheduler":     scheduler,     
            "schedulername": schedulername,       
        }
        del pipe

        return (new_pipe,)

#---------------------------------------------------------------------------------------------------------------------------------------------------

# 节点束输出
class NepPipeOut:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
             "required": {
                "pipe": ("NEPPIPELINE",),
            },
            "hidden": {"my_unique_id": "UNIQUE_ID"},
        }

    RETURN_TYPES = ("NEPPIPELINE", "MODEL", "STRING", "CLIP", "VAE", "INT", "FLOAT", "STRING", "STRING", "STRING", "STRING",)
    RETURN_NAMES = ("pipe", "model", "modelname", "clip", "vae", "steps", "cfg", "sampler","samplername","scheduler","schedulername",)
    FUNCTION = "flush"

    CATEGORY = "EasyUse/Pipe"

    def flush(self, pipe, my_unique_id=None):
        model         = pipe.get("model")
        modelname     = pipe.get("modelname")
        clip          = pipe.get("clip")
        vae           = pipe.get("vae")
        steps         = pipe.get("steps")
        cfg           = pipe.get("cfg")
        sampler       = pipe.get("sampler")
        samplername   = pipe.get("samplername")
        scheduler     = pipe.get("scheduler")
        schedulername = pipe.get("schedulername")

        return (pipe, model, modelname, clip, vae, steps, cfg, sampler, samplername, scheduler, schedulername,)

#---------------------------------------------------------------------------------------------------------------------------------------------------
class NepPipeEdit:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
             "required": {},
             "optional": {
                "pipe": ("NEPPIPELINE",),
                "model": ("MODEL",),
                "modelname": ("STRING",),
                "clip": ("CLIP",),
                "vae": ("VAE",),
                "steps": ("INT",),
                "cfg": ("FLOAT",),
                "sampler": ("STRING",),
                "samplername": ("STRING",),
                "scheduler": ("STRING",),
                "schedulername": ("STRING",),
            },
            "hidden": {"my_unique_id": "UNIQUE_ID"},
        }
    RETURN_TYPES = ("NEPPIPELINE", "MODEL", "STRING", "CLIP", "VAE", "INT", "FLOAT", "STRING", "STRING", "STRING", "STRING",)
    RETURN_NAMES = ("pipe", "model", "modelname", "clip", "vae", "steps", "cfg", "sampler","samplername","scheduler","schedulername",)
    FUNCTION = "flush"

    def flush(self, pipe=None, model=None, modelname=None, clip=None, vae=None, steps=None, cfg=None, sampler=None, samplername=None, scheduler=None, schedulername=None,  my_unique_id=None):

        if pipe is None:
            pipe = {"loader_settings": {"positive": "", "negative": "", "xyplot": None}}

        model =         model         if model is not None else pipe.get("model")
        modelname =     modelname     if (modelname is not None and modelname is not "") else pipe.get("modelname")
        clip =          clip          if clip is not None else pipe.get("clip")
        vae =           vae           if vae is not None else pipe.get("vae")
        steps =         steps         if (steps is not None and steps > 0) else pipe.get("steps")
        cfg =           cfg           if (cfg is not None and cfg > 0.0) else pipe.get("cfg")
        sampler =       sampler       if sampler is not None else pipe.get("sampler")
        samplername =   samplername   if (samplername is not None and samplername is not "") else pipe.get("samplername")
        scheduler =     scheduler     if scheduler is not None else pipe.get("scheduler")
        schedulername = schedulername if (schedulername is not None and schedulername is not "") else pipe.get("schedulername")



        new_pipe = {
            **pipe,
            "model":         model,         
            "modelname":     modelname,     
            "clip":          clip,          
            "vae":           vae,           
            "steps":          steps,         
            "cfg":           cfg,           
            "sampler":       sampler,       
            "samplername":   samplername,   
            "scheduler":     scheduler,     
            "schedulername": schedulername,       
        }
        del pipe

        return (new_pipe,)


#---------------------------------------------------------------------------------------------------------------------------------------------------



NODE_CLASS_MAPPINGS = {
    "NepPipeIn": NepPipeIn,
    "NepPipeOut": NepPipeOut,
    "NepPipeEdit": NepPipeEdit,

}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NepPipeIn": "Pipe In (NEP)",
    "NepPipeOut": "Pipe Out (NEP)",
    "NepPipeEdit": "Pipe Edit (NEP)",
}