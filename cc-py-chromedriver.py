U
    ч�_l=  �                   @   s�  d dl Z d dlZ d dlmZ d dlZd dlmZ d dlZd dlZd dlZd dl	Z	e �
d� d dlZd dlZd dlmZ d dlmZ d dlmZ d dlmZ d d	lmZ d d
lmZ d dlmZ dZe�� Ze�ddg� e�de � ed�Zed�Z ed�Z!ed�Z"ed�Z#dZ$G dd� d�Z%dd� Z&dd� Z'dd� Z(dd� Z)d d!� Z*d"d#� Z+d$d%� Z,d&d'� Z-d(d)� Z.d*d+� Z/d,d-� Z0d.d/� Z1d0d1� Z2d2d3� Z3d4d5� Z4d6d7� Z5e'�  dS )8�    N)�Path)�sleepzpip install -r requirements.txt)�	webdriver)�WebDriverWait)�expected_conditions)�TimeoutException)�By)�NoSuchElementException)�Fernetz	1920,1080ZexcludeSwitcheszenable-loggingz--window-size=%s�driver/chromedriverzconfig/config.txt�driver�.secret.key�configi   c                   @   s0   e Zd ZdZdZdZdZdZdZdZ	dZ
d	Zd
S )�bcolorsz[95mz[94mz[96mz[92mz[93mz[91mz[0mz[1mz[4mN)�__name__�
__module__�__qualname__ZHEADER�OKBLUE�OKCYAN�OKGREEN�WARNING�FAIL�ENDCZBOLDZ	UNDERLINE� r   r   �cc-py-chromedriver.pyr   6   s   r   c                 C   sJ   | r>t | d�\}}d�||�}t|dd� t�d� | d8 } q td� d S )N�<   z{:02d}:{:02d}�)�end�   zAThe time has expired! For security reasons we closed the webpage!)�divmod�format�print�timer   )�time_to_runZminsZsecsZtimerr   r   r   �	CountdownF   s    

r$   c                  C   s6  t �d� td� tt�d�� d} t j�t�rFttj	d tj
 � n2ttjd tj
 � t �d� ttjd tj
 � t�� r�ttj	d	 tj
 � n0| d
 } ttjd tj
 � ttjd tj
 � t j�t�r�ttj	d tj
 � n2ttjd tj
 � t �d� ttjd tj
 � t�� �r:ttj	d tj
 � n:ttjd tj
 � ttd�}|��  ttjd tj
 � t�� �r�ttj	d tj
 � n.ttjd tj
 � t�  ttjd tj
 � | d
k�r�ttjd tj
 � t��  nttj	d tj
 � td� tdd� tt�D ��}tdt|� d � td� ttjd tj
 tj d  tj
 � td!�}|d"k�sx|d#k�r�t�  n�|d$k�s�|d%k�r�t�  n�|d&k�s�|d'k�r�t�  nt|d(k�s�|d)k�r�t �  nX|d*k�s�|d+k�r�t!�  n<|d,k�s|d-k�rt��  nt �d� ttjd. tj
 � t"�  d S )/N�clear�
Written by�n1c0t1n3r   z
driver folder -- goodzdriver folder -- not foundr   zcreated 'driver' folderzchromedriver -- goodr   zchromedriver -- not foundz6Download chromedriver and place it in 'driver' folder!zconfig folder -- goodzconfig folder -- not foundr   zcreated 'config' folderzconfig file -- goodzconfig file -- not found�w+zcreated 'config' filezsecret key -- goodzsecret key -- not foundzcreated '.secret.key' filezu
Critical error! Some files are missing/not found. Please get the files, put them in the right folder and try again!
z!
GOOD! No missing files/folders!
�
++++++++++++++++++++
c                 s   s   | ]
}d V  qdS �r   Nr   ��.0�liner   r   r   �	<genexpr>�   s     zFile_Checker.<locals>.<genexpr>�Your config file contains �	 accounts�
What do you want to do?��

