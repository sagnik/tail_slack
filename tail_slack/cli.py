import argparse
from .tail_slack import Watcher


if __name__ == "__main__":
    parser = argparse.ArgumentParser("tail file and send to slack")
    parser.add_argument("--file_to_tail", required=True)
    parser.add_argument("--slack_webhook", required=True)
    args = parser.parse_args()
    w = Watcher(args.file_to_tail, args.slack_webhook)
    w.run()