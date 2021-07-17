# -*- coding: utf-8 -*-
"""
@author: Tanya.Nayyar

"""
#%%Import the required libraries
import pysftp as psftp
import SFTP_Class as sc
#%%

sftp_hostname, sftp_username, sftp_password, my_private_key, my_private_key_pass = sc.General.get_username_password_key()

try:
    with psftp.Connection(host=sftp_hostname, username=sftp_username, password=sftp_password) as sftp:
    #Using an RSA or DSA key pair
    #Private key pass since key is password protected
    #with psftp.Connection(host=sftp_hostname, username=sftp_username, private_key=my_private_key, private_key_pass=my_private_key_pass) as sftp:    
        print("Connection succesfully established ... ")
        print(sftp.pwd)
        # Switch to a remote directory
        sftp.cwd('path to remote working directory')

        # Obtain structure of the remote directory
        directory_structure = sftp.listdir_attr()
        
        sc.General.list_files_in_directory(directory_structure)
        
        indicator = "download"
        
        local_file_path, remote_file_path = sc.General.get_remote_and_local_file_path(indicator)
        
        if indicator == "upload":
            print("uploading")
            #adding file to the local path
            #sftp.put(local_file_path, remote_file_path)
        else:
            print("downloading")
            sftp.get(remote_file_path, local_file_path)
        
        sc.General.list_files_in_directory(directory_structure)
    
# connection closed automatically at the end of the with-block
except Exception as e:
    print("Couldn't connect to sftp. Error: %s" % e)
