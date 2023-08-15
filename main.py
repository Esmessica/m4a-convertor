from moviepy.editor import AudioFileClip
import os


script_directory = os.path.dirname(os.path.abspath(__file__))
m4a_folder = os.path.join(script_directory, "m4a_files")
mp3_folder = os.path.join(script_directory, "mp3_files")


if not os.path.exists(mp3_folder):
    os.makedirs(mp3_folder)


m4a_files = [f for f in os.listdir(m4a_folder) if f.endswith(".m4a")]


for m4a_file in m4a_files:
    input_path = os.path.join(m4a_folder, m4a_file)
    output_file = os.path.splitext(m4a_file)[0] + ".mp3"
    output_path = os.path.join(mp3_folder, output_file)
    audio_clip = AudioFileClip(input_path)
    audio_clip.write_audiofile(output_path)

print("Conversion complete.")
