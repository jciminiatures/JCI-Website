import os
import json

gallery_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images", "gallery")

with open("manifest.json","w") as f:
    files = os.listdir(gallery_path)

    # MACOS bypass
    try:
        files.remove(".DS_Store")
    except:
        pass

    f.write(json.dumps({"gallery": files}))
    
    print("[OK]: Finished creating manifest from gallery.")