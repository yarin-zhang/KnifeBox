# KnifeBox

KnifeBox 中的 Knife 取自“瑞士军刀”（Swiss Army Knife）的意思，KnifeBox 允许你收纳你的小工具，可以自由集成可用的 Python 代码的工具库。

这样就能够将自己所需的 Python 代码片段整合到一个地方，并允许通过命令行请求调用。

## 创建一个 KnifeBox 的小工具

以下是创建一个 KnifeBox 的小工具的步骤：

1. **创建脚本目录**：在 `./data` 目录下创建一个新的目录，目录的名称将作为你的脚本的名称。例如，你可以创建一个名为 `pangu_spacing` 的目录。

2. **编写脚本**：在你的脚本目录中创建一个名为 `script.py` 的 Python 脚本。你的脚本应该从命令行参数中接收输入，并通过 `print` 函数输出结果。例如，你可以创建一个使用 `pangu.spacing_text` 函数来添加空格的脚本。

    ```python
    import sys
    import pangu

    def main(input_text):
        spaced_text = pangu.spacing_text(input_text)
        print(spaced_text)

    if __name__ == "__main__":
        input_text = sys.argv[1]
        main(input_text)
    ```

3. **列出依赖**：在你的脚本目录中创建一个名为 `requirements.txt` 的文件，列出你的脚本的依赖。例如，如果你的脚本使用了 `pangu` 模块，那么你的 `requirements.txt` 文件应该包含一行 `pangu`。

## 运行 KnifeBox

你可以通过以下命令在命令行中运行 KnifeBox：

```
python main.py
```

## 使用 KnifeBox

你可以通过命令行来列出所有可用的脚本：

```
python main.py list-scripts
```

你也可以通过命令行来运行一个脚本：

```
python main.py run-script script_name --script-input script_input
```

请注意，`script_name` 应该替换为你的脚本的名称，`--script-input` 参数的值是你想要传递给你的脚本的输入。

## 与 KnifeHub 的区别

与 KnifeHub 不同，KnifeBox 是一个命令行应用，而不是一个 Web 服务器。这意味着你不能通过 HTTP 请求来调用你的脚本，而是需要在命令行中直接运行它们。

然而，KnifeBox 和 KnifeHub 有很多相似之处。它们都允许你收纳你的小工具，并且它们都使用一个类似的目录结构来组织你的脚本。此外，它们都在启动时自动安装你的脚本的依赖。