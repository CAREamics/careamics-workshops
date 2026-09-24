# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "careamics[examples]>=0.3.0, <0.4.0",
# ]
# [tool.uv.sources]
# careamics = {git = "https://github.com/CAREamics/careamics", branch = "main"}
# ///
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from skimage import data
import numpy as np
from scipy.ndimage import convolve
from torch import tensor
from microssim import MicroSSIM

from careamics import CAREamist
from careamics.config import create_n2v_config, create_structn2v_config
from careamics.plotting import plot_loss
from careamics.metrics.metrics import scale_invariant_psnr


def train_and_predict() -> None:
    pass

if __name__ == "__main__":
    train_and_predict()