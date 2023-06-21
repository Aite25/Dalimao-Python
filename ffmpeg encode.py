# -*- coding: UTF-8 -*-
import subprocess,os

FFMPEG_PATH = "E:/ffmpeg/ffmpeg-master-latest-win64-gpl-shared/bin/ffmpeg.exe"
address = os.getcwd()
format = ".avi"
allfiles = os.listdir(address)

def encode_image_sequence(img_seq_path, output_path, crf=20, preset="veryslow"):

    ffmpeg_cmd = FFMPEG_PATH
    ffmpeg_cmd += " -y "
    ffmpeg_cmd += " -i %s" %img_seq_path

    ffmpeg_cmd += " -c:v libx264 -crf %s -preset %s" %(crf, preset)

    ffmpeg_cmd += ' %s' %output_path
    print (ffmpeg_cmd)
    subprocess.call(ffmpeg_cmd)

if __name__ == "__main__":
    for eachfile in allfiles:
        if eachfile.endswith(format):
            file_prename = os.path.splitext(eachfile)[0]
            img_seq_path = "\""+ address + "\\" + eachfile + "\""
            output_path = "\""+ address + "\\" + file_prename + "_encode.mp4\""
            print(img_seq_path)
            print(output_path)
            encode_image_sequence(img_seq_path, output_path)
            #压缩完之后删除当前文件
            #os.remove(eachfile)
            
print("________________Complete________________")            
