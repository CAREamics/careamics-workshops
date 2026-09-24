# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "careamics[examples]>=0.3.0, <0.4.0",
# ]
# [tool.uv.sources]
# careamics = {git = "https://github.com/CAREamics/careamics", branch = "main"}
# ///
from pathlib import Path

from skimage import data
from pathlib import Path

from skimage import data
import numpy as np
from scipy.ndimage import convolve
from tifffile import imwrite


def get_gaussian_noise(img: np.ndarray, c: int) -> tuple[np.ndarray, np.ndarray]:
    """Generate Gaussian additive noise.

    Parameters
    ----------
    img : np.ndarray
        Image to which noise should be added.
    c : int
        Noise strength (au).

    Returns
    -------
    np.ndarray
        Resulting noisy image.
    np.ndarray
        Noise. 
    """
    rng = np.random.default_rng(24)

    noise = rng.normal(0, c, img.shape)
    noisy = np.clip(img+noise, 0, None)

    return noisy, noisy-img

def _add_correlations(noise: np.ndarray, d: int = 3) -> np.ndarray:
    """Add correlations to a noise map.

    Parameters
    ----------
    noise : np.ndarray
        Noise map.
    d : int
        Size of the correlation.

    Returns
    -------
    np.ndarray
        Resulting corelated noise.
    """
    noise_kernel  = np.array([[[1] * d]]) / d # horizontal correlations
    return convolve(noise, noise_kernel)


def get_corr_gaussian_noise(img: np.ndarray, c: int) -> tuple[np.ndarray, np.ndarray]:
    """Generate correlated Gaussian additive noise.

    Parameters
    ----------
    img : np.ndarray
        Image to which noise should be added.
    c : int
        Noise strength (au).

    Returns
    -------
    np.ndarray
        Resulting noisy image.
    np.ndarray
        Noise. 
    """
    rng = np.random.default_rng(24)

    noise = rng.normal(0, c, img.shape)
    corr_noise = _add_correlations(noise)
    noisy = np.clip(img+corr_noise, 0, None)

    return noisy, noisy-img


def save_data(path: Path) -> None:
    img = data.cells3d()[:, 0]
    c_example = int(img.mean())

    img_gauss, _ = get_gaussian_noise(img, c_example)
    img_corr, _ = get_corr_gaussian_noise(img, c_example)

    root = path / "data"
    root.mkdir(parents=True, exist_ok=True)

    # save images
    imwrite(root / "img_ground_truth.tif", img)
    imwrite(root / "img_gauss_noise.tif", img_gauss)
    imwrite(root / "img_corr_noise.tif", img_corr)

if __name__ == "__main__":
    save_data(Path(__file__).parent)