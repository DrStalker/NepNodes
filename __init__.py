"""
@author: Nepenthe
@title: NepNodes Custom Nodes for ComfyUI
@nickname: NepNodes
@description: Personal Nodes
"""


# Combine the mappings/dispaly names from all files
from .nep_nodes import NODE_CLASS_MAPPINGS as MAP1
from .nep_nodes import NODE_DISPLAY_NAME_MAPPINGS as NAME1
from .nep_pipes import NODE_CLASS_MAPPINGS as MAP2
from .nep_pipes import NODE_DISPLAY_NAME_MAPPINGS as NAME2
NODE_CLASS_MAPPINGS = MAP1 | MAP2
NODE_DISPLAY_NAME_MAPPINGS = NAME1 | NAME2