# -*- coding: utf-8 -*-
"""
@author: Tanya.Nayyar

"""
#%%
class General:
    
    def get_username_password_key():
        """
        Get remote server's fully qualified domain qualified name (FQDN : hostname), username, password, path
        to the local private key file, and the private key password if the 
        key is password protected
        Parameters
        ----------
        None
        Returns
        -------
        my_hostname : str
            SFTP server's fully qualified domain name.
        my_username : str
            SFTP server's username.
        my_password : str
            SFTP server's password.
        my_private_key : str
            Local file path to the private key.
        my_private_key_pass : str
            Password if the private key is password protected.
        
        """
        my_hostname = "enter the hostname"
        my_username = "enter the username"
        my_password = "enter the password"
        my_private_key = 'enter path to the private key'
        my_private_key_pass = 'enter the private key password'
        return my_hostname, my_username, my_password, my_private_key, my_private_key_pass
    
    def get_remote_and_local_file_path(indicator):
        """
        Get the local file path depending upon the indicator parameter and 
        the remote file path from where the file needs to be retrieved or where 
        it needs to be stored
        
        Parameters
        ----------
        indicator : str
            Variable indicating an upload or download
            
        Returns
        -------
        local_file_path : str
            Local path to the file or for the file.
        remote_file_path : str
            Remote path to the file or for the file.
        
        """
        if indicator == "upload":
            #Define local path where file will be downloaded to or from where it will be uploaded
            local_file_path = 'local file path'
        else:
            local_file_path = 'local file path'
            # Define the remote path where file will be uploaded or from file will be downloaded
            remote_file_path = 'remote file path'
            
        return(local_file_path, remote_file_path)
    
    def list_files_in_directory(directory_structure):
        """
        Print the files in the list of SFTPAttribute objects 
        of the files/directories for the given remote path.
        
        Parameters
        ----------
        directory_structure : (list of SFTPAttributes)
            List of SFTPAttribute objects of the files/directories for the given remote path.
           
        Returns
        -------
        None
        
        """
        # Print data inside the directory
        for attr in directory_structure:
            print(attr.filename, attr)
