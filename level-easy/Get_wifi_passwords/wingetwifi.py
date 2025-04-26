# Source Code of Getting WiFi Passwords using Python in Windows

# importing subprocesses
import subprocess

# getting meta data
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

# decoding meta data
data = meta_data.decode('utf-8', errors="backslashreplace")

# spliting data line by line 
data = data.split('\n')

# creating a list of profiles
profile = []

# traverse the data
for i in data:
    # find "all user profile" in each item
    if "All User Profile" in i:
        #if found, split the item
        i = i.split(":")
        
        # item at index 1 will be wifi name
        i = i[1]
        
        # formating the name
        # first and last character is less used
        i = i[1:-1]
        
        # appending the wifi name in profile list
        profile.append(i)
        
print("{:<30}|{:<}".foramt("wifi name", "password"))
print("-------------------------------------------")

# traversing the profiles
for i in profile:
    
    # try catch block begins
    # try block
    try:
        # getting meta data with passwords using wifi names
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear'])
        
        #decoding and spliting data line by line
        results = results.decode('utf-8', errors="backslashreplace")
        results = results.split('\n')
        
        # finding passwords for the results list
        results = [b.split(":")[1][1:-1] for b in results if "key content" in b]
        
        # if there is password it will print the password
        print("{:<30}|{:<}".format(i, results[0]))
        
        # else it will print blank in front of password
    except IndexError:
        print("{:<30}|{:<}".format(i, ""))
        
    # and when this process get failed 
    except subprocess.CalledProcessError:
        print('Encoding Error Occured')