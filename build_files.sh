# build_files.sh
#!/bin/bash
pip install -r requirements.txt
python3.9 manage.py collectstatic
