import Constant
from VideoExtractor import VideoExtractor

video_extractor = VideoExtractor()
video_extractor.extract_to(video_extractor.get_random_stream_url(), "./out/", 0.5, 10)
