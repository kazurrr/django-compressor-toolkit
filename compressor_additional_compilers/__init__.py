# PEP 440 - version number format
VERSION = (0, 7, 1)

# PEP 396 - module version variable
__version__ = '.'.join(map(str, VERSION))

default_app_config = 'compressor_additional_compilers.apps.CompressorToolkitConfig'
