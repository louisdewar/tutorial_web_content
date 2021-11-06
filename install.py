import sys

if sys.version_info[0] != 3:
    print('Please run this script using python3')
    sys.exit(1)

import json
import urllib.error
import urllib.request
import os
import stat
import tarfile
import shutil
import subprocess

match_release = None
try:
    match_release = sys.argv[1]
# Arguments are not required
except IndexError:
    pass

REPO_RELEASE_URL = 'https://api.github.com/repos/louisdewar/tutorial_web/releases/latest'
try:
    f = urllib.request.urlopen(REPO_RELEASE_URL)
except urllib.error.URLError:
    print('There was an SSL cert verification error')
    print('If you are on a mac and you have recently installed a new version of\
 python then you should navigate to "/Applications/Python {VERSION}/"')
    print('Then run a script in that folder called "Install Certificates.command"')
    sys.exit(1)

response = json.loads(f.read())

print('Current version tag:', response['tag_name'])

assets = [asset for asset in response['assets']
          if asset['name'].endswith('.tar.gz')]

if match_release:
    try:
        asset_choice = next(
            asset for asset in assets if match_release in asset['name'])
        print('Automatically picked {} to download based on match "{}"\n'.format(
            asset_choice['name'], match_release))
    except StopIteration:
        print('Couldn\'t find "{}" in releases'.format(match_release))
else:
    print('\nPick a release to download:')
    for (i, asset) in enumerate(assets):
        print(str(i + 1) + '.', asset['name'])

    while True:
        try:
            release_number = int(input('Enter a number: '))

            # If number in range we can exit this loop
            if release_number > 0 and release_number <= len(assets):
                break
        except ValueError:
            pass

        print('Please enter a valid number')

    asset_choice = assets[release_number - 1]

download_url = asset_choice['browser_download_url']

# Folder where this script is + bin
bin_dir = os.path.join(os.path.dirname(__file__), 'bin')

print('Downloading', asset_choice['name'], 'to', bin_dir)
print('({})'.format(download_url))

# Clear bin directory if it exists
if os.path.exists(bin_dir):
    shutil.rmtree(bin_dir)

os.mkdir(bin_dir)

zip_path = os.path.join(bin_dir, asset_choice['name'])

# Download zip file
urllib.request.urlretrieve(download_url, zip_path)

# Open and extract zip file
tar_file = tarfile.open(zip_path)
tar_file.extractall(bin_dir)

# Delete zip file
os.remove(zip_path)

# Path to the actual binary program (normally called tutorial_web)
binary_path = os.path.join(bin_dir, 'tutorial_web')

if not os.path.exists(binary_path):
    print('Couldn\'t find the binary file `tutorial_web` in the bin directory')
    print('This probably means that there was a problem with the download or you chose windows (.exe file)')
    sys.exit(1)

# Make binary executable
st = os.stat(binary_path)
os.chmod(binary_path, st.st_mode | stat.S_IEXEC)

# Run help
print('\n\n')
print(binary_path + ' --help')
subprocess.run([binary_path, '--help'])
