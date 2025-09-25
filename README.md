# AI Text-to-Video Generator 

> This Python script uses the OpenAI API to automatically convert a single text prompt into a narrated video. It generates a story with GPT-4o, creates scene-by-scene images with DALL-E 3, and produces a voiceover with a TTS model. The `moviepy` library then assembles these AI-generated assets into a final video file.

---

## Demo 

A short video created from the prompt "A cat astronaut exploring a candy planet."

* [View the full story text that was generated](generated_text.txt)
* [See a demo of generated images for this run](demo_assets/)
* [Listen to to a demo of generated audio clips](demo_assets/)
* [See a demo of intermediate video clips](demo_assets/)
* [Final Generated Video](demo_assets/final_video.mp4)


## Key Features 
* **Automated Story Generation**: Expands a simple user prompt into a multi-sentence story using GPT-4o.
* **AI Image Generation**: Creates a unique, high-definition image for each sentence using DALL-E 3.
* **Realistic Voiceover**: Generates a natural-sounding audio narration for each sentence using OpenAI's TTS model.
* **Automatic Video Assembly**: Stitches together the generated images, audio files, and text overlays into a final, cohesive video.

---

## How It Works

The project is split into two main scripts that create an automated content pipeline:

1.  **Text Generation (`text_generator.py`)**: The user provides a topic. This script uses a **Large Language Model (LLM)** to write a short story and saves it to `generated_text.txt`.
2.  **Video Generation (`video_generator.py`)**:
    * Reads the generated story and splits it into individual sentences.
    * For each sentence, it uses a **Generative Adversarial Network (GAN)** to create a corresponding image and a **Text-to-Speech (TTS)** model for the audio narration.
    * It uses `moviepy` to combine the image, audio, and a text overlay into a video clip for that sentence.
    * Finally, it concatenates all the individual clips into the final `final_video.mp4`.

---
## Core AI Methodology

This project's innovation comes from its unique integration of Transformer and GAN models to improve the quality of the final video output.

### 1. Story Generation (Transformer LLM)
To generate a coherent and detailed story, the system utilizes the **decoder block of a Transformer architecture**. The user's initial prompt is converted into vector embeddings, which are processed through multiple layers of **multi-head self-attention**. This allows the model to understand the context and relationships between words, generating a rich narrative that serves as a high-quality input for the next stage.

### 2. Image Generation (GAN)
The generated story is segmented, and each sentence is fed into a **Generative Adversarial Network (GAN)** for image synthesis. The GAN consists of two competing neural networks:
* A **Generator** creates images based on text embeddings from the story.
* A **Discriminator** evaluates these images against real-world data, providing feedback that iteratively trains the generator to produce more accurate and realistic visuals.

This two-part approach ensures that the generated story is detailed and that the resulting images are of high quality and contextually relevant.


---

## Getting Started

To run this project locally, you will need to follow these setup steps.

### Prerequisites

* Python 3.9+
* Git
* An active OpenAI API account

### Installation Steps

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/vidyacheekuri/text-to-video-generator.git](https://github.com/vidyacheekuri/text-to-video-generator.git)
    cd text-to-video-generator
    ```

2.  **Install External Dependencies**
    This project relies on two external programs for video and image processing. You must install them and add them to your system's PATH.

    * **FFmpeg**: A powerful multimedia framework.
        * [Download FFmpeg](https://ffmpeg.org/download.html)
    * **ImageMagick**: A software suite for image manipulation.
        * [Download ImageMagick](https://imagemagick.org/script/download.php#windows)

3.  **Add Your OpenAI API Key**
    1.  Create a file named `api_key.py` in the root directory.
    2.  Add your OpenAI API key to this file:
        ```python
        API_KEY = "sk-YourSecretKeyGoesHere"
        ```

---

## Usage

Run the scripts from the root `GenAI` directory.

1.  **Generate the Story**:
    Run the text generator and enter a topic when prompted.
    ```bash
    python text_generator.py
    ```

2.  **Generate the Video**:
    Once the text is generated, run the video generator script.
    ```bash
    python video_generator.py
    ```

3.  **View the Output**:
    The final video will be saved as `final_video.mp4` in the root directory. All intermediate assets will be in the `images/`, `audio/`, and `videos/` folders.

---

## Technologies Used

* **AI Models**:
    * **Large Language Model**: Transformer-based decoder architecture for story generation (GPT-4o).
    * **Image Generation**: Generative Adversarial Network (GAN) for text-to-image synthesis (DALL-E 3).
    * **Speech Synthesis**: Text-to-Speech (TTS) for voiceover narration.
* **Core Language**: Python
* **Video Processing**: MoviePy
* **External Tools**: FFmpeg, ImageMagick

---

