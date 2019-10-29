import os, click
from pdf2image import convert_from_path


@click.command()
@click.argument('pdf_file')
def cmd(pdf_file):
    path = pdf_file
    folder_path = os.path.splitext(path)[0]
    os.mkdir(folder_path)
    images = convert_from_path(path)

    folder_name = os.path.basename(folder_path)

    i = 0
    for image in images:
        image.save(f'{folder_path}/slide{i}.png')
        i+=1

    f = open(f'{folder_path}.md','w')

    for j in range(i):
        f.write(f'![slide{j}](./{folder_name}/slide{j}.png)\n\n')
        f.write('---\n\n')
        f.write('\n\n\n\n\n\n\n\n\n\n')




def main():
    cmd()
