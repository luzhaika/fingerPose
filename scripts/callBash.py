import subprocess

def call(str):
        print ("starting shell script")
        subprocess.call("./"+str+".sh")
        print ("end shell script")
