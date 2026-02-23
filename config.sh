#!/bin/bash

OUTPUT="./models"

# Download model weights
if [ ! -f "$OUTPUT/agg.pth" ]; then
    uv run gdown --folder "https://drive.google.com/drive/folders/17SAuZ2sZrTYf21BiNKhRsEfdj-fbeQQN" -O $OUTPUT
else
    echo "ssv2a weights already exist, skipping"
fi

# Download yolo
wget -nc https://github.com/ultralytics/assets/releases/download/v8.4.0/yolov8x-oiv7.pt -P $OUTPUT

# update config
sed -i 's|"detection_model": ""|"detection_model": "./yolov8x-oiv7.pt"|' models/ssv2a.json