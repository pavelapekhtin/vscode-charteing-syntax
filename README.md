# Chartering Syntax Highlighting for VS Code

## Description

This VS Code extension provides syntax highlighting for important keywords in dry cargo fixture recaps. It aims to make it easier to read and understand chartering documents by highlighting key terms, numbers, and phrases.

## Features

* Highlights numerical values with optional prefixes and suffixes.
* Highlights quoted strings and specific chartering terms.
* Highlights parameters related to money, costs, and payments.
* Highlights read/write variables related to voyage details.
* Highlights storage-related terms like account, shipper, and receiver.
* Highlights class types and entities related to responsibilities and options.

## Installation

1. Install Node.js and npm if you haven't already.
2. Install vsce package by running npm install -g vsce.
3. Navigate to your extension's directory and run vsce package to package your extension into a .vsix file.
4. Install the .vsix file in VS Code using the "Install from VSIX..." option in the Extensions view command drop-down.

## Usage

Open a file with the .txt or .recap extension.
The extension should automatically apply the syntax highlighting based on the file extension.
Supported File Extensions
`.txt`
`.recap`

## Configuration

The language configuration supports line comments with // and block comments with /* */. It also supports auto-closing and surrounding pairs for {}, [], and ().

## Contributing

Feel free to open issues or pull requests if you have suggestions for improvement.

## Version

0.1.0
