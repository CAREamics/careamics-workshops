# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "careamics[examples]>=0.3.0, <0.4.0",
# ]
# [tool.uv.sources]
# careamics = {git = "https://github.com/CAREamics/careamics", branch = "main"}
# ///
from pathlib import Path

from careamics import CAREamist
from careamics.config import create_n2v_config
from careamics.plotting import plot_loss


def train_and_predict() -> None:
    root = Path(__file__).parent / "data"
    root_exp = Path(__file__).parent / "results"
    root_exp.mkdir(parents=True, exist_ok=True)

    file_path = root / "img_corr_noise.tif"
    if not file_path.exists():
        raise ValueError(
            f"Example image {file_path} not found, run 00_create_data.py"
        )
    
    # configuration
    n_epochs = 10
    name = f"n2v_corr_noise_e{n_epochs}"
    exp = root_exp / name
    exp.mkdir(parents=True, exist_ok=True)

    config = create_n2v_config(
        experiment_name=name,
        data_type="tiff",
        axes="ZYX",
        batch_size=16,
        patch_size=(8, 64, 64),
        num_epochs=n_epochs,
        use_n2v2=True,
    )

    # create a CAREamist object
    careamist = CAREamist(config, work_dir=exp)

    # train!
    careamist.train(train_data=file_path)

    # save loss to disk
    plot_loss(careamist.get_losses(), save_path=exp, plot_learning_rate=False, plot_metrics=False)

    # predict to disk
    careamist.predict_to_disk(
        pred_data=file_path
    )

if __name__ == "__main__":
    train_and_predict()