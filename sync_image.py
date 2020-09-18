# coding:utf-8
import subprocess, os
def get_filename():
    with open("images.txt", "r") as f:
        lines = f.readlines()
        # print(lines)
        return lines

# def rename():
#     name_list= get_filename()
#     for name in name_list:
#         new_name = "kenwood/" + name.split("/")[-1]
#         print(new_name)


def pull_image():
    name_list= get_filename()
    for name in name_list:
        new_name = "kenwood/" + name.split("/")[-1]
        cmd = "docker tag {0}   {1}".format(name, new_name)
        subprocess.call("docker pull {}".format(name), shell=True)
        subprocess.run(["docker", "tag", name, new_name])
        subprocess.call("docker login -u kenwood -p qwer1234", shell=True)
        subprocess.call("docker push {}".format(new_name), shell=True)
        
if __name__ == "__main__":
    pull_image()
