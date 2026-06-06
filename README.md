# Textual Inversion vs DreamBooth

## Project Overview

This project explores two personalization techniques for Stable Diffusion v1.5:

- Textual Inversion
- DreamBooth (LoRA)

The objective is to teach the model a new visual concept corresponding to a toy car using a small custom dataset.

---

## Dataset

The dataset contains 10 images of a toy car captured from different viewpoints.

Dataset location:

```text
dataset/raw/
```

Processed images:

```text
dataset/processed/
```

All images were center-cropped and resized to 512×512 pixels.

---

## Project Structure

```text
.
├── dataset/
├── models/
├── notebooks/
├── results/
├── src/
├── README.md
└── requirements.txt
```

### Notebooks

```text
notebooks/
├── 01_baseline.ipynb
├── 02_textual_inversion.ipynb
└── 03_dreambooth.ipynb
```

- Baseline generation
- Textual Inversion training
- DreamBooth LoRA training

---

## Trained Models

### Textual Inversion

```text
models/textual_inversion/
└── learned_embeds.safetensors
```

Embedding size:

- 4 KB

Training time:

- 73.87 minutes

---

### DreamBooth LoRA

```text
models/dreambooth/
└── pytorch_lora_weights.safetensors
```

Model size:

- 3.1 MB

Training time:

- 24.08 minutes

---

## Generated Results

### Baseline

```text
results/baseline/
```

### Textual Inversion

```text
results/textual_inversion/
```

### DreamBooth

```text
results/dreambooth/
```

---

## Conclusion

Both methods successfully learned the toy car concept.

- Textual Inversion produces an extremely lightweight embedding and learns the general concept.
- DreamBooth generates images that are visually closer to the original toy car and preserves more details.

In this project, DreamBooth achieved the best visual quality while Textual Inversion offered the lightest solution.
