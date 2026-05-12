import psutil

def current_cpu_usage():
    
    threshold = int(input("Enter the threshold CPU Percentage value: "))

    current_cpu_percentage= psutil.cpu_percent(interval=1)

    print("Current CPU percentage=",current_cpu_percentage)

    if threshold < current_cpu_percentage:
        print("Current CPU percentage is ",current_cpu_percentage,"Alert Notification mail has been sent")
    else:
        print("CPU is in safe state..!!")

current_cpu_usage()