# RTFM - Read The Fucking Manual
RTFM is a manual generation tool for when someone on the archlinux website tells you to "rtfm".
It is the shittiest manual generation tool around, and might also be written in python, so that's
even worse.

## Install
```console
git clone https://github.com/ElisStaaf/rtfm
cd rtfm
./install.sh
```

## How to
RTFM operates by using a configuration file, kind of like `make`!
The configuration file is called `rtfm.cfg`, so we can start of
with creating that:
```console
touch rtfm.cfg
```
Open it. RTFM operates by using a YAML-like configuration (tough I built this parser from
scratch, so it's much worse than say, libyaml3). This is an example:
```yaml
def console:
    cmd: echo "Hello World"
def building:
    use: roff
    build: main.1
def tooling:
    tool: mytool gcc
    use: mytool
    build: main.1
```
This will eventually run:
```console
echo "Hello World"
groff main.1
gcc main.1
```
Then compile with the command `rtfm` and you're good to go:
```console
rtfm
```
Manual generated!
