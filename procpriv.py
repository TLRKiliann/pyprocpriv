#!/usr/bin/python3
# -*- encoding:Utf-8 -*-

__SIMPLE__="""
################################################

	Simple syscall to display process,
	uid, gid, group, etc...

################################################
"""


import os
# from pwd import getpwnam (python2)


print(__SIMPLE__)

dispid = os.getpid()
print("+ PID : ", dispid)

disppid = os.getppid()
print("\n+ PPID : ", disppid)

disenvname = os.environ.get('USER')
print("\n+ Username environ :", disenvname)
print("+ Real group id (gid) :", os.getgid())
print("+ Effective user id (euid) :", os.geteuid())
print("+ Effective group id (egid) :", os.getegid())
print("+ List of supplemental group ids :", os.getgroups())

print("\n+ Command 'id' on linux with bash --> echo $(id)")
os.system("echo $(id)")
print("\n+ Command 'id' on linux with python3 --> id")
os.system("id")

discwd = os.getcwd()
print("\n+ CWD :", discwd)

print("\n+ PATH (with bash) :")
os.system("echo $PATH")

disenv = os.environ
print("\n+ Environ :", disenv)

print("\n+ You can also use evironb to switch in binary --> os.environb")
