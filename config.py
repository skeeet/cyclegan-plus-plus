# -*- coding: utf-8 -*-

__author__ = "Rahul Bhalley"

# Data
DATASET_DIR = "datasets"
DATASET_NAME = "ukiyoe2photo"
STYLES = ["ce", "mo", "uk", "vg"]
# Set up `TRAIN_STYLE`
if DATASET_NAME == "cezanne2photo":
    TRAIN_STYLE = "ce"
elif DATASET_NAME == "monet2photo":
    TRAIN_STYLE = "mo"
elif DATASET_NAME == "ukiyoe2photo":
    TRAIN_STYLE = "uk"
elif DATASET_NAME == "vangogh2photo":
    TRAIN_STYLE = "vg"
DATASET_PATH = {
    "trainA": f"./{DATASET_DIR}/{DATASET_NAME}/trainA",
    "trainB": f"./{DATASET_DIR}/{DATASET_NAME}/trainB",
    "testA": f"./{DATASET_DIR}/{DATASET_NAME}/testA",
    "testB": f"./{DATASET_DIR}/{DATASET_NAME}/testB"
}
LOAD_DIM = 286
CROP_DIM = 256
CKPT_DIR = "checkpoints"
SAMPLE_DIR = "samples"

# Quadratic Potential
NORM = "l1"
LAMBDA = 10.0

# CycleGAN
CYC_WEIGHT = 10.0
ID_WEIGHT = 0.5

# Network
N_CHANNELS = 3
UPSAMPLE = True

# Training
BATCH_SIZE = 4
LR = 2e-4
BETA1 = 0.5
BETA2 = 0.999
BEGIN_ITER = 0
END_ITER = 15000
TRAIN = True  # `False` runs `infer` function & `True` runs `train` function

# Logs
ITERS_PER_LOG = 100
ITERS_PER_CKPT = 1000

# Inference configurations
INFER_ITER = 15000
INFER_STYLE = "uk"
IMG_NAME = "image.jpg"
IN_IMG_DIR = "images"
OUT_REC_DIR = "rec"
OUT_STY_DIR = "sty"
IMG_SIZE = None  # If `None` then stylizes original size `IMG_NAME`