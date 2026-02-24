#!/bin/bash

OUTPUT="./models"
YOLO_VERSION="yolo26x"

# Download model weights
if [ ! -f "$OUTPUT/agg.pth" ]; then
    uv run gdown --folder "https://drive.google.com/drive/folders/17SAuZ2sZrTYf21BiNKhRsEfdj-fbeQQN" -O $OUTPUT
else
    echo "ssv2a weights already exist, skipping"
fi

# Download yolo
wget -nc https://github.com/ultralytics/assets/releases/download/v8.4.0/${YOLO_VERSION}.pt -P $OUTPUT

# update config
SEARCH='"detection_model": ".*"'
REPLACE="\"detection_model\": \"models/${YOLO_VERSION}.pt\""

sed -i "s|$SEARCH|$REPLACE|" models/ssv2a.json