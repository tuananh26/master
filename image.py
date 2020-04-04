import pathlib

SOURCE_IMAGE = pathlib.Path(__file__).parent / 'src/image'


def convert_path(path):
    return '/'.join(str(path).split('\\'))


path_img_x = convert_path(SOURCE_IMAGE/'x.PNG')
path_img_o = convert_path(SOURCE_IMAGE/'o.PNG')
