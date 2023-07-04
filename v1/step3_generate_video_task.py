import cv2
import os
import argparse
import sys
from tqdm import tqdm
sys.path.append(
    os.path.dirname(
         os.path.dirname(
             os.path.abspath(__file__)
         )
    )
)
import logging
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(os.path.basename(__file__))

def main(args):
    width = args.width
    height = args.height
    fps = args.fps
    img_path = args.img_path
    video_name = args.video_name
    save_path = args.save_path
    video_save_path = os.path.join(save_path, f"{video_name}.mp4").replace("\\", "/")
    logger.info (f"video save path: {video_save_path}")

    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video_writer = cv2.VideoWriter(video_save_path, fourcc, fps, (width, height))

    #get first img shape
    first_img = os.path.join(img_path, os.listdir(img_path)[0])
    first_img_reader = cv2.imread(first_img)
    logger.info (f"first img shape: {first_img_reader.shape}  current use shape: ({width},{height})")

    # Generate gradient image frames and write video
    for img_name in tqdm(os.listdir(img_path)):
        img = os.path.join(img_path, img_name).replace("\\", "/")
        frame = cv2.imread(img)
        frame = cv2.resize(frame, (width, height))
        # Writes frames to video
        video_writer.write(frame.astype('uint8'))
        
    # release resource
    video_writer.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="generate video for current pipline")
    parser.add_argument("--img_path", default="C:/Users/weidong.he/Desktop/1/fisheye_front_cylinder", help="img location original path")
    parser.add_argument("--save_path", default="C:/Users/weidong.he/Desktop", help="video location save path")
    parser.add_argument("--video_name", default="video")
    parser.add_argument("--width", default=960, type=int)
    parser.add_argument("--height", default=720, type=int)
    parser.add_argument("--fps", default=10, type=int)
    args = parser.parse_args()
    main(args)