
<p align="center">
  <a href="https://careamics.github.io/">
    <img src="https://raw.githubusercontent.com/CAREamics/.github/main/profile/images/banner_careamics.png">
  </a>
</p>


# Noise2Void with CAREamics

In this section, we explore Noise2Void in CAREamics using Google Colab.

## Pre-requisites

- A google account and space on your Google drive

## 1 - Download the Colab notebook
 
1. Open the [notebook in Colab]
(https://colab.research.google.com/github/CAREamics/ZeroCostDL4Mic/blob/n2v-careamics/Colab_notebooks/CAREamics_Noise2Void_2D_ZeroCostDL4Mic.ipynb).
2. Sign-in with your Google account.
3. Choose `File > Save a copy in Drive`.

This will reopen a copy hosted on your Google Drive.


## 2 - Setting up

1. Make sure you are using a GPU: under your profile click on "v" and select `Change runtime type > T4 GPU > Save`. 
2. Run cells in order, top to bottom. To run a cell, click the "▶" (play) button on its top-left corner. Alternatively, click on the cell and press `Shift+Enter`. Wait for each cell to finish (a green tick appears) before running the next.
3. You can ignore the code. The only things you need to fill in are the form fields (boxes and tick-boxes) in the cells.


## 3 - Training Noise2Void

You can add your own data to your Google Drive, or use our example data (tick `Use_example_dataset` in
the relevant cell). Follow the indications in the notebook, train and predict using Noise2Void!


## Notes on Colab

- Colab disconnects after about 90 minutes idle and GPU time is limited, so students should use their own Google accounts and not share a session
- The first time the notebook are run, imports and data download might take a little while so you may want to run it before your teaching session once


## Going further

Check out the [CAREamics documentation](https://careamics.github.io/latest/) to learn more
about running Noise2Void using Python scripts and notebooks.

### Noise2Void UIs

- There is a [napari Noise2Void plugin](github.com/CAREamics/careamics-ui)
- We recently developed an experimental [Fiji Noise2Void plugin](https://github.com/CAREamics/careamics-fiji) 

### Understanding Noise2Void

We also provide an example notebook to [better understand Noise2Void](https://github.com/CAREamics/careamics-workshops/tree/main/n2v).

### Questions / help needed?

Contact us on [image.sc] using the `careamics` topic or open an [issue on CAREamics](https://github.com/CAREamics/careamics/issues).


