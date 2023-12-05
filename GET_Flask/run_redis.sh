echo "Installing and configuring environment..."
python3 -q -m venv venv
source venv/bin/activate

# pip3 install -r requirements.txt
export APP_SETTINGS=config.DevelopmentConfig
python3 /home/reid/Documents/Code/get_site/GET_Flask/GET_project/api/worker.py
