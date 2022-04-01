import func
import sys

if len(sys.argv) == 1:
    func.run_gui()
else:
    comm = sys.argv[1]
    site = sys.argv[2]
    func.run_command(comm, site)

# url = 'https://' + 'skyfitness.ru'
# func.db_reader(url)

# Temporary write to file - logs in the future
# func.dict_writer(tags)



