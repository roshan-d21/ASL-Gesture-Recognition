# ASL-Gesture-Recognition

A python application that uses deep learning to recognize hand sign of alphabets of the American Sign Language

https://user-images.githubusercontent.com/22237701/115950021-592d8e80-a4f6-11eb-9239-16ab5737900a.mp4

## Installation

**Note: GPU support is only available for Nvidia GPUs running on Windows or Linux**

1. Install the latest Nvidia drivers `>=450.51.06` for your card by clicking [here](https://www.nvidia.com/Download/index.aspx)

2. Install [Nvidia CUDA Toolkit 11.0 Update 1](https://developer.nvidia.com/cuda-11.0-update1-download-archive) by following the guides
    - [Windows](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-microsoft-windows/index.html)
    - [Linux](https://docs.nvidia.com/cuda/archive/11.0/cuda-installation-guide-linux/index.html)

3. Install `python` `3.6` or `3.7`

4. Install `PyTorch v1.7.1`
    ```zsh
    pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
    ```

5. Install `fastai v1.0.61`
    ```zsh
    pip install fastai==1.0.61
    ```

6. Install `opencv`
    ```zsh
    pip install opencv-python
    ```

## Execution

First, extract the contents of the zip file `/model/v4/export.zip` in the same directory

Run the application using:
```zsh
python demo.py
```