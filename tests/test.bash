#!/bin/bash

cd $(dirname "$0")

# If this works, it works
uv run --with ipykernel --with papermill papermill jupytext:notebook.py output.ipynb --kernel python3
