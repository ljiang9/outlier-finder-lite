# outlier-finder-lite

异常检测小工具。z-score / IQR / MAD 三种方法标记异常点。零第三方依赖。

## 功能

- **z-score**：|x-μ|/σ 超阈值；
- **IQR**：超出 Q1/Q3 ± 1.5·IQR；
- **MAD**：中位数绝对偏差稳健检测。

## 快速开始

```bash
python3 cli.py 1,2,3,4,100,2,3
```

## 无 API Key 如何运行

本工具**完全不需要 API Key**。

## 目录结构

```
outlier-finder-lite/
├── outlier.py    # z-score / IQR / MAD
├── cli.py
├── tests/test_outlier.py
├── README.md / LICENSE / .gitignore
```

## 测试

```bash
python3 -m unittest discover -s tests
```

## 许可证

[MIT](./LICENSE)
