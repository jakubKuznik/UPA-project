# Exit on error
set -e

# Create a virtual environment
#python3 -m venv venv

# Activate the virtual environment
#source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install driver
#wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip

#unzip chromedriver_linux64.zip -d ./drivers

#chmod +x ./drivers/chromedriver


# Run any pre-build commands or tasks
# For example, database migrations, compiling assets, etc.

#get latest version
#version=`curl http://chromedriver.storage.googleapis.com/LATEST_RELEASE`;
#echo 'Currently LATEST_RELEASE:' $version;
#download the latest version chrome driver available as per the above line
#wget -N http://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip
#unzip chromedriver_linux64.zip -d .
#chmod a+x ./chromedriver
#upgrade to latest google chrome 
#yum upgrade google-chrome-stable
#google_version=`google-chrome --version`;
#echo 'Google Chrome Version:' $google_version;
#echo 'Currently LATEST_RELEASE:' $version;
#echo 'End of the script'

# Run tests
#python manage.py test

# Run any additional build steps

# Deactivate the virtual environment
#deactivate

echo "Build completed successfully."

