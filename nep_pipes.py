import torch
import json
import os
import comfy.sd # type: ignore
import folder_paths # type: ignore
import math
#from datetime import datetime
#from PIL import Image, ImageOps, ImageSequence
#import numpy as np
#from PIL.PngImagePlugin import PngInfo
#from comfy.cli_args import args
#import torch.nn.functional as F
#import time
#import random
#import traceback
import re
import comfy.samplers, comfy.supported_models



# Taken from EasyUSe and modified.

class NepPipeIn:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
             "required": {},
             "optional": {
                "pipe": ("PIPE_LINE",),
                "model": ("MODEL",),
                "pos": ("CONDITIONING",),
                "neg": ("CONDITIONING",),
                "latent": ("LATENT",),
                "vae": ("VAE",),
                "clip": ("CLIP",),
                "image": ("IMAGE",),
                "xyPlot": ("XYPLOT",),
            },
            "hidden": {"my_unique_id": "UNIQUE_ID"},
        }

    RETURN_TYPES = ("PIPE_LINE",)
    RETURN_NAMES = ("pipe",)
    FUNCTION = "flush"

    CATEGORY = "EasyUse/Pipe"

    def flush(self, pipe=None, model=None, pos=None, neg=None, latent=None, vae=None, clip=None, image=None, xyplot=None, my_unique_id=None):

        model = model if model is not None else pipe.get("model")
        if model is None:
            log_node_warn(f'pipeIn[{my_unique_id}]', "Model missing from pipeLine")
        pos = pos if pos is not None else pipe.get("positive")
        if pos is None:
            log_node_warn(f'pipeIn[{my_unique_id}]', "Pos Conditioning missing from pipeLine")
        neg = neg if neg is not None else pipe.get("negative")
        if neg is None:
            log_node_warn(f'pipeIn[{my_unique_id}]', "Neg Conditioning missing from pipeLine")
        vae = vae if vae is not None else pipe.get("vae")
        if vae is None:
            log_node_warn(f'pipeIn[{my_unique_id}]', "VAE missing from pipeLine")
        clip = clip if clip is not None else pipe.get("clip") if pipe is not None and "clip" in pipe else None
        # if clip is None:
        #     log_node_warn(f'pipeIn[{my_unique_id}]', "Clip missing from pipeLine")
        if latent is not None:
            samples = latent
        elif image is None:
            samples = pipe.get("samples") if pipe is not None else None
            image = pipe.get("images") if pipe is not None else None
        elif image is not None:
            if pipe is None:
                batch_size = 1
            else:
                batch_size = pipe["loader_settings"]["batch_size"] if "batch_size" in pipe["loader_settings"] else 1
            samples = {"samples": vae.encode(image[:, :, :, :3])}
            samples = RepeatLatentBatch().repeat(samples, batch_size)[0]

        if pipe is None:
            pipe = {"loader_settings": {"positive": "", "negative": "", "xyplot": None}}

        xyplot = xyplot if xyplot is not None else pipe['loader_settings']['xyplot'] if xyplot in pipe['loader_settings'] else None

        new_pipe = {
            **pipe,
            "model": model,
            "positive": pos,
            "negative": neg,
            "vae": vae,
            "clip": clip,

            "samples": samples,
            "images": image,
            "seed": pipe.get('seed') if pipe is not None and "seed" in pipe else None,

            "loader_settings": {
                **pipe["loader_settings"],
                "xyplot": xyplot
            }
        }
        del pipe

        return (new_pipe,)

# 节点束输出
class NepPipeOut:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
             "required": {
                "pipe": ("PIPE_LINE",),
            },
            "hidden": {"my_unique_id": "UNIQUE_ID"},
        }

    RETURN_TYPES = ("PIPE_LINE", "MODEL", "CONDITIONING", "CONDITIONING", "LATENT", "VAE", "CLIP", "IMAGE", "INT",)
    RETURN_NAMES = ("pipe", "model", "pos", "neg", "latent", "vae", "clip", "image", "seed",)
    FUNCTION = "flush"

    CATEGORY = "EasyUse/Pipe"

    def flush(self, pipe, my_unique_id=None):
        model = pipe.get("model")
        pos = pipe.get("positive")
        neg = pipe.get("negative")
        latent = pipe.get("samples")
        vae = pipe.get("vae")
        clip = pipe.get("clip")
        image = pipe.get("images")
        seed = pipe.get("seed")

        return pipe, model, pos, neg, latent, vae, clip, image, seed

#---------------------------------------------------------------------------------------------------------------------------------------------------


NODE_CLASS_MAPPINGS = {
    "NepPipeIn": NepPipeIn,
    "NepPipeOut": NepPipeOut,

}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NepPipeIn": "Pipe In (NEP)",
    "NepPipeOut": "Pipe Out (NEP)",
}