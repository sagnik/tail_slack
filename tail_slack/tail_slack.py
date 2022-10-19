import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, EVENT_TYPE_MODIFIED
from subprocess import Popen, PIPE
from slack_sdk.webhook import WebhookClient


class Watcher:
    def __init__(self, path, webhook_url):
        self.observer = Observer()
        self.path = path
        self.webhook = WebhookClient(webhook_url)

    def run(self):
        event_handler = Handler(webhook = self.webhook)
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
    def __init__(self, webhook):
        self.webhook = webhook

    @staticmethod
    def read_last_line(_file: str):
        p = Popen(['tail', '-1', _file], shell=False, stderr=PIPE, stdout=PIPE)
        res, err = p.communicate()
        if err:
            return err.decode()
        else:
            return res.decode()

    def on_any_event(self, event):
        if event.event_type == EVENT_TYPE_MODIFIED:
            response = self.webhook.send(f"[{time.asctime()}]: {self.read_last_line(event.src_path)}")
            if response.staus_code != 200:
                raise RuntimeError(response.body)

