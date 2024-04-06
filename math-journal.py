import errno
import os
from datetime import datetime

now = datetime.now()
year = now.strftime('%Y');
month = now.strftime('%m');
day = now.strftime('%d');

# Navigate to the year directory and make it if it doesn't exist
path = os.path.join(year,month);

if not os.path.exists(path):
    os.makedirs(path)

file_path = path + '/' +  day + '.tex'

madeNewFile = False;

if not os.path.isfile(file_path):
    madeNewFile = True;

    print('made a file')
    # The 'x' flag will only 
    with open(file_path,'x') as file:
        file.close()
else:
    print('is a file')

############

# We now have a file if we need it. Time to edit the list of dates in the main file
