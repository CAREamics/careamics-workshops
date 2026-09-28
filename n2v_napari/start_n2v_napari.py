#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "careamics[examples]>=0.3.4,<0.4.0",
#     "careamics-napari>=0.3.4b0,<0.4.0",
#     "napari>=0.9.0,<0.10.0"
# ]
# ///
import napari

from careamics_napari.n2v_plugin import N2VPlugin
from careamics_napari.sample_data import n2v_sem_data

if __name__ == "__main__":
    # download data
    data = n2v_sem_data()
    # create a Viewer
    viewer = napari.Viewer()
    # add n2v plugin
    viewer.window.add_dock_widget(N2VPlugin(viewer))
    # add data
    for layer in data:
        viewer.add_layer(layer)
    # start UI
    napari.run()