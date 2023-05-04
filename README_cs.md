# Plugin pro konverzi FGDB do GPKG (pro QGIS)

<p align="center">
  <a href="./README_cs.md">Česky</a> |
  <a href="./README.md">English</a>
</p>

---

## Popis

Tento plugin pro QGIS umožňuje snadnou konverzi vrstev z formátu File Geodatabase (FGDB) do formátu GeoPackage (GPKG).

## Instalace

Pro instalaci pluginu postupujte následovně:

1. Stáhněte zdrojový kód pluginu z repozitáře na GitHubu jako ZIP soubor.
2. Rozbalte ZIP soubor do složky s pluginy QGIS, která se nachází zde:
   - Windows: `C:\Users\USERNAME\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins`
   - macOS: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins`
   - Linux: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins`
3. Restartujte QGIS, pokud je v současné době spuštěn.
4. V QGIS otevřete dialogové okno `Plugins > Správce doplňků`.
5. V seznamu pluginů najděte `FGDB to GPKG Converter` a zaškrtněte ho, abyste ho aktivovali.

Plugin je nyní nainstalován a aktivován v QGIS. Najdete ho v panelu Processing Toolbox v kategorii `FGDB to GPKG`.

## Použití

1. Otevřete panel Processing Toolbox a rozbalte kategorii `FGDB to GPKG`.
2. Spusťte algoritmus `Convert FGDB to GPKG`.
3. Zvolte vstupní File Geodatabase (.gdb) a výstupní GeoPackage (.gpkg).
4. Klikněte na tlačítko `Spustit`.

## Autorství

Tento plugin byl zcela napsán jazykovým modelem ChatGPT od OpenAI.

---

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Release](https://img.shields.io/github/release/breta01/fgdb_to_gpkg.svg)](https://github.com/breta01/fgdb_to_gpkg/releases)
[![GitHub Issues](https://img.shields.io/github/issues/breta01/fgdb_to_gpkg.svg)](https://github.com/breta01/fgdb_to_gpkg/issues)
