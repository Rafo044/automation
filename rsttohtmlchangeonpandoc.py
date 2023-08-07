
# Change Rst to Html 
import os
import subprocess

def rst_to_html(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".rst"):
                rst_file_path = os.path.join(root, file)
                html_file_path = os.path.splitext(rst_file_path)[0] + ".html"
                cmd = f"pandoc -s {rst_file_path} -o {html_file_path}"
                subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    target_directory = "/var/home/rafo/matplotlib"  #Directory
    rst_to_html(target_directory)
