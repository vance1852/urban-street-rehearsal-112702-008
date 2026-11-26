# 多角色调度脚本的虚拟时间联调与重演

临时通行协作的合成排练脚本与历史动作记录。脚本只作用于本地虚拟角色。

数据约定见 [资料协议](protocol.md)。项目资料使用 Python 3.11 标准库读取，无需安装依赖。仓库保留的是资料和接口约定。

在项目根目录运行 `python3 inspect_inputs.py` 查看资料并检查文件关联，运行 `python3 -m unittest discover -s tests -v` 核验资料的格式和完整性。
