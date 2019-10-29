import os.path, click
from pdf2image import convert_from_path, convert_from_bytes
from tqdm import tqdm

@click.command()
@click.argument('pdf_file')
def cmd(pdf_file):
    path = pdf_file
    folder_path = os.path.splitext(path)[0]

    try:
        os.mkdir(folder_path)
        print(f'New directory has made: {folder_path}')
        new_dict = True
    except FileExistsError:
        pass

    print('converting...')

    images = convert_from_path(path, dpi=200, size=(500, None))


    folder_name = os.path.basename(folder_path)

    i = 0

    for image in tqdm(images):
        image.save(f'{folder_path}/slide{i}.png')
        i+=1
    print('success!!')
    f = open(f'{folder_path}.md','w')

    for j in range(i):
        f.write(f'![slide{j}](./{folder_name}/slide{j}.png)\n\n')
        f.write('---\n\n')
        f.write('\n\n\n\n\n\n\n\n\n\n')




def main():
    cmd()
