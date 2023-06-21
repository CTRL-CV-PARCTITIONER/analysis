import os
import shutil
import argparse
import sys
sys.path.append(
    os.path.dirname(
         os.path.dirname(
             os.path.abspath(__file__)
         )
    )
)
from utils.tools import json_load, json_dump
from utils.base_multiprocess import Multiprocess
from configuration.config import _type
import logging
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(os.path.basename(__file__))


def analysis_txt_function(line, param):
    return {os.getpid(): line.strip()}
    
def analysis_txt(text_path, save_path, processes_number):
    reader = open(text_path)
    lines = reader.readlines()
    reader.close()
    save_path = os.path.join(
        save_path, 
        text_path.split("/")[-1].replace(".txt", ".json")
    )
    params = (
        "python",
        "java",
        "c++"
    )
    Mul = Multiprocess(
        lines=lines,
        processes_number=processes_number,
        function=analysis_txt_function,
        params=params,
    )
    result = Mul()
    json_dump(save_path, result)

def analysis_csv(text_path, save_path, processes_number):
    pass

def analysis_xls(text_path, save_path, processes_number):
    pass

def analysis_json(text_path, save_path, processes_number):
    json_load(text_path)
    name = os.path.join(save_path, text_path.split("/")[-1])
    if not os.path.exists(name):
        logger.info(f"writing to {name}")
        shutil.copy(text_path, name)
    else:
        logger.info(f"{name} exists, continue!")

def analysis_html(text_path, save_path, processes_number):
    pass


def main(text_path, save_path, suffix, processes_number):
    execute_object = {
        "txt"   :   lambda: analysis_txt(text_path, save_path, processes_number),
        "csv"   :   lambda: analysis_csv(text_path, save_path, processes_number),
        "xlsx"  :   lambda: analysis_xls(text_path, save_path, processes_number),
        "xls"   :   lambda: analysis_xls(text_path, save_path, processes_number),
        "json"  :   lambda: analysis_json(text_path, save_path, processes_number),
        "html"  :   lambda: analysis_html(text_path, save_path, processes_number),
    }
    execute_object[suffix]()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analysis text convert to json for current pipline ")
    parser.add_argument("--text_path", default="C:/Users/weidong.he/Desktop/1/txt/train_FSD_Site_NC110_20221228_side.txt", help="text location original path")
    parser.add_argument("--save_path", default="C:/Users/weidong.he/Desktop/1", help="text location save path")
    parser.add_argument("--processes_number", default=5, type=int, help="max processes")
    args = parser.parse_args()
    suffix = args.text_path.split(".")[-1]
    assert suffix in _type
    main(args.text_path, args.save_path, suffix, args.processes_number)