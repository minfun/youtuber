import subprocess
import sys

if __name__ == '__main__':
    command_pattern = """python upload_video.py --noauth_local_webserver --file ./{video_id}.mp4 --description "{description}" --title "{title}" --category 10"""
    video_id = sys.argv[1]
    description = sys.argv[2]
    title = sys.argv[3]
    command = command_pattern.format(video_id=video_id, description=description, title=title)
    print(command)
    stdout = subprocess.run(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    print(stdout.stdout.decode())
