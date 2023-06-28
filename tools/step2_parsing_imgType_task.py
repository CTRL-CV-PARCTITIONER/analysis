import numpy as np
import cv2
import os
import argparse
import base64
import sys
sys.path.append(
    os.path.dirname(
         os.path.dirname(
             os.path.abspath(__file__)
         )
    )
)
from utils.base_multiprocess import Multiprocess
import logging
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(os.path.basename(__file__))

def img_convert_binary(img_path, params):
    image = cv2.imread(img_path)
    try:
        _, binary_data = cv2.imencode('.jpg', image)
        binary_data = binary_data.tobytes()
        key = img_path.split("/")[-1].replace(".jpg", "").encode()
    except:
        _, binary_data = cv2.imencode('.png', image)
        binary_data = binary_data.tobytes()
        key = img_path.split("/")[-1].replace(".png", "").encode()
    return (str({key: binary_data}) + "\n").encode()

def binary_convert_img(binary_text, save_path):
    str_binary = binary_text.decode("utf-8").strip()
    json_binary = eval(str_binary)
    name = list(json_binary.keys())[0].decode("utf-8")
    binary_data = list(json_binary.values())[0]
    base64_data = base64.b64encode(binary_data)
    decoded_data = base64.b64decode(base64_data)
    restored_image = cv2.imdecode(
        np.frombuffer(decoded_data, np.uint8),
        cv2.IMREAD_COLOR
    )
    
    '''save img'''
    # img_path = save_path + "/" + name
    # cv2.imwrite(img_path, restored_image)
    
    '''show img'''
    cv2.imshow('Restored Image', restored_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main(args):
    lines = [
        args.img_path + "/" + img
        for img in os.listdir(args.img_path)
    ]
    params = ()
    Mul = Multiprocess(
        lines=lines,
        processes_number=args.processes_number,
        function=img_convert_binary,
        params=params
    )
    result = Mul()
    save_path = os.path.join(
        args.save_path + "/" + "image_binary.bin"
    )
    with open(save_path, 'wb') as file:
        for res in result: file.write(res)
    logger.info(f"saved to {save_path}")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analysis img convert to text for current pipline")
    parser.add_argument("--img_path", default="C:/Users/weidong.he/Desktop/1/bigsize_V2", help="img location original path")
    parser.add_argument("--save_path", default="C:/Users/weidong.he/Desktop", help="img location save path")
    parser.add_argument("--processes_number", default=5, type=int, help="max processes")
    args = parser.parse_args()
    main(args)