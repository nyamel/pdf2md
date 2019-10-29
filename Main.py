from pdf2image import convert_from_path, convert_from_bytes
import os


path = input('変換するpdfファイルを入力してください:')
folder_path = os.path.splitext(path)[0]
os.mkdir(folder_path)
images = convert_from_path(path)



i = 0
for image in images:
    image.save(f'{folder_path}/test{i}.png')
    i+=1

f = open(f'{folder_path}test.md','w')

for j in range(i):
    f.write(f'![test{j}](./test{j}.png)\n\n')
    f.write('---\n\n')
    f.write('\n\n\n\n\n\n\n\n\n\n')
