import os
import argparse
import logging
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(os.path.basename(__file__))


def step_execute_file(step, args) -> str:
    if args.version == "v1":
        step_execute_file_v1 = {
            "step1": "python3 pipline1.0/step1_parsing_textType_task.py ",
            "step2": "python3 pipline1.0/step2_parsing_imgType_task.py ",
            "step3": "python3 pipline1.0/step3_generate_video_task.py ",
            "step4": "python3 pipline1.0/step4_data_visualization_task.py ",
            "step5": "python3 pipline1.0/step5_get_data_from_database.py ",
        }
        return step_execute_file_v1[step]
    else:
        raise ModuleNotFoundError(f"version {args.version} is developing !!!")
    

def step_params(step, args) -> str:
    step_param = {
        "step1": 
            f"--text_path {args.text_path} --save_path {args.save_path} --processes_number {args.processes_number}",
        "step2": 
            f"--img_path {args.img_path} --save_path {args.save_path} --processes_number {args.processes_number}",
        "step3": 
            f"--img_path {args.img_path} --save_path {args.save_path} --video_name {args.video_name} --width {args.width} --height {args.height} --fps {args.fps}",
        "step4": 
            f"--data_path {args.img_path} --save_path {args.save_path} ",
        "step5": 
            f'--sql "{args.sql}" ',
    }
    return step_param[step]


def main(args):
    step_list = args.step.split("_")
    for step in step_list:
        execute = step_execute_file(step, args) + step_params(step, args)
        os.system(execute)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="generate video for current pipline")
    parser.add_argument("--step", default="step5", help="img location original path")
    parser.add_argument("--sql", default="select * from student limit 10", help="execute sql")
    parser.add_argument("--text_path", default="C:/Users/weidong.he/Desktop/1/txt/train_FSD_Site_NC110_20221228_side.txt", help="text location original path")
    parser.add_argument("--img_path", default="C:/Users/weidong.he/Desktop/1/fisheye_front_cylinder", help="text location original path")
    parser.add_argument("--save_path", default="C:/Users/weidong.he/Desktop/1", help="text location save path")
    parser.add_argument("--processes_number", default=10, type=int, help="max processes")
    parser.add_argument("--video_name", default="video")
    parser.add_argument("--width", default=960, type=int)
    parser.add_argument("--height", default=720, type=int)
    parser.add_argument("--fps", default=10, type=int)
    parser.add_argument("--version", default="v1")
    args = parser.parse_args()
    main(args)