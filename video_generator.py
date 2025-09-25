import os
import re
import urllib.request
from openai import OpenAI, APIError, RateLimitError
from moviepy.editor import *
from api_key import API_KEY

# --- Main Script ---
def main():
    """
    Main function to create a video from a text file by generating images and audio.
    """
    try:
        # 1. Initialize the OpenAI Client
        client = OpenAI(api_key=API_KEY)

        # 2. Read the text file
        # The script now looks for the text file inside the GenAI folder
        input_filename = "GenAI/generated_text.txt" 
        with open(input_filename, "r", encoding="utf-8") as file:
            text = file.read()

        # 3. Split text into smaller, sentence-like chunks
        paragraphs = re.split(r'[.,;!?\n]', text)
        paragraphs = [p.strip() for p in paragraphs if p.strip()]

        # 4. Create necessary folders safely
        print("Creating output directories...")
        os.makedirs("audio", exist_ok=True)
        os.makedirs("images", exist_ok=True)
        os.makedirs("videos", exist_ok=True)

        # 5. Loop through each paragraph to generate a video clip
        for i, para in enumerate(paragraphs):
            print(f"\n--- Processing Clip {i+1}/{len(paragraphs)} ---")
            print(f"Text: {para}")

            # Generate Image using DALL-E 3
            print("Generating AI image...")
            image_response = client.images.generate(
                model="dall-e-3", prompt=para, n=1, size="1024x1024", quality="hd"
            )
            image_url = image_response.data[0].url
            image_path = f"images/image{i+1}.jpg"
            urllib.request.urlretrieve(image_url, image_path)
            print(f"Image saved to {image_path}")

            # Generate Audio using OpenAI TTS-HD
            print("Generating AI voiceover...")
            audio_response = client.audio.speech.create(
                model="tts-1-hd", voice="alloy", input=para
            )
            audio_path = f"audio/voiceover{i+1}.mp3"
            audio_response.stream_to_file(audio_path)
            print(f"Audio saved to {audio_path}")

            # Create video clip using MoviePy
            print("Assembling video clip...")
            audio_clip = AudioFileClip(audio_path)
            image_clip = ImageClip(image_path).set_duration(audio_clip.duration)
            
            # --- THIS IS THE CORRECTED SECTION ---
            # Creates a caption with a transparent background that wraps text.
            text_clip = TextClip(
                para, 
                fontsize=50,
                color="white",
                font="Arial-Bold",
                stroke_color='black', # Adds a black outline for readability
                stroke_width=2,
                method='caption', 
                size=(950, None) # Sets a max width for the text box
            ).set_duration(audio_clip.duration)
            
            video_clip = CompositeVideoClip([image_clip, text_clip.set_position("center")]).set_audio(audio_clip)
            video_path = f"videos/video{i+1}.mp4"
            video_clip.write_videofile(video_path, fps=24, codec="libx264")
            print(f"Clip saved to {video_path}")

        # 6. Concatenate all individual clips into a final video
        print("\n--- Creating Final Video ---")
        video_files = [f"videos/video{i+1}.mp4" for i in range(len(paragraphs))]
        final_clips = [VideoFileClip(vf) for vf in video_files]
        
        final_video = concatenate_videoclips(final_clips, method="compose")
        final_video.write_videofile("GenAI/final_video.mp4", fps=24, codec="libx264")
        print("\nSuccess! The final video has been saved to 'final_video.mp4'")

    except FileNotFoundError:
        # Updated error message to reflect the new path
        print(f"Error: The input file '{input_filename}' was not found. Please run text_generator.py first.")
    except (APIError, RateLimitError) as e:
        print(f"An OpenAI API error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
'''import openai
import re, os
from requests import get
import urllib.request
from gtts import gTTS
from moviepy.editor import *
from api_key import API_KEY

# Set your OpenAI API key
openai.api_key = API_KEY

# Read the text file
with open("generated_text.txt", "r") as file:
    text = file.read()

# Split the text by , and .
paragraphs = re.split(r"[,.]", text)

#Create Necessary Folders
os.makedirs("audio")
os.makedirs("images")
os.makedirs("videos")

# Loop through each paragraph and generate an image for each
i=1
for para in paragraphs[:-1]:
    response = openai.Image.create(
        prompt=para.strip(),
        n=1,
        size="1024x1024"
    )
    print("Generate New AI Image From Paragraph...")
    image_url = response['data'][0]['url']
    urllib.request.urlretrieve(image_url, f"images/image{i}.jpg")
    print("The Generated Image Saved in Images Folder!")

    # Create gTTS instance and save to a file
    tts = gTTS(text=para, lang='en', slow=False)
    tts.save(f"audio/voiceover{i}.mp3")
    print("The Paragraph Converted into VoiceOver & Saved in Audio Folder!")

    # Load the audio file using moviepy
    print("Extract voiceover and get duration...")
    audio_clip = AudioFileClip(f"audio/voiceover{i}.mp3")
    audio_duration = audio_clip.duration

    # Load the image file using moviepy
    print("Extract Image Clip and Set Duration...")
    image_clip = ImageClip(f"images/image{i}.jpg").set_duration(audio_duration)

    # Use moviepy to create a text clip from the text
    print("Customize The Text Clip...")
    text_clip = TextClip(para, fontsize=50, color="white")
    text_clip = text_clip.set_pos('center').set_duration(audio_duration)

    # Use moviepy to create a final video by concatenating
    # the audio, image, and text clips
    print("Concatenate Audio, Image, Text to Create Final Clip...")
    clip = image_clip.set_audio(audio_clip)
    video = CompositeVideoClip([clip, text_clip])

    # Save the final video to a file
    video = video.write_videofile(f"videos/video{i}.mp4", fps=24)
    print(f"The Video{i} Has Been Created Successfully!")
    i+=1


clips = []
l_files = os.listdir("videos")
for file in l_files:
    clip = VideoFileClip(f"videos/{file}")
    clips.append(clip)

print("Concatenate All The Clips to Create a Final Video...")
final_video = concatenate_videoclips(clips, method="compose")
final_video = final_video.write_videofile("final_video.mp4")
print("The Final Video Has Been Created Successfully!")'''
