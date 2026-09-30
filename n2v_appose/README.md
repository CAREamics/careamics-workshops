# CAREamics Fiji

Updated: 30.09.26

In this section, we take a peek at the [Noise2Void Appose plugin for Fiji](https://github.com/CAREamics/careamics-fiji). 

> [!WARNING]  
> This plugin is experimental and is not expected to be bug-free.

## Pre-requisite

- [Fiji](https://fiji.github.io/)

## Run

1. Download the `.jar` from the [v0.1.0 careamics-fiji release](https://github.com/CAREamics/careamics-fiji/releases/tag/v0.1.0)
2. Place it in your Fiji plugin folder or install it via the interface (`Plugin > Install`, restart Fiji)
3. Download the [SEM example data](https://download.fht.org/jug/n2v/SEM.zip)
4. Start the CAREamics plugin from within Fiji
5. Select 15 epochs and run training


## Future developments

We want to develop the Appose plugin further, including:
- A prediction plugin
- Training and prediction from files on disk (including OME-Zarr)