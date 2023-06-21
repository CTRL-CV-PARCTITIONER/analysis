import psutil
import json
import yaml
from yaml import SafeDumper
import pynvml
import os
import logging
logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(os.path.basename(__file__))


def get_cpu_used():
    logger.info (f"CPU逻辑核心数: {psutil.cpu_count(logical=True)}")
    logger.info (f"CPU物理核心数: {psutil.cpu_count(logical=False)}")
    logger.info (f"CPU使用率: {psutil.cpu_percent()}")
    logger.info (f"CPU Stats: {psutil.cpu_stats()}")


def get_gpu_used():
    pynvml.nvmlInit()
    gpu_count = pynvml.nvmlDeviceGetCount()
    for i in range(gpu_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        gpu_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        logger.info (f" GPU {i}: Total Memory: {gpu_info.total}  Used Memory: {gpu_info.used}  Free Memory: {gpu_info.free}")
    pynvml.nvmlShutdown()

def json_load(path):
    with open(path, encoding="utf-8") as f:
        result = f.read()
    return json.loads(result)

def json_dump(path, param):
    with open(path, 'w') as file:
        json.dump(param, file, indent=4)


def yaml_load(path):
    with open(path, encoding="utf-8") as f:
        result = f.read()
        read_dic = yaml.load(result, Loader=yaml.FullLoader)
    return read_dic

def yaml_dump(path, load_dic):
    SafeDumper.add_representer(
        type(None),
        lambda dumper, value: dumper.represent_scalar(u'tag:yaml.org,2002:null', '')
    )
    with open(path, 'w') as output:
        yaml.safe_dump(load_dic, output, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    get_gpu_used()