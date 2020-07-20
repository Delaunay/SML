import os
import shutil

source = os.path.dirname(__file__)
destination = 'C:/Users/Newton/work/satisfactory_mod/SatisfactoryModLoader/'


def copy_sml_to_loader():
    shutil.rmtree(os.path.join(destination, 'Source', 'SML'))
    shutil.copytree(
        os.path.join(source, 'Source'),
        os.path.join(destination, 'Source', 'SML'))


def copy_loader_to_sml():
    shutil.rmtree(os.path.join(source, 'Source'))
    # os.makedirs(os.path.join(source, 'Source'), exist_ok=True)
    shutil.copytree(
        os.path.join(destination, 'Source', 'SML'),
        os.path.join(source, 'Source'))


# copy_sml_to_loader()

copy_loader_to_sml()
