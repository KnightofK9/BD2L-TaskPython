import Constant
from VideoExtractor import VideoExtractor
from Detector import Detector

video_extractor = VideoExtractor()
video_extractor.extract_to(video_extractor.get_random_stream_url(), Constant.VIDEO_EXTRACT_OUTPUT_PATH, 0.5, 100, True)

# detector = Detector(Constant.DARK_NET_CFG_PATH + "yolo.cfg", Constant.WEIGHT_PATH + "yolo.weights",
#                     Constant.DARK_NET_CFG_PATH + "coco.data")
# detector.detect_all_image_in_folder(Constant.IMAGE_DETECT_INPUT_PATH,
#                                     Constant.IMAGE_DETECT_OUTPUT_PATH)
