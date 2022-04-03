from tgc import func
import sys
from loguru import logger


# Start the app, check and process the arguments
def main():
    logger.remove()
    logger.add('get.log', format='{message}', rotation="50 MB")

    if len(sys.argv) == 1:
        func.run_gui()
    elif len(sys.argv) == 3:
        comm = sys.argv[1]
        if '"' in sys.argv[2]:
            site = sys.argv[2].strip('"')
        elif "'" in sys.argv[2]:
            site = sys.argv[2].strip("'")
        else:
            site = sys.argv[2]
        func.run_command(comm, site)
    else:
        print(func.ENTER_SITE_COMM)


# To enable two run types: direct and via python "Scripts" directory (after installation)
if __name__ == '__main__':
    main()
