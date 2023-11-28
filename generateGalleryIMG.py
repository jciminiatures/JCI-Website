import os
import json
files = os.listdir(os.path.expanduser('~/Desktop/website-gallery/images/gallery'))
x = {"gallery": files}
try:
    x['gallery'].remove('.DS_Store')
except:
    pass
y = json.dumps(x)

with open('galleryIMG.json','w') as f:
    f.write(y)
