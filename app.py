from flask import Flask
import requests
import manager.implementation.file_manager as file_manager
import view_data_interfaces.implementation.view_data_cli as view_data_cli
import view_data_interfaces.implementation.view_data_event_hub as view_data_event_hub
from connections import app_mode

cli = view_data_cli.Cli
event_hub_mode = view_data_event_hub.EventHub

api = Flask(__name__)

@api.route("/files/<path:path>", methods=["GET"])
def get_file(path):
    """Download a file."""
    if app_mode == 'cli':
        # r = requests.get(path, allow_redirects=True)
        file_manager.FileManager.process_data(path, cli)
    elif app_mode == 'event_hub':
        file_manager.FileManager.process_data(path, event_hub_mode)
    return  "File is Proccesing...", 201

@api.route("/test")
def get():
    return "okkkkkkkk", 201

if __name__ == "__main__":
    api.run(debug=True, port=8000)


