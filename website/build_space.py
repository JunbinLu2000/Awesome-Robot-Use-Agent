"""Package the existing catalogue as a Hugging Face Static Space."""
import shutil
from urllib.parse import urlsplit, unquote

from bs4 import BeautifulSoup
import build as website


def build_space():
    output = website.HERE / 'space-dist'
    previous_output = website.OUT
    try:
        website.OUT = output
        total = website.build()
    finally:
        website.OUT = previous_output

    page = BeautifulSoup((output / 'index.html').read_text(), 'html.parser')
    # The original analytics and page-view total belong to GitHub Pages.
    for node in page.select('#google-analytics, .site-views'):
        node.decompose()
    # External destinations must open outside the Space iframe.
    for link in page.select('a[href]'):
        if urlsplit(link['href']).scheme in ('http', 'https'):
            link['target'] = '_blank'
            link['rel'] = 'noopener noreferrer'
    (output / 'index.html').write_text(str(page))
    script = (output / 'app.js').read_text()
    assert script.count('\nloadViews();') == 1
    (output / 'app.js').write_text(script.replace(
        '\nloadViews();', "\nif (document.querySelector('#view-count')) loadViews();"))
    shutil.copyfile(website.ROOT / 'LICENSE', output / 'LICENSE')
    (output / 'README.md').write_text('''---
title: Awesome Robot Use Agent
emoji: 🤖
colorFrom: yellow
colorTo: gray
sdk: static
app_file: index.html
fullWidth: true
header: mini
license: mit
short_description: Papers, tools, benchmarks and demos for robot-use agents
thumbnail: assets/previews/robot-use-overview.png
tags:
  - robotics
  - embodied-ai
  - agents
  - awesome-list
---

# Awesome Robot Use Agent (RUA)

A curated, searchable collection of research papers, open-source projects,
tools, datasets, benchmarks, and community demos for robot-use agents.

Search by topic, author, or task; filter for code and demo environments;
sort papers by date, GitHub stars, or citations. Community demos include
GPT-6 Astra × Robotics examples from X and RedNote, with original sources
and distinctions between real robots, simulation, and supporting perception.

- [GitHub and contributions](https://github.com/kairunwen/Awesome-Robot-Use-Agent)
- [GitHub Pages](https://kairunwen.github.io/Awesome-Robot-Use-Agent/)
- [Discord](https://discord.gg/rpBvfef4b)

This Space is built from the same README and website sources as GitHub Pages.
Resource descriptions and media retain their original source links;
the collection does not claim authorship of the included third-party work.

To refresh: run `website/.venv/bin/python website/build_space.py` in the
source repository, then upload the contents of `website/space-dist/` here.
''')

    assert len(page.select('.entry')) == total
    assert not page.select('#google-analytics, #view-count')
    for node in page.select('[src], link[href]'):
        url = urlsplit(node.get('src', node.get('href', '')))
        if url.path and not url.scheme and not url.netloc:
            assert (output / unquote(url.path)).is_file(), url.path
    print(f'Built and checked {total} entries → {output}')


if __name__ == '__main__':
    build_space()
