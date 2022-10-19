import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from subprocess import Popen, PIPE
from slack_sdk.webhook import WebhookClient


class Watcher:
    def __init__(self, path, webhook_url, interval):
        self.observer = Observer()
        self.path = path
        self.webhook = WebhookClient(webhook_url)
        self.interval = interval / 1000

    def run(self):
        event_handler = Handler(webhook=self.webhook, interval=self.interval)
        self.observer.schedule(event_handler, self.path, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):
    def __init__(self, webhook, interval):
        self.webhook = webhook
        self.interval = interval
        self.last_event_time = time.time()
        self.current_event_time = time.time()

    @staticmethod
    def read_last_line(_file: str):
        p = Popen(['tail', '-1', _file], shell=False, stderr=PIPE, stdout=PIPE)
        res, err = p.communicate()
        if err:
            return err.decode()
        else:
            return res.decode()

    def on_modified(self, event):
        self.current_event_time = time.time()
        if self.current_event_time - self.last_event_time > self.interval:
            _con = self.read_last_line(event.src_path)
            response = self.webhook.send(text=_con)
            if response.status_code != 200:
                raise RuntimeError(response.body)
            self.last_event_time = self.current_event_time
            

