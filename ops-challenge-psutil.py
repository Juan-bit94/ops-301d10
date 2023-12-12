import os
import psutil

# This gets system information
def system_main_info():
    info = {
        'User Mode Time': psutil.cpu_times().user,
        'Kernel Mode Time': psutil.cpu_times().system,
        'Idle Time': psutil.cpu_times().idle,
        'Priority User Mode Time': psutil.cpu_times().nice,
        'I/O Wait Time': psutil.cpu_times().iowait,
        'Hardware Interrupt Time': psutil.cpu_times().irq,
        'Software Interrupt Time': psutil.cpu_times().softirq,
        'Virtualized OS Time': psutil.cpu_times().steal,
        'Gust OS Time': psutil.cpu_times().guest,
    }
    return info

# This saves info to a text file
def save_to_file(info):
    file_path = 'system_info.txt'
    with open(file_path, 'w') as file:
        for key, value in info.items():
            file.write(f'{key}: {value}\n')
    return file_path

# This displays the info and the directory location for the file
def display_info(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
        print(f'File Contents:\n{file_contents}')
        
    directory_location = os.path.abspath(file_path)
    print(f'\nDirectory Location:\n{directory_location}')
               
if __name__ == "__main__":
    system_info = system_main_info()
    
    saved_file_path = save_to_file(system_info)
    
    display_info(saved_file_path)
