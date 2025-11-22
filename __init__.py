"""
@author: Nepenthe
@title: NepNodes Custom Nodes for ComfyUI
@nickname: NepNodes
@description: Personal Nodes
"""

#from .nep_nodes import NODE_CLASS_MAPPINGS

#__all__ = ['NODE_CLASS_MAPPINGS']


from .nep_nodes import NepWan_Resolutions
from .nep_nodes import NepXOR_INT_INT
from .nep_nodes import  *

NODE_CLASS_MAPPINGS = { 
    "NepWan_Resolutions": NepWan_Resolutions,
    "NepXOR_INT_INT": NepXOR_INT_INT,
    "NepRemoveFirstOrLastImageFromBatch": NepRemoveFirstOrLastImageFromBatch,
    "NepRatioResolution": NepRatioResolution,

}

NODE_DISPLAY_NAME_MAPPINGS = { 
    "NepWan_Resolutions": "WAN Resolutions (Nep)" ,
    "NepXOR_INT_INT": "XOR (Nep)",
    "NepRemoveFirstOrLastImageFromBatch": "Remove First or Last From Batch (Nep)",
    "NepRatioResolution": "Resolution from Ratio (Nep)",
    
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

