A simple cli tool to `tail -n 1` a file and push the result to a slack webhook. Should be run as a daemon.

In the base directory, do `pip install -e .`

Run as:

```bash
nohup tail_slack  <your-file> <your-slack-webhook> &
```

You can also set the interval (in milliseconds) of your updates: 

```
nohup tail_slack  <your-file> <your-slack-webhook> --interval 5000 &
```
