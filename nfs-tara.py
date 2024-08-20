import os
import subprocess
from tabulate import tabulate

ip_list_file = 'ip_list.txt'
output_file = 'nfs_scan_results.txt'


with open(output_file, 'w') as f:
    f.write("NFS Scan Results\n")
    f.write("================\n\n")

writeable_shares = []
readable_shares = []

def check_nfs_share(ip):
    try:
        shares = subprocess.check_output(['showmount', '-e', ip]).decode().strip().split('\n')
        
        if len(shares) > 1:
            shares = shares[1:]  # İlk satırı atla çünkü başlık satırı
            print(f"\n[INFO] {ip} üzerinde bulunan NFS paylaşımları:")
            with open(output_file, 'a') as f:
                f.write(f"\nIP: {ip}\n")
                f.write("Paylaşımlar:\n")
                
                for share in shares:
                    share_path = share.split()[0]
                  
                    mount_point = f"/mnt/nfs_temp"
                    os.makedirs(mount_point, exist_ok=True)
                    
                    try:
                        subprocess.check_call(['mount', f"{ip}:{share_path}", mount_point], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        
                        
                        read_test = os.access(mount_point, os.R_OK)
                       
                        write_test = os.access(mount_point, os.W_OK)
                        
                        if write_test:
                            writeable_shares.append([ip, share_path])
                        if read_test:
                            readable_shares.append([ip, share_path])
                        
                     
                        with open(output_file, 'a') as f:
                            print(f"\n[INFO] {share_path} dizininin içeriği ({'OKUMA' if read_test else 'YAZMA'} yetkisi):")
                            f.write(f"\n[INFO] {share_path} dizininin içeriği ({'OKUMA' if read_test else 'YAZMA'} yetkisi):\n")
                            
                            for root, dirs, files in os.walk(mount_point):
                                level = root.replace(mount_point, '').count(os.sep)
                                indent = ' ' * 4 * (level)
                                f.write(f"{indent}{os.path.basename(root)}/\n")
                                sub_indent = ' ' * 4 * (level + 1)
                                for d in dirs:
                                    f.write(f"{sub_indent}{d}/\n")
                                for f_name in files:
                                    f.write(f"{sub_indent}{f_name}\n")
                    
                    except subprocess.CalledProcessError:
                        print(f"    [ERROR] {share_path} mount edilemedi.")
                        with open(output_file, 'a') as f:
                            f.write(f"    [ERROR] {share_path} mount edilemedi.\n")
                    
                    finally:
                       
                        subprocess.call(['umount', mount_point])
                        os.rmdir(mount_point)
        else:
            print(f"[INFO] {ip} üzerinde herhangi bir NFS paylaşımı bulunamadı.")
            with open(output_file, 'a') as f:
                f.write(f"[INFO] {ip} üzerinde herhangi bir NFS paylaşımı bulunamadı.\n")
    
    except subprocess.CalledProcessError:
        print(f"[ERROR] {ip} adresine bağlanılamadı veya NFS paylaşımı bulunamadı.")
        with open(output_file, 'a') as f:
            f.write(f"[ERROR] {ip} adresine bağlanılamadı veya NFS paylaşımı bulunamadı.\n")


with open(ip_list_file, 'r') as file:
    for ip in file:
        ip = ip.strip()
        if ip:
            print(f"\n[SCAN] {ip} üzerinde NFS taraması başlatılıyor...")
            check_nfs_share(ip)


if writeable_shares:
    print("\n[INFO] Yazma yetkisi olan NFS paylaşımları:")
    print(tabulate(writeable_shares, headers=["IP Adresi", "Paylaşım Dizini"]))
    with open(output_file, 'a') as f:
        f.write("\nYazma yetkisi olan NFS paylaşımları:\n")
        f.write(tabulate(writeable_shares, headers=["IP Adresi", "Paylaşım Dizini"]))
        f.write("\n")

if readable_shares:
    print("\n[INFO] Okuma yetkisi olan NFS paylaşımları:")
    print(tabulate(readable_shares, headers=["IP Adresi", "Paylaşım Dizini"]))
    with open(output_file, 'a') as f:
        f.write("\nOkuma yetkisi olan NFS paylaşımları:\n")
        f.write(tabulate(readable_shares, headers=["IP Adresi", "Paylaşım Dizini"]))
        f.write("\n")

print("\n[INFO] NFS tarama işlemi tamamlandı.")
