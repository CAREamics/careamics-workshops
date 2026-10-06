# Using Noise2Void in CAREamics

In this section, we take a deep dive into Noise2Void using `n2v_in_depth.ipynb`. We discuss
pixel noise in microscopy, how Noise2Void trains by masking pixels, and showcase how
to run Noise2Void with CAREamics and some limitations of the method.

## Pre-requisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [juv](https://github.com/manzt/juv)

## Run the notebook

You can run the notebook as a stand-alone using `juv` (pre-requisite):

```bash
juv run n2v_in_depth.ipynb
```


## References

- [Noise2Void paper](https://arxiv.org/abs/1811.10980)