(1) n = add new account to the list
(2) d = delete an account from the list
(3) c = connect to an account from the list
(4) cnc = connect to an account outside the list
(5) v = view all your accounts
(6) q = quit�n/d/c/cnc/v/q: �n�1�d�2�c�3�cnc�4�v�5�q�6�
Unknown command! Try again!)#�os�systemr!   �pyfiglet�figlet_format�path�exists�driver_folderr   r   r   r   �makedirsr   �chromedriver_path�is_file�config_folder�config_file_path�open�close�secret_key_path�generate_key�sys�exit�sum�strr   r   �input�Add_Account�Delete_Account�CC�CC_no_credits�Viewer�	Main_Menu)�error�f�config_file_lines�choicer   r   r   �File_CheckerR   sn    







$

r`   c               	   C   s,   t �� } tdd��}|�| � W 5 Q R X d S )Nr   �wb)r
   rP   rM   �write)�keyZkey_filer   r   r   rP   �   s    rP   c                   C   s   t dd��� S )Nr   �rb)rM   �readr   r   r   r   �load_key�   s    rf   c                 C   sL   t � }| �� }t|�}|�|�}ttd�}|�|� |��  t�  t	�  d S )NZab)
rf   �encoder
   ZencryptrM   �	file_namerb   rN   �Succes�Return_To_Main_Menu)�messagerc   Zencoded_messager]   �encrypted_messager   r   r   �encrypt_message�   s    


rm   c                 C   s$   t � }t|�}|�| �}|�� ad S �N)rf   r
   Zdecrypt�decode�account_to_connect_pass)rl   rc   r]   Zdecrypted_messager   r   r   �decrypt_message�   s    
rq   c                  C   s0   t tjd tj �} | dkr$t�  nt��  d S )Nz(
Return to main menu? y = yes // n = no �y)rU   r   r   r   r[   rQ   rR   �r_   r   r   r   rj   �   s    rj   c                  C   s@   t tjd tj �} | dkr$t�  n| dkr4t�  nt��  d S )Nz9
Return to main menu? y = yes // n = no // t = try again rr   �t)rU   r   r   r   r[   rX   rQ   rR   rs   r   r   r   � Return_To_Main_Menu_Or_Try_Again�   s    ru   c                  C   s:  t �d� td� tt�d�� td� tdd� tt�D ��} tdt| � d � td� tt	j
d	 t	j t	j d
 t	j � td�}|dks�|dkr�t�  n�|dks�|dkr�t�  nz|dks�|dkr�t�  nb|dks�|dkr�t�  nJ|dks�|dkr�t�  n2|dk�s|dk�rt��  ntt	jd t	j � t�  d S )Nr%   r&   r'   r)   c                 s   s   | ]
}d V  qdS r*   r   r+   r   r   r   r.   �   s     zMain_Menu.<locals>.<genexpr>r/   r0   r1   r2   r3   r4   r5   r6   r7   r8   r9   r:   r;   r<   r=   r>   r?   r@   )rA   rB   r!   rC   rD   rS   rM   rL   rT   r   r   r   r   rU   rV   rW   rX   rY   rZ   rQ   rR   r   r[   )r^   r_   r   r   r   r[   �   s.    
$
r[   c                  C   s,   t t�} | D ]}t|� q| ��  t�  d S rn   )rM   rL   r!   rN   rj   )r]   r-   r   r   r   rZ   �   s
    
rZ   c                  C   sp   t d�} t d�}t d�}d|  d attd�}|�|d � |��  ttd�}|�| d	 � |��  t|� tS )
N�Account name: zAccount email: zAccount password: �config/.�.txtr(   �:�a�
)rU   rh   rM   rb   rN   rL   rm   )Zaccount_nameZaccount_emailZaccount_passwordr]   r   r   r   rV     s    

rV   c                   C   s   t tjd tj � d S )NzCommand completed succesfully)r!   r   r   r   r   r   r   r   ri     s    ri   c                  C   s|  �zHd} t �  tjtdd�}|�d� t|| ��t�t	j
df��}td� |�d��t� |�d��t� |�d���  td	� |�d
�j}|dkr�ttjd t d tj � |�d�j}|dkr�ttjd t d tj � t�  n`|dk�rttjd t d tj � t�  n2ttjd tj � tt� td� |��  W dS W n, tk
�rv   td� |��  t�  Y nX d S )N�
   r   ��optionsZexecutable_path�https://mega.nz/login�login-name2�Page is ready!�login-password2�//*[@id="login_form"]/div[6]r   �#//*[@id="login_form"]/div[2]/div[2]�#Please enter a valid email address.�"
