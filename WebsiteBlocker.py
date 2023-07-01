import time

website = input("Enter the website to be blocked seperated by comma: ")
blocked_websites = website.split(",")
host_path = r"C:\Windows\System32\drivers\etc\hosts"
block_duration = 60 #time in seconds

def is_blocked(start_time):
    return time.time() < block_duration + start_time

def blocker():
    with open(host_path,"r+") as host_file:
        file_content = host_file.read()
        for web in blocked_websites:
            if web in file_content:
                pass
            else:
                host_file.write("127.0.0.1 " + web + "\n")

def unblocker():

    with open(host_path,"r+") as host_file:
        file_content = host_file.readlines()
        host_file.seek(0)
        for line in file_content:
            if not any(web in line for web in blocked_websites):
                host_file.write(line)
        
        # removing the blocked websites from the host file
        host_file.truncate()

def website_blocker_timer():
    start_time = time.time()

    blocker() # blocking the websites

    while is_blocked(start_time):

        if is_blocked(start_time):
            print("Access Denied")
        else:
            print("Website Accessible")
    
    unblocker() #Unblocking the websites


website_blocker_timer()