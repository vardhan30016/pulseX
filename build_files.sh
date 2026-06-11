# Install dependencies
python3.12 -m pip install -r requirements.txt

# Collect static files
python3.12 pulsex/manage.py collectstatic --noinput --clear
