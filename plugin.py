import os

import shutil

import sublime_plugin

import sublime

from LSP.plugin.core.handlers import LanguageHandler

from LSP.plugin.core.settings import ClientConfig

from LSP.plugin.core.protocol import Request, Point

from LSP.plugin.references import ensure_references_panel

from LSP.plugin.core.documents import is_at_word, get_position, get_document_position

from LSP.plugin.core.workspace import get_project_path

from LSP.plugin.core.url import uri_to_filename

from os.path import dirname


default_cwtools_settings = {

}

config_name = 'fsharp'

server_name = 'fsharp'

def get_fsharp_config():
    s = sublime.load_settings("LSP-fsharp.sublime-settings").get('settings', default_cwtools_settings)
    return ClientConfig(

        name=config_name,

        binary_args=[

            dirname(__file__) + '/win-x64/FSharpLanguageServer.exe'

        ],

        tcp_port=None,

        scopes=['source.fsharp'],

        syntaxes=[

        ],

        languageId='F#',

        enabled=True,

        init_options=dict(),

        settings=s,

        env=dict())


class LspCwtoolsPlugin(LanguageHandler):
    def __init__(self):
        self._name = config_name
        self._config = get_fsharp_config()

    @property
    def name(self) -> str:
        return self._name

    @property
    def config(self) -> ClientConfig:
        return self._config

    def on_start(self, window) -> bool:
        print("on start")
        return True

    def on_initialized(self, client) -> None:
        print("on initialized")
        register_client(client)


def register_client(client):
    print("register loadingBar")
    client.on_notification(
        "loadingBar",
        lambda params: on_loading_bar(params))

def on_loading_bar(params):
    print("loadingBar")
    if(params["enable"]):
        sublime.status_message(params["value"])
    else:
        sublime.status_message("")
