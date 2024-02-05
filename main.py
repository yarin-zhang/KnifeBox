import json
import os
import subprocess
import typer
import time
import ensurepip
from typing import Optional
from venv import EnvBuilder

app = typer.Typer()


def check_pip(env_dir: str):
    '''
    检查 pip 是否已经在虚拟环境中可用
    '''
    pip_path = os.path.join(env_dir, "bin", "pip")
    try:
        subprocess.check_output([pip_path, "--version"])
        return True
    except FileNotFoundError:
        return False


def setup_env(script_dir: str):
    '''
    创建虚拟环境并安装依赖
    '''
    env_dir = os.path.join(script_dir, ".venv")
    if not os.path.exists(env_dir):
        builder = EnvBuilder(with_pip=True)  # 让 venv 自动安装 pip
        builder.create(env_dir)

        # 检查 pip 是否可用
        pip_path = os.path.join(env_dir, "bin", "pip")
        while True:
            try:
                # 尝试运行 pip
                subprocess.run([pip_path, "--version"], check=True)
                break  # 如果成功，那么跳出循环
            except subprocess.CalledProcessError:
                # 如果失败，那么等待一段时间，然后再次尝试
                time.sleep(1)

        # 检查 requirements.txt 文件是否存在，如果存在则安装依赖
        requirements_file = os.path.join(script_dir, "requirements.txt")
        if os.path.exists(requirements_file):
            try:
                subprocess.run([pip_path, "install", "-r",
                               requirements_file], check=True)
            except subprocess.CalledProcessError as e:
                print(
                    f"Error installing dependencies for script {script_dir}: {e}")


@app.callback()
def startup_event():
    '''
    在应用启动时，读取脚本目录并安装必要的依赖
    '''
    script_dirs = [d for d in os.listdir(
        "./data") if os.path.isdir(os.path.join("./data", d))]

    # 为每个脚本目录创建虚拟环境并安装必要的依赖
    for script_dir in script_dirs:
        setup_env(os.path.join("./data", script_dir))

        # 创建 knife-config.json 文件
        config_file = os.path.join("./data", script_dir, "knife-config.json")
        if not os.path.exists(config_file):
            with open(config_file, "w") as f:
                json.dump({
                    "use_in_knifebox": True,
                    "use_in_knifehub": False,
                    "prebuild_on_startup": True,
                    "ignore_dependencies": False,
                    "check_sha_for_updates": True
                }, f)


@app.command()
def list_scripts():
    '''
    添加命令，让用户可以通过命令行来列出所有脚本
    '''
    # 读取 ./data 目录下的所有目录
    script_dirs = [d for d in os.listdir(
        "./data") if os.path.isdir(os.path.join("./data", d))]
    typer.echo(f"Scripts: {script_dirs}")


@app.command()
def run_script(script_name: str, script_input: Optional[str] = None):
    '''
    添加命令，让用户可以通过命令行来运行一个脚本
    '''

    # 运行脚本
    script_dir = os.path.join("./data", script_name)
    env_dir = os.path.join(script_dir, ".venv")
    command = [os.path.join(env_dir, "bin", "python"), "script.py"]
    if script_input:
        command.append(script_input)
    result = subprocess.run(command, capture_output=True, text=True)

    # 输出结果
    typer.echo(result.stdout)


if __name__ == "__main__":
    app()
