# Duplicate Finder Anki Addon

Anki addon that will find if there are duplicates cards in specified deck, based on current Reviewing Card.

When reviewing cards, specially new ones, you might feel like you've already had a card for that word or expression in another deck that that you are not using anymore.

# How to use

While reviewing a card and you press the shortcut, this addon will look in the designated decks for any exact match of current card being reviewed and report the results, adding a custom tag to the duplicate card, makign it easy to find it in the browser later on for reference.

# Info

## Environment

- Python 3.8.10

This are the main packages that are being used:

- anki 2.1.49
- aqt 2.1.49

## Supported Anki Version

This addon was made and tested on this version of Anki:

- Version 2.1.54 (b6a7760c)
- Python 3.9.7 Qt 5.15.2 PyQt 5.15.5

# How to Install

- Download the zip file in the newest version from the [Release Page](https://github.com/bernardobt/anki-duplicate-finder-addon/releases)

- <img alt="Release">

- Open the Addons menu:

  - Use the Ctrl + Shift + A Shortcut
  - In Anki's menu, go to Tools -> Add-ons
    <img src="docs\AddonMenuFromToolbar.png" alt="Addon menu from toolbar">

- In the Add-ons menu, click on "View Files" to open Anki's Add-on folder:
  <img src="docs\ViewFiles.png" alt="Addon menu from toolbar">

- Extract the downloaded zip file into Anki's Add-on folder
  <img src="docs\Installed.png" alt="Addon Menu">

- Reopen the Add-on Menu so it updates the addon list, select 'duplicate-finder' and click on Config
  <img src="docs\Config.png" alt="Addon Menu">

- Edit the appropriate variables acording to instructions to fit your needs.

- Restart Anki

# Current State

- Simple Version of the Addon, without GUI. Config must be done Manually inside anki addon config file.

## To Do

- Basic GUI to make config easier
- Progress bar to show searching progress
