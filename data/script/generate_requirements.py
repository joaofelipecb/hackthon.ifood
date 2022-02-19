import sys
try:
    from pip._internal.operations import freeze
except ImportError:
    from pip.operations import freeze

try:
    file_path = sys.argv[1]
    content = '\n'.join(freeze.freeze())
    with open(file_path,'w') as f:
        f.write(content)
    print(f'Requirements file {file_path} generated with success.')
except IndexError:
    print('Please pass the file path where you want to generate the file.')
