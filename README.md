How to install FSharp language server for Sublime Text 3
N.B. ST3 does not support LSP as well as vscode, so it's a bit clumsy. This is also currently win-x64 only.
1. Install Package Control
2. Run command "Package Control: install Package" to install "LSP"
3. Run command "Package Control: Add repository" to add "https://raw.githubusercontent.com/tboby/fsharp-language-server-sublime/master/packages.json"
5. Run command "Package Control: Install Package" to install "LSP_fsharp"
6. Close and re-open Sublime Text
7. Open your project folder, then open an F# file
8. If it doesn't happen automatically, change the language to "F#".
9. (recommended) Run command "Preferences: LSP Settings" and add:
   "log_stderr": true,
    "only_show_lsp_completions": true,
    "resolve_completion_for_snippets": true,
    "show_diagnostics_phantoms": true,
     "show_diagnostics_count_in_view_status": true

F# settings
To change settings run the command "Preferences: LSP_fsharp Settings"
