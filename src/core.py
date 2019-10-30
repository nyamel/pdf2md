import os.path
import click
from pdf2image import convert_from_path, convert_from_bytes
from .exceptions import NotPDFFileError


@click.command(options_metavar='<options>')

@click.argument('pdf_file', type=click.Path(exists=True), metavar='YOUR_FILE.pdf')

@click.option('--width', '-w', type=click.INT, default=None, metavar='<int>',
help='Set image width. (default=450)')

@click.option('--height', '-h', type=click.INT, default=None, metavar='<int>',
help='Set image height. (default=None)')

@click.option('--fullsize', '-f', is_flag=True,
help='If this option is enabled, --width and --height are disabled')

@click.option('--linefeed', '-l', default=5, metavar='<int>',
help='Number of line feed between images in Markdown file. (default=5)')


def cmd(pdf_file, width, height, fullsize, linefeed):
    """
    Convert YOUR_FILE.pdf to PNG images and make YOUR_FILE.md with image tags.
    """

    path = pdf_file
    folder_path = os.path.splitext(path)[0]

    if os.path.splitext(path)[1] != '.pdf':
        raise NotPDFFileError('Your file is not a pdf file.')

    try:
        os.mkdir(folder_path)
        click.echo(f'New directory has made: {folder_path}')
        new_dict = True
    except FileExistsError:
        pass

    click.echo('    converting...')
    images = convert_from_path(path, dpi=200, size=set_size(width, height,fullsize))

    i = 0
    with click.progressbar(images, fill_char='█', show_pos=True, show_percent=True) as bar:
        for image in bar:
            image.save(f'{folder_path}/slide{i}.png')
            i += 1
    click.echo('    success!!')

    f = open(f'{folder_path}.md', 'w')
    folder_name = os.path.basename(folder_path)
    for j in range(i):
        f.write(f'![slide{j}](./{folder_name}/slide{j}.png)\n\n')
        f.write('---\n\n')
        for n in range(linefeed):
            f.write('\n\n')


def set_size(width, height, fullsize):
    if fullsize:
        return (None, None)
    else:
        if width == None and height == None:
            return (450, None)
        elif width != None and height == None:
            return (width, None)
        elif width == None and height != None:
            return (None, width)
        else:
            return (width, height)


def main():
    cmd()


if __name__ == '__main__':
    main()
