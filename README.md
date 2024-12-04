# GPT_LLM_ToyStory 😉 🚀 🧸 

This repository contains a GPT-based language model trained on a **Toy Story dataset**. The model uses transformer architectures, including self-attention, multi-head attention, and feed-forward layers, to generate contextually coherent text inspired by the Toy Story universe.

## 📖 Overview

We inteded to train the model to understand and generate text in the style of the beloved Toy Story characters. It uses a sequence-to-sequence modeling approach with state-of-the-art transformer techniques to create outputs that mimic the tone and dialogue of the Toy Story movies.
For the output, it saves the generated text at each milestone into a file "(milestoneX.txt)".

## 🛠️ Features

- **Transformer Architecture**: The backbone of the model is a powerful transformer architecture that leverages multi-head self-attention to understand contextual relationships between words, layer normalization to ensure stable training, and residual connections to prevent vanishing gradients. This combination allows the model to capture intricate details of Toy Story dialogues and interactions. "Buzz and Woody would call it cutting-edge teamwork!" 🌌👨‍🚀🚀

- **Custom Dataset**: The model is trained on a carefully curated and preprocessed Toy Story script dataset. This ensures the generated text mirrors the tone, quirks, and personalities of the beloved characters. Preprocessing steps like tokenization and cleaning guarantee clean and meaningful inputs for training.
"It's like feeding the model a treasure chest of Toy Story magic!" 🐑👩‍🌾🤠🐎

- **Text Generation**: Harness the model to create creative, character-themed outputs with customizable lengths. Whether it’s Buzz’s bold declarations, Woody’s heartfelt lines, or Rex’s anxious ramblings, the model can generate them all, bringing your favorite characters to life in words.
"To infinity and beyond... with words!" 🧸👾🐎

- **Milestone Training**: During training, intermediate outputs are saved at regular intervals as milestone checkpoints. This allows you to track the model’s progress, compare versions, and even revisit earlier results for insights or nostalgia. "Think of it as leaving breadcrumbs on the road to AI greatness!" 👼🚀👨‍🚀

# Milestones

The project was completed in eight milestones, each building on the previous one:

1. Dataset Exploration and Preparation

- Load and preprocess the Toy Story dataset by cleaning and tokenizing the text.
- Split the dataset into training and validation sets.

2. Basic Model Usage (Bigram Language Model)

- Implement a simple Bigram Language Model for initial experimentation.
- Evaluate its performance on the dataset and generate preliminary text.

3. Self-attention & Softmax Iteration

- Introduce self-attention to compute contextual relationships between tokens.
- Use masked softmax to ensure causal predictions.

4. Multi-head Attention

- Enhance the model with multi-head attention, allowing it to focus on multiple aspects of the input simultaneously.

5. Feed Forward Layers

- Add feed-forward layers to improve the model’s ability to capture complex patterns.

6. Residual Connections

- Incorporate residual connections to stabilize training and mitigate vanishing gradients.

7. Layer Normalization

- Add layer normalization for better numerical stability and faster convergence.

8.Dropout

- Introduce dropout regularization to reduce overfitting and improve generalization.


# Install Dependencies
Make sure you have Python and PyTorch installed. Install the required packages using:

pip install -r requirements.txt


# Milestone Outputs
Generated text is saved at each milestone in the format milestoneX.txt

  

