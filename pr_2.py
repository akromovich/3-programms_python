import moviepy.editor
from pathlib import Path

video_file = 0

video = moviepy.editor.VideoFileClip('morgen.mp4')
audio = video.audio
audio.write_audiofile('morgen.mp3')