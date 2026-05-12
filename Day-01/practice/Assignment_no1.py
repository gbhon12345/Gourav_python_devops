#Takes threshold values (CPU, disk, memory) from user input
#Also fetches system metrics using a Python library (example: psutil)
#Compares metrics against thresholds
#Prints the result to the terminal


import psutil
Threshold=[60,65,90]
def cpu_health_check():
    #CPU_Threshold = int(input("Please enter threshold percentage for CPU Usage : "))
    for CPU_Threshold in Threshold:

        Current_CPU_Percentage = psutil.cpu_percent(interval=1)

        if Current_CPU_Percentage > CPU_Threshold:
            print(f"Current CPU usage {Current_CPU_Percentage} higher than  Threshold value {CPU_Threshold} ")
            print("Alert Notification has been sent to the System team and Operation team")
        else:
            print(f"CPU Utilization {Current_CPU_Percentage} is safe..!")
#cpu_health_check()

def disk_health_check():
    #DISK_Threshold = int(input("Please enter threshold percentage for Disk Usage : "))
    #DISK_Threshold = 80
    for DISK_Threshold in Threshold:
        Current_DISK_usage= psutil.disk_usage('/')
        #current_disk_percentage = (Current_DISK_usage.used/Current_DISK_usage.total)*100
        current_disk_percentage = (Current_DISK_usage.percent)
        print(Current_DISK_usage.percent)

        if current_disk_percentage > DISK_Threshold:
            print(f"Current DISK usage {current_disk_percentage} higher than  Threshold value {DISK_Threshold} ")
            print("Alert Notification has been sent to the System team and Operation team")
        else:
            print(f"Disk utilization {current_disk_percentage} is safe..!")

#disk_health_check()

def memory_health_check():
    #Memory_Threshold = int(input("Please enter threshold percentage for Memory Usage : "))
    #Memory_Threshold = 75
    #for Memory_Threshold in Threshold:
        Current_Memory_usage = psutil.virtual_memory()
        Current_mem_percent = Current_Memory_usage.percent
        print(Threshold[2] )
        print(Threshold[1] )
        print(Threshold[0] )
        
        if Threshold[2]  < Current_mem_percent:
            print(f"Current Memory usage {Current_mem_percent} more than Threshold {Threshold[2]} Its an High priority Alert")
            print("Alert Notification has been sent to the System team and Operation team") 

        elif Threshold[1] < Current_mem_percent:
            print(f"Current Memory usage {Current_mem_percent} more than Threshold {Threshold[1]} It is moderate Alert")
            print("Please  monitor closely before it reaches to 80%")
        elif Threshold[0] < Current_mem_percent:
            print(f"Current Memory usage {Current_mem_percent} more than Threshold {Threshold[0]} It is low priority alert ")
            print("Alert Notification has been sent to the System team and Operation team") 
        else:     
            print("Memory utilization is safe..!")

# memory_health_check()

i = 0

while (i < 1):

    print("++++++++++++++++++++++SYSTEM TEST START+++++++++++++++++++++++")
    print("CPU Health Check Start ...")
    print("########################################################################")
    cpu_health_check()
    print("########################################################################")
    print("CPU Health Check End...Thanks you for your convinience")
    print("########################################################################")
    print("                                                                          ")
    print("                                                                          ")
    print("                                                                          ")
    print("########################################################################")
    print("Disk Health Check Start ...")
    print("########################################################################")
    disk_health_check()
    print("########################################################################")
    print("Disk Health Check End...Thanks you for your convinience")
    print("########################################################################")
    print("                                                                          ")
    print("                                                                          ")
    print("                                                                          ")

    print("########################################################################")
    print("Memory Health Check Start ...")
    print("########################################################################")
    memory_health_check()
    print("########################################################################")
    print("Memory Health Check End...Thanks you for your convinience")    
    print("+++++++++++++++++++++++++ SYSTEM TEST END +++++++++++++++++++++++++")
    print("                                                                          ")
    print("                                                                          ")
    print("                                                                          ")
    i = i+1
