# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.

from .build import MODEL_REGISTRY, build_model  # noqa
from .custom_video_model_builder import *  # noqa
from .video_model_builder import ResNet, SlowFast # noqa

# self.pretrained = False  # ✅ 禁止调用 load_pretrained (when training on 1*224*224; with vit-tiny)