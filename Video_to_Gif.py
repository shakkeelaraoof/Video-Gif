from moviepy.editor import VideoFileClip

clip = VideoFileClip("abcd.mp4")#the file which need to Convert
clip.write_gif("mygif.gif")#to save the file give the extention '--FileName.gif-- '

#using this we can change the FPS of the video
#clip.write_gif("mygif.gif", fps=10)


