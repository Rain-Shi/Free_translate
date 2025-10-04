"""
安装pandoc的辅助脚本
在Windows系统上自动下载并安装pandoc
"""
import os
import sys
import urllib.request
import zipfile
import subprocess

def download_and_install_pandoc():
    """下载并安装pandoc"""
    print("正在下载pandoc...")
    
    # pandoc下载URL
    pandoc_url = "https://github.com/jgm/pandoc/releases/download/2.19.2/pandoc-2.19.2-windows-x86_64.zip"
    
    # 下载文件
    try:
        urllib.request.urlretrieve(pandoc_url, "pandoc.zip")
        print("下载完成")
        
        # 解压文件
        with zipfile.ZipFile("pandoc.zip", 'r') as zip_ref:
            zip_ref.extractall("pandoc_temp")
        
        # 移动pandoc.exe到系统路径
        pandoc_exe = "pandoc_temp/pandoc-2.19.2/pandoc.exe"
        if os.path.exists(pandoc_exe):
            # 创建pandoc目录
            pandoc_dir = os.path.join(os.environ['USERPROFILE'], 'pandoc')
            os.makedirs(pandoc_dir, exist_ok=True)
            
            # 复制文件
            import shutil
            shutil.copy2(pandoc_exe, pandoc_dir)
            
            # 添加到PATH
            current_path = os.environ.get('PATH', '')
            if pandoc_dir not in current_path:
                os.environ['PATH'] = current_path + ';' + pandoc_dir
            
            print(f"pandoc已安装到: {pandoc_dir}")
            print("请重启命令行或IDE以使PATH生效")
            
        # 清理临时文件
        os.remove("pandoc.zip")
        import shutil
        shutil.rmtree("pandoc_temp")
        
    except Exception as e:
        print(f"安装失败: {e}")
        print("请手动下载并安装pandoc: https://pandoc.org/installing.html")

if __name__ == "__main__":
    download_and_install_pandoc()
