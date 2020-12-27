from moviepy.editor import VideoFileClip

yuan_video = VideoFileClip('linyilian.mp4')
audio = yuan_video.audio
video = VideoFileClip('/media/hy/Seagate Expansion Drive/Results/sandy.mp4')
videoclip2 = video.set_audio(audio)
videoclip2.write_videofile('/media/hy/Seagate Expansion Drive/Results/sandy_final.mp4')