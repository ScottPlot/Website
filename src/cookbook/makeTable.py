from typing import ForwardRef
import urllib.request
import json
import pyperclip

versions = """
4.1.16 | 2021-05-30 | [Cookbook](../cookbooks/4.1.16) | [API](https://www.fuget.org/packages/ScottPlot/4.1.16)
4.1.14 | 2021-05-22 | [Cookbook](../cookbooks/4.1.14) | [API](https://www.fuget.org/packages/ScottPlot/4.1.14)
4.1.13-beta | 2021-05-02 | [Cookbook](../cookbooks/4.1.13-beta) | [API](https://www.fuget.org/packages/ScottPlot/4.1.13-beta)
4.1.12-beta | 2021-04-12 | [Cookbook](../cookbooks/4.1.12-beta) | [API](https://www.fuget.org/packages/ScottPlot/4.1.12-beta)
4.1.11-beta | 2021-03-29 | [Cookbook](../cookbooks/4.1.11-beta) | [API](https://www.fuget.org/packages/ScottPlot/4.1.11-beta)
4.1.10-beta | 2021-03-21 | [Cookbook](../cookbooks/4.1.10-beta) | [API](https://www.fuget.org/packages/ScottPlot/4.1.10-beta)
4.1.9-beta | 2021-02-21 | [Cookbook](../cookbooks/4.1.9-beta) | [API](https://www.fuget.org/packages/ScottPlot/4.1.9-beta)
4.1.8-beta | 2021-02-16 | [Cookbook](../cookbooks/4.1.8-beta) | [API](https://www.fuget.org/packages/ScottPlot/4.1.8-beta)
4.1.7-beta | 2021-02-14 | [Cookbook](../cookbooks/4.1.7-beta) | [API](https://www.fuget.org/packages/ScottPlot/4.1.7-beta)
4.1.6-beta | 2021-02-08 | [Cookbook](../cookbooks/4.1.6-beta) | [API](https://www.fuget.org/packages/ScottPlot/4.1.6-beta)
4.1.5-beta | 2021-02-01 | [Cookbook](../cookbooks/4.1.5-beta) | [API](https://www.fuget.org/packages/ScottPlot/4.1.5-beta)
4.1.4-beta | 2021-02-14 | [Cookbook](../cookbooks/4.1.4-beta) | [API](https://www.fuget.org/packages/ScottPlot/4.1.4-beta)
4.1.3-beta | 2020-12-27 | [Cookbook](../cookbooks/4.1.3-beta) | [API](https://www.fuget.org/packages/ScottPlot/4.1.3-beta)
4.1.2-beta | 2020-12-12 | [Cookbook](../cookbooks/4.1.2-beta) | [API](https://www.fuget.org/packages/ScottPlot/4.1.2-beta)
4.0.47 | 2020-12-11 | [Cookbook](../cookbooks/4.0.47) | [API](https://www.fuget.org/packages/ScottPlot/4.0.47)
4.0.46 | 2020-12-11 | [Cookbook](../cookbooks/4.0.46) | [API](https://www.fuget.org/packages/ScottPlot/4.0.46)
4.0.44 | 2020-11-22 | [Cookbook](../cookbooks/4.0.44) | [API](https://www.fuget.org/packages/ScottPlot/4.0.44)
4.0.40 | 2020-09-20 | [Cookbook](../cookbooks/4.0.40) | [API](https://www.fuget.org/packages/ScottPlot/4.0.40)
4.0.38 | 2020-07-06 | [Cookbook](../cookbooks/4.0.38) | [API](https://www.fuget.org/packages/ScottPlot/4.0.38)
4.0.36 | 2020-06-21 | [Cookbook](../cookbooks/4.0.36) | [API](https://www.fuget.org/packages/ScottPlot/4.0.36)
4.0.35 | 2020-09-09 | [Cookbook](../cookbooks/4.0.35) | [API](https://www.fuget.org/packages/ScottPlot/4.0.35)
4.0.32 | 2020-05-17 | [Cookbook](../cookbooks/4.0.32) | [API](https://www.fuget.org/packages/ScottPlot/4.0.32)
4.0.31 | 2020-05-05 | [Cookbook](../cookbooks/4.0.31) | [API](https://www.fuget.org/packages/ScottPlot/4.0.31)
4.0.30 | 2020-05-03 | [Cookbook](../cookbooks/4.0.30) | [API](https://www.fuget.org/packages/ScottPlot/4.0.30)
4.0.29 | 2020-04-11 | [Cookbook](../cookbooks/4.0.29) | [API](https://www.fuget.org/packages/ScottPlot/4.0.29)
4.0.28 | 2020-04-07 | [Cookbook](../cookbooks/4.0.28) | [API](https://www.fuget.org/packages/ScottPlot/4.0.28)
4.0.27 | 2020-04-05 | [Cookbook](../cookbooks/4.0.27) | [API](https://www.fuget.org/packages/ScottPlot/4.0.27)
4.0.26 | 2020-04-04 | [Cookbook](../cookbooks/4.0.26) | [API](https://www.fuget.org/packages/ScottPlot/4.0.26)
4.0.25 | 2020-03-29 | [Cookbook](../cookbooks/4.0.25) | [API](https://www.fuget.org/packages/ScottPlot/4.0.25)
4.0.24 | 2020-03-27 | [Cookbook](../cookbooks/4.0.24) | [API](https://www.fuget.org/packages/ScottPlot/4.0.24)
4.0.23 | 2020-03-23 | [Cookbook](../cookbooks/4.0.23) | [API](https://www.fuget.org/packages/ScottPlot/4.0.23)
4.0.22 | 2020-03-16 | [Cookbook](../cookbooks/4.0.22) | [API](https://www.fuget.org/packages/ScottPlot/4.0.22)
4.0.21 | 2020-03-14 | [Cookbook](../cookbooks/4.0.21) | [API](https://www.fuget.org/packages/ScottPlot/4.0.21)
3.1.6 | 2019-10-10 | [Cookbook](../cookbooks/3.1.6) | [API](https://www.fuget.org/packages/ScottPlot/3.1.6)
"""

all = ""
for line in versions.split("\n"):
    if not "|" in line:
        continue
    parts = line.split("|")
    version = parts[0].strip()
    date = parts[1].strip()
    cookbookUrl = f"https://swharden.com/scottplot/cookbooks/{version}"
    apiUrl = f"https://www.fuget.org/packages/ScottPlot/{version}"
    controlUrl = f"https://www.fuget.org/packages/ScottPlot.WinForms/{version}"
    releaseNotesUrl = f"https://github.com/ScottPlot/ScottPlot/releases/tag/{version}"
    line = f"{version} | {date} | [Cookbook]({cookbookUrl}) | [Release Notes]({releaseNotesUrl})"
    all += line+"\n"

print(all)
pyperclip.copy(all)
