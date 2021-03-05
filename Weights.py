import re
import os
import subprocess
import sys

class _WeightsUrls_(object):
    """
    Mapping from cfg files to officially released YOLOv4 weights
    """
    CONFIG_PATH_TO_URL_SUFFIX= {
    "cfg/yolov4.cfg": "https://drive.google.com/file/d/137U-oLekAu-J-fe0E_seTblVxnU3tlNC/view?usp=sharing",
    "cfg/yolov4-pacsp-s.cfg": "https://drive.google.com/file/d/1-QZc043NMNa_O0oLaB3r0XYKFRSktfsd/view?usp=sharing",
    "cfg/yolov4-pacsp.cfg": "https://drive.google.com/file/d/1sIpu29jEBZ3VI_1uy2Q1f3iEzvIpBZbP/view?usp=sharing",
    "cfg/yolov4-pacsp-x.cfg":"https://drive.google.com/file/d/1aZRfA2CD9SdIwmscbyp6rXZjGysDvaYv/view?usp=sharing",
    "cfg/yolov4-pacsp-s-mish.cfg": "https://drive.google.com/file/d/1q0zbQKcSNSf_AxWQv6DAUPXeaTywPqVB/view?usp=sharing",
    "cfg/yolov4-pacsp-mish.cfg": "https://drive.google.com/file/d/116yreAUTK_dTJErDuDVX2WTIBcd5YPSI/view?usp=sharing",
    "cfg/yolov4-pacsp-x-mish.cfg": "https://drive.google.com/file/d/1GGCrokkRZ06CZ5MUCVokbX1FF2e1DbPF/view?usp=sharing"
    }

def download_weights(weights_url,file_name):
    """
    Given a Google Drive link corresponding to a YOLOv4 weights file, downloads the weights and places them under the weights weights_folder
    Args:
        weights_url (str): Google Drive link to YOLOv4 weights file
        file_name (str): the name of the file in which weights will be saved
    """
    # file_id is a unique identifier of the Google Drive File
    file_id = re.findall(r"(?<=d\/)(.*)(?=\/view)",weights_url)[0]
    cmd_head = "bash ./gdrive.sh"
    cmd = cmd_head + " " + file_id + " " + file_name
    try:
        subprocess.call(cmd.split(" "))
        print('Download finished successfully - Proceeding')
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        print("Exiting")
        sys.exit(1)
    return None


def get_weights_url(config_path):
    """
    Returns the URL to the model trained using the given config
    Args:
        config_path (str): config file name relative to Pytorch_YOLOv4
            directory, e.g., "cfg/yolov4.cfg"
    Returns:
        str: a URL to a Google Drive file that contains the model weights
    """
    if config_path in _WeightsUrls_.CONFIG_PATH_TO_URL_SUFFIX:
        weights_url = _WeightsUrls_.CONFIG_PATH_TO_URL_SUFFIX[config_path]
    return weights_url

def check_for_weights(config_path,folder='weights',postfix='weights'):
    """
    Checks if the weights file is already downloaded in the weights folder, else calls the subroutine responsible for downloading
    Args:
        config_path (str): config file name relative to Pytorch_YOLOv4
            directory, e.g., "cfg/yolov4.cfg"
        postfix(str): string name for file extension (default: weights)
    """
    weights_folder = os.path.join(os.getcwd(),folder)
    model_name = re.findall(r"(?<=cfg\/)(.*)(?=\.cfg)",config_path)[0]
    weights_file = os.path.join(weights_folder,model_name + '.' + postfix)
    if os.path.exists(weights_file):
        print('Already downloaded, found in {}'.format(weights_file))
    else:
        print('Doesnt exist, proceeding to download')
        weights_url=get_weights_url(config_path)
        print('Downloading weights from {}'.format(weights_url))
        download_weights(weights_url,weights_file)
    return weights_file

def check_for_model(config_path):
    """
    checks if the given cfg file corresponds to officially released Pytorch_YOLOv4 models

    """
    print("Checks if cfg file {} corresponds to any officialy released Pytorch_YOLOv4 models".format(config_path))
    model_name = model_name = re.findall(r"(?<=cfg\/)(.*)(?=\.cfg)",config_path)[0]
    if config_path in _WeightsUrls_.CONFIG_PATH_TO_URL_SUFFIX:
        print("{} is available in Pytorch_YOLOv4".format(model_name))
        return True
    else:
        print("{} not available in Pytorch_YOLOv4".format(model_name))
        return False

def get_weights(config_path):
    """
    Given a configuration file, returns the path to the corresponding
    """
    if (check_for_model(config_path)):
        weights_file=check_for_weights(config_path)
    try:
        return weights_file
    except UnboundLocalError:
        print('Please provide a correct configuration file matching one of the officially released YOLOv4 models available')
        sys.exit(1)
