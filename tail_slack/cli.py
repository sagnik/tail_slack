import argparse
from .tail_slack import Watcher


def main():
    parser = argparse.ArgumentParser("tail file and send to slack")
    parser.add_argument("file_to_tail")
    parser.add_argument("slack_webhook")
    parser.add_argument("--interval", default=1, help="interval in milli seconds", type=int)
    args = parser.parse_args()
    w = Watcher(args.file_to_tail, args.slack_webhook, args.interval)
    w.run()


if __name__ == "__main__":
    main()
