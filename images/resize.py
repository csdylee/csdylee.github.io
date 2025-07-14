import os
from PIL import Image

# 이미지 폴더 경로
IMAGE_DIR = "./"
# 최대 해상도
MAX_WIDTH = 1920
MAX_HEIGHT = 1080

# 지원하는 확장자
EXTS = (".jpg", ".jpeg", ".png")

for filename in os.listdir(IMAGE_DIR):
    if filename.lower().endswith(EXTS):
        path = os.path.join(IMAGE_DIR, filename)
        try:
            with Image.open(path) as img:
                w, h = img.size
                # 리사이즈가 필요한 경우만 처리
                if w > MAX_WIDTH or h > MAX_HEIGHT:
                    img.thumbnail((MAX_WIDTH, MAX_HEIGHT), Image.LANCZOS)
                    img.save(path)
                    print(f"{filename}: {w}x{h} → {img.size[0]}x{img.size[1]}")
                else:
                    print(f"{filename}: {w}x{h} (변경 없음)")
        except Exception as e:
            print(f"{filename}: 처리 실패 - {e}")