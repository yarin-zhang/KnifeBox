import os
import subprocess
import typer
from typing import Optional

app = typer.Typer()

# 在应用启动时，读取脚本目录并安装必要的依赖
@app.callback()
def startup_event():
    script_dirs = [d for d in os.listdir("./data") if os.path.isdir(os.path.join("./data", d))]

    # 为每个脚本目录安装必要的依赖
    for script_dir in script_dirs:
        subprocess.run(["pip", "install", "-r", f"./data/{script_dir}/requirements.txt"])

# 添加命令，让用户可以通过命令行来列出所有脚本
@app.command()
def list_scripts():
    # 读取 ./data 目录下的所有目录
    script_dirs = [d for d in os.listdir("./data") if os.path.isdir(os.path.join("./data", d))]
    typer.echo(f"Scripts: {script_dirs}")

# 添加命令，让用户可以通过命令行来运行脚本
@app.command()
def run_script(script_name: str, script_input: Optional[str] = None):
    # 运行脚本
    command = ["python", f"./data/{script_name}/script.py"]
    if script_input:
        command.append(script_input)
    result = subprocess.run(command, capture_output=True, text=True)
    
    # 输出结果
    typer.echo(result.stdout)

if __name__ == "__main__":
    app()
