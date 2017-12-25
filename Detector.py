import Constant
import sys
import os
sys.path.append(Constant.DARK_NET_PYTHON_MODULE_PATH)
import darknet


class Detector:
    def __init__(self, input_cfg, intput_weight, input_data):
        self.net = darknet.load_net(input_cfg, intput_weight, 0)
        self.meta = darknet.load_meta(input_data)

    def detect_image(self, image_url):
        return darknet.detect(self.net, self.meta, image_url)

    def detect_all_image_in_folder(self, folder_url):
        list_res = []
        for filename in os.listdir(folder_url):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                list_res.append(self.detect_image(folder_url+filename))
        return list_res
