import os
from collections import Counter
from PIL import Image

def get_image_resolutions(directory):
    resolutions = Counter()
    supported_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"}

    for root, _, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1].lower() in supported_extensions:
                filepath = os.path.join(root, file)
                try:
                    with Image.open(filepath) as img:
                        width, height = img.size
                        resolutions[(width, height)] += 1
                except Exception:
                    pass  
    return resolutions

if __name__ == "__main__":
    path = input("Enter directory path: ").strip()
    if not os.path.isdir(path):
        print("Invalid directory path")
    else:
        results = get_image_resolutions(path)

        if results:
            total = sum(results.values())

            w_width = max(len("Width"), max(len(str(w)) for w, _ in results))
            h_width = max(len("Height"), max(len(str(h)) for _, h in results))
            c_width = max(len("Count"), max(len(f"{c:,}") for c in results.values()))

            print("\nImage Resolution Summary\n")
            header = f"{'Width':>{w_width}}  {'Height':>{h_width}}  {'Count':>{c_width}}"
            print(header)
            print("-" * len(header))

            for (w, h), count in sorted(results.items(), key=lambda x: (-x[1], x[0][0], x[0][1])):
                print(f"{w:>{w_width}}  {h:>{h_width}}  {count:>{c_width},}")

            print("-" * len(header))
            print(f"{'Total images:':<{w_width + h_width + 4}} {total:>{c_width},}")
        else:
            print("No images found in this directory.")
