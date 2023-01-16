import os
import json
files = os.listdir('.\\images\\gallery\\')
x = {"gallery": files}
y = json.dumps(x)

with open('galleryIMG.json','w') as f:
    f.write(y)