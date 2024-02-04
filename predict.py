# image_to_video.py

import cv2
import argparse

def create_video(image_path, audio_path, output_path='output_video.mp4', frame_rate=25):
    # Load the audio file
    wav = audio.load_wav(audio_path, 16000)

    # Get the duration of the audio in seconds
    audio_duration = len(wav) / 16000.0

    # Load the image
    image = cv2.imread(image_path)

    # Create a video with the image repeating to match the audio duration
    num_frames = int(audio_duration * frame_rate)

    # Resize image to video frame size
    frame_height, frame_width, _ = image.shape
    video_size = (frame_width, frame_height)
    resized_image = cv2.resize(image, video_size)

    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_path, fourcc, frame_rate, video_size)

    # Write the resized image to the video for the specified duration
    for _ in range(num_frames):
        video_writer.write(resized_image)

    # Release the video writer
    video_writer.release()

    print(f'Video created successfully: {output_path}')

def main():
    parser = argparse.ArgumentParser(description='Create a video with image duration matching the length of an audio file')

    parser.add_argument('--image', type=str, help='Filepath of the image to use', required=True)
    parser.add_argument('--audio', type=str, help='Filepath of the audio file to use', required=True)
    parser.add_argument('--outfile', type=str, help='Video path to save result', default='output_video.mp4')
    parser.add_argument('--frame_rate', type=int, help='Frame rate of the output video', default=25)

    args = parser.parse_args()

    create_video(args.image, args.audio, args.outfile, args.frame_rate)

if __name__ == '__main__':
    main()