Invalid email adress for account � !�%//*[@id="msgDialog"]/div[2]/div[2]/h1��This account has not completed the registration process yet. First check your email, click on the Activate Account button and reconfirm your chosen password.�.
Please complete the registration for account � then try again!�0Invalid email and/or password. Please try again.�+
Invalid email and/or password for account �. Please try againzSuccesfully connected!�#  r   �	Timed out)�Get_Account_Datar   �Chromer~   �getr   �until�EC�presence_of_element_locatedr   �IDr!   �find_element_by_id�	send_keys�account_to_connect_emailrp   �find_element_by_xpath�clickr   �textr   r   �account_to_connectr   rj   r   r$   r#   �quitr   ru   )�delayr   ZmyElem�check_email�checkr   r   r   rX     s<    


rX   c                  C   s�  d} t d�}t d�}�z>tjtdd�}|�d� t|| ��t�t	j
df�� td� |�d��|� |�d	��|� |�d
���  td� |�d�j}|dkr�ttjd | d tj � |�d�j}|dkr�ttjd | d tj � t�  n`|dk�r ttjd | d tj � t�  n2ttjd tj � tt� td� |��  W dS W n, tk
�r�   td� |��  t�  Y nX d S )Nr|   zAccount's email: zAccount's password: r   r}   r   r�   r�   r�   r�   r   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   zSuccesfully connected!
r�   r   r�   )rU   r   r�   r~   r�   r   r�   r�   r�   r   r�   r!   r�   r�   r�   r�   r   r�   r   r   r   rj   r   r$   r#   r�   r   ru   )r�   ZemailZpasswordr   r�   r�   r   r   r   rY   F  s>    


rY   c               	   C   s  t d�} d|  d }tt|��}|�� r�ttjd tj � t�	|� t
tt�d��}|�� }W 5 Q R X t
tt�d��(}|D ]}|�d�| kr||�|� q|W 5 Q R X t�  t�  ndttjd tj � t d	�}|d
kr�t�  n8|dkr�t�  n(|dk�rt��  nttjd tj � d S )Nz%Which account do you want to delete? rw   rx   ZDeleted�r�wr{   zNo account foundzYTry again deleting the account?
y = yes // n = no (Take me to the main menu) // q = quit r4   rr   r>   r@   )rU   r   rT   rJ   r!   r   r   r   rA   �removerM   rL   �	readlines�striprb   ri   rj   r   r[   rW   rQ   rR   )Zaccount_to_delZaccount_to_del_file_nameZaccount_to_del_pathr]   �linesr-   r_   r   r   r   rW   q  s.    


rW   c               	   C   s�   t d�adt d } t| �}|�� r�t|d��X}|�� �� }|�d�d at	dt � |�d�d }t	d	| � t
|d
�}t|� W 5 Q R X nbt	tjd tj � t d�}|dkr�t�  n6|dkr�t�  n&|dkr�t��  nt	tjd tj � d S )Nrv   rw   rx   r�   ry   r   zEmail: r   zPass: zutf-8z
No account foundzDTry again?
y = yes // n = no (Take me to the main menu) // q = quit r4   rr   r>   r@   )rU   r�   r   rJ   rM   �readliner�   �splitr�   r!   �bytesrq   r   r   r   r[   rX   rQ   rR   )Zfile_sZ	file_pathr]   Z
first_lineZaccount_to_connect_enc_passZaccount_to_connect_enc_pass_br_   r   r   r   r�   �  s*    

r�   )6rA   �os.path�pathlibr   r"   r   rQ   �
subprocessZpkg_resources�	linecacherB   rC   Zseleniumr   Zselenium.webdriver.support.uir   Zselenium.webdriver.supportr   r�   Zselenium.common.exceptionsr   Zselenium.webdriver.common.byr   r	   Zcryptography.fernetr
   ZWINDOW_SIZEZChromeOptionsr~   Zadd_experimental_option�add_argumentrI   rL   rG   rO   rK   r#   r   r$   r`   rP   rf   rm   rq   rj   ru   r[   rZ   rV   ri   rX   rY   rW   r�   r   r   r   r   �<module>   s\   
R
		++ 