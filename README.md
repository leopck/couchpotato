# couchpotato
Web Browser Caster or Remote to control your web browser remotely

## Introduction

Pretty much the title says it all, use couchpotato to remote control your favourite websites using simple selenium and REST API from another device such as your smartphone.

## Getting Started

```
git clone https://github.com/leopck/couchpotato
cd couchpotato
pip install -r requirements.txt
python3 rest_server.py
```

Currently there's no website implemented for this solution but it exposes various REST endpoints to launch Chrome with your website. To implement your website, add into plugins.
