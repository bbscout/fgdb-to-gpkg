# FGDB to GPKG Converter Plugin (QGIS)

<p align="center">
  <a href="./README_cs.md">Česky</a> |
  <a href="./README.md">English</a>
</p>

---

## Description

This QGIS plugin allows easy conversion of layers from File Geodatabase (FGDB) format to GeoPackage (GPKG) format.

## Installation

To install the plugin, follow these steps:

1. Download the source code of the plugin from the GitHub repository as a ZIP file.
2. Extract the ZIP file to the QGIS plugin folder located here:
   - Windows: `C:\Users\USERNAME\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins`
   - macOS: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins`
   - Linux: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins`
3. Restart QGIS, if it is currently running.
4. In QGIS, open the `Plugins > Plugin Manager` dialog.
5. In the list of plugins, find `FGDB to GPKG Converter` and check the box to activate it.

The plugin is now installed and activated in QGIS. You can find it in the Processing Toolbox panel under the `FGDB to GPKG` category.

## Usage

1. Open the Processing Toolbox panel and expand the `FGDB to GPKG` category.
2. Run the `Convert FGDB to GPKG` algorithm.
3. Choose the input File Geodatabase (.gdb) and output GeoPackage (.gpkg).
4. Click `Run`.

## Authorship

This plugin was entirely written by the AI language model ChatGPT from OpenAI. 

---

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Release](https://img.shields.io/github/release/bbscout/fgdb-to-gpkg.svg)](https://github.com/bbscout/fgdb-to-gpkg/releases)
[![GitHub Issues](https://img.shields.io/github/issues/bbscout/fgdb-to-gpkg.svg)](https://github.com/bbscout/fgdb-to-gpkg/issues)
