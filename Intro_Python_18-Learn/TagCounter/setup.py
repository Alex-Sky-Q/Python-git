import setuptools as st

st.setup(
    name='TagCounter',
    version='0.1',
    # py_modules=['tagcounter', 'func', 'create_exe', 'db_creation', 'settings'],
    # package_dir={"": "src"},
    # packages=st.find_namespace_packages(where='src'),  # For unknown reason it doesn't find the package
    packages=['tgc'],
    include_package_data=True,
    package_data={'': ['domains_syn.yml', 'tags_count.db']},
    # data_files=[('Lib/site-packages', ['domains_syn.yml'])],
    install_requires=['lxml', 'bs4', 'requests', 'pyyaml', 'loguru'],
    entry_points={'console_scripts': ['tagcounter=tgc:tagcounter.main']},  # To enable run via python "Scripts" dir
    url='https://github.com/Alex-Sky-Q/Python-git/tree/master/Introduction-to-Python-18-Learn/TagCounter',
    author='Alex Sky',
    author_email='contact_via_github',
    description='A program to query a site, count its tags and store it in a local DB'
)
