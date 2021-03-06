# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Edgar Andrés Margffoy-Tuay, Emilio Botero and Juan Camilo Pérez
#
# Licensed under the terms of the MIT License
# (see LICENSE for details)
# -----------------------------------------------------------------------------

"""Dynamic Multimodal Network PyTorch implementation."""

from .models import DMN, BaseDMN
from .referit_loader import ReferDataset

VERSION_INFO = (0, 1, 0, 'dev0')
__version__ = '.'.join(map(str, VERSION_INFO))
