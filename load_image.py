# coding:utf-8
import subprocess, os
def get_filename():
    with open("images.txt", "r") as f:
        lines = f.read().split('\n')
        # print(lines)
        return lines



def pull_image():
    name_list= get_filename()
    for name in name_list:
        new_name = "kenwood/" + name.split("/")[-1]
        subprocess.call("docker pull {}".format(new_name), shell=True)
        subprocess.run(["docker", "tag", new_name, name])
        subprocess.call("docker rmi  {}".format(new_name), shell= True)
if __name__ == "__main__":
    pull_image()
