#!/usr/bin/env python3

import sys
import subprocess

import parse_video_info
import highest_resolutions_video_cmd

def you_get_i_url(video_url):
    youtube_video = 'https://www.youtube.com' + video_url
    p = subprocess.Popen(['you-get' , '-i', '{0}'.format(youtube_video)],
                        stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    p.wait()

    video_info = p.stdout.read().decode('utf8')
    with open('video_info.txt', 'w') as fp:
        fp.write(video_info)
    return video_info


if __name__ == '__main__':
    you_get_i_url(sys.argv[1])
    video = parse_video_info.parse_video_info('video_info.txt')
    final_you_get_cmd = highest_resolutions_video_cmd.get_highest_resolution_video_cmd(video)
    print(final_you_get_cmd + ' "https://www.youtube.com' + sys.argv[1].strip('"') + '"')

