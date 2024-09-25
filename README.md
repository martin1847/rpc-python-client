

`krpc` Python Client.

## 安装依赖 
需要python > 3.6

env 激活

```bash
export VER=3
conda  安装 python3
```

```python
# 全局设置镜像 
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

pip install grpcio protobuf
```

## 测试

```bash
python test-krpc.py
```
