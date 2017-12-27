import Constant
from VideoExtractor import VideoExtractor

video_extractor = VideoExtractor()
video_extractor.extract_to(video_extractor.get_random_stream_url(), Constant.VIDEO_EXTRACT_OUTPUT_PATH, 0.5, 10, True)
