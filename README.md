# AI Text-to-Video Generator 

> This Python script uses the OpenAI API to automatically convert a single text prompt into a narrated video. It generates a story with GPT-4o, creates scene-by-scene images with DALL-E 3, and produces a voiceover with a TTS model. The `moviepy` library then assembles these AI-generated assets into a final video file.

---

## Demo 

A short video created from the prompt "A cat astronaut exploring a candy planet."

* [View the full story text that was generated](generated_text.txt)
* [See all generated images for this run](images/)
* [Listen to all generated audio clips](audio/)
* [See all intermediate video clips](videos/)


## Key Features 
* **Automated Story Generation**: Expands a simple user prompt into a multi-sentence story using GPT-4o.
* **AI Image Generation**: Creates a unique, high-definition image for each sentence using DALL-E 3.
* **Realistic Voiceover**: Generates a natural-sounding audio narration for each sentence using OpenAI's TTS model.
* **Automatic Video Assembly**: Stitches together the generated images, audio files, and text overlays into a final, cohesive video.

---

## ⚙️ How It Works

The project is split into two main scripts that create an automated content pipeline:

1.  **Text Generation**: The user provides a topic to `text_generator.py`. This script uses OpenAI's GPT-4o model to write a short story and saves it to `generated_text.txt`.
2.  **Video Generation**: `video_generator.py` reads the story and splits it into individual sentences.
3.  **Asset Creation**: For each sentence, it makes parallel calls to the OpenAI API to generate a corresponding image (DALL-E 3) and an audio voiceover (TTS).
4.  **Clip Assembly**: It uses the `moviepy` library to combine the image, audio, and a text overlay into a short video clip for that sentence.
5.  **Finalization**: All the individual clips are concatenated in order to produce the final `final_video.mp4`.

---

## 🚀 Getting Started

To run this project locally, you will need to follow these setup steps.

### Prerequisites

* Python 3.9+
* Git
* An active OpenAI API account with billing set up.

### Installation Steps

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git)
    cd YOUR_REPOSITORY
    ```

2.  **Install External Dependencies**
    This project relies on two external programs for video and image processing. You must install them and add them to your system's PATH.

    * **FFmpeg**: A powerful multimedia framework.
        * [Download FFmpeg](https://ffmpeg.org/download.html)
    * **ImageMagick**: A software suite for image manipulation.
        * [Download ImageMagick](https://imagemagick.org/script/download.php#windows)
        * **Important**: During installation, you **must** check the boxes for **"Add application directory to your system path (PATH)"** and **"Install legacy utilities (e.g., convert)"**.

3.  **Set Up Python Environment**
    It is highly recommended to use a virtual environment to manage project dependencies.

    ```bash
    # Create and activate a virtual environment
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate

    # Install the required Python libraries
    pip install -r requirements.txt
    ```

4.  **Add Your OpenAI API Key**
    1.  Create a file named `api_key.py` in the root directory.
    2.  Add your OpenAI API key to this file:
        ```python
        API_KEY = "sk-YourSecretKeyGoesHere"
        ```
    *(Note: `api_key.py` is included in the `.gitignore` file to prevent you from accidentally committing your secret key.)*

---

## 🏃‍♀️ Usage

Run the scripts from the root `CAPSTONE` directory.

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

## 🛠️ Technologies Used

* **Python**
* **OpenAI API**
    * GPT-4o (Text Generation)
    * DALL-E 3 (Image Generation)
    * TTS (Audio Generation)
* **MoviePy**
* **FFmpeg**
* **ImageMagick**

---

## 📜 License

This project is distributed under the MIT License. See the `LICENSE` file for more information.