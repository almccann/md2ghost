import os
import sys
from converter import MarkdownConverter


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print('Usage: python -m /path/to/notes > /path/to/ghost.json')
        sys.exit(1)
    filepath = os.path.expanduser(args[0])
    if not os.path.exists(filepath):
        print('File does not exist: %s' % filepath)
        sys.exit(1)
    converter = MarkdownConverter(filepath)
    converter.convert()
    sys.exit()


if __name__ == '__main__':
    main()
