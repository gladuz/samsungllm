## Installation

### From scratch
```bash
conda create -n samsungchal python=3.10
conda activate samsungchal
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
pip install transformers datasets accelerate flash_attn vllm
```

### If there is a torch already
```bash
pip install transformers datasets accelerate flash_attn vllm
```