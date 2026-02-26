## Demo
First, make sure to clone the repository with the required submodules with `git clone --recurse-submodules [...]`.

To download the model weights and update the configuration file, run `config.sh`.

Then, make sure to have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed, go to the root directory of the project and run `uv run python src/SSV2A/infer_i2a.py --cfg models/ssv2a.json --ckpt models/ssv2a.pth --image_dir ./img --out_dir ./output`.

## Dependencies
The original repository had some dependencies issues. The fixed code runs on python 3.10, and the required libraries have different versions than those on the original `SSV2A` repo.