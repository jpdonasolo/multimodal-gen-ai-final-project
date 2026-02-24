import os
import subprocess
import json


def setup(
    yolo_version="yolo26x",
    *,
    config_path="models/ssv2a.json",
    output="./models",
    yolo_url_template="https://github.com/ultralytics/assets/releases/download/v8.4.0/{version}.pt",
):
    yolo_weights = f"{output}/{yolo_version}.pt"
    yolo_url = yolo_url_template.format(version=yolo_version)

    # Download model weights if not already present
    if not os.path.isfile(f"{output}/agg.pth"):
        # Try to download via gdown (requires gdown and uv installed)
        subprocess.run([
            "uv", "run", "gdown", 
            "--folder", 
            "https://drive.google.com/drive/folders/17SAuZ2sZrTYf21BiNKhRsEfdj-fbeQQN", 
            "-O", output
        ])
    else:
        print("ssv2a weights already exist, skipping")

    # Download YOLO weights if not present
    if not os.path.isfile(yolo_weights):
        subprocess.run([
            "wget", "-nc", 
            yolo_url,
            "-P", output
        ])
    else:
        print(f"{yolo_weights} already exists, skipping download")

    # Update detection_model path in config
    if os.path.isfile(config_path):
        with open(config_path, "r") as f:
            config = json.load(f)

        # Update detection_model field if needed
        detection_model_path = f"models/{yolo_version}.pt"
        if config["detector"]["detection_model"] != detection_model_path:
            config["detector"]["detection_model"] = detection_model_path
            with open(config_path, "w") as f:
                json.dump(config, f, indent=4)
            print(f"Updated 'detection_model' path in {config_path}")
        else:
            print(f"'detection_model' already set correctly in {config_path}")
    else:
        print(f"Config file {config_path} not found.")


if __name__ == "__main__":
    setup()