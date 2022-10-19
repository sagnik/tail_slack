A simple cli tool to `tail -n 1` a file and push the result to a slack webhook. Should be run as a daemon.

Run as:

```slack
nohup tail_slack  <your-file> <your-slack-webhook> &
```