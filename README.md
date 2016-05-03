## What is this?
This project is a drop in replacement for [sshuttle](https://github.com/sshuttle/sshuttle)
which is described as follows:
```
Transparent proxy server that works as a poor man's VPN.
Forwards over ssh.
Doesn't require admin.
Works with Linux and MacOS.
Supports DNS tunneling.
```
It's an amazing little piece of software, and I tend to find obscure new uses
for it every day. Read more about it on the official documentation
[here](http://sshuttle.readthedocs.org/). This is a binary packaged `sshuttle`
that you don't have to `pip install`. It's a single binary that you can drop in
your path and then go about your business.

## Installation
It works the same on OSX and Linux. I've personally tested it on Debian 8,
Ubuntu 14.04 LTS, and OSX 10.10/10.11. They all seemed to work. You can grab the
latest version and set it executable with something like this:
```bash
sudo curl -o /usr/local/bin/sshuttle -L "https://github.com/rholder/sshuttle-binary/releases/download/v0.78.0/sshuttle" && \
sudo chmod +x /usr/local/bin/sshuttle
```

## License
This sshuttle-binary scaffolding project is released under version 2.0 of the
[Apache License](http://www.apache.org/licenses/LICENSE-2.0). The original sshuttle
project is released under [Library GPL Version 2.0](http://www.gnu.org/licenses/old-licenses/lgpl-2.0.en.html).