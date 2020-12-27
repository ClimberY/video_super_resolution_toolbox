from moviepy.editor import *

video = VideoFileClip('linyilian.mp4')
audio = video.audio
audio.write_audiofile('linyilian.wav')
