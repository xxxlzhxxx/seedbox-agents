# SeedBox Agents

角色行动的最小参考实现。walk.py 使用广度优先搜索，返回经过连接数最少的步行路线。运行环境为 Python 3.8 及以上，仅使用标准库。

在两个子仓的上级目录运行：

```sh
python3 seedbox-agents/walk.py seedbox-worlds/plaza.json entrance bookshop
```

输出为 `入口 → 喷泉 → 书店`。起点或终点未知、终点不可达时，命令返回非零退出码。世界格式见 [seedbox-worlds](../../../seedbox-worlds)。
