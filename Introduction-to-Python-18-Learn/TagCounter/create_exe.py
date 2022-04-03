# Create a portable exe
import PyInstaller.__main__

PyInstaller.__main__.run([
    'tgc/tagcounter.py',
    '--add-data=tgc/tags_count.db;tgc',
    '--add-data=tgc/domains_syn.yml;tgc',
    '--add-data=tgc/TC_36896_32.ico;tgc',
    # '--icon=tgc/TC_36896.ico',  # icon for exe file
    '--onefile',
    '--windowed'
])
