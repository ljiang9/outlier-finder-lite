"""命令行：python3 cli.py 1,2,3,4,100,2,3"""
import argparse
import json

from outlier import find


def main(argv=None):
    p = argparse.ArgumentParser(description="outlier-finder-lite 异常检测")
    p.add_argument("series", help="逗号分隔数值")
    args = p.parse_args(argv)
    series = [float(x) for x in args.series.split(",") if x.strip()]
    print(json.dumps(find(series), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
