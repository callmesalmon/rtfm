# RTFM - Read The Fucking Manual
RTFM is a manual generation tool for when someone on the archlinux website tells you to "rtfm".
It is the shittiest manual generation tool around, and might also be written in python, so that's
even worse.

## Install
```console
git clone https://github.com/callmesalmon/rtfm
cd rtfm
./install.sh
```

## How to
RTFM operates by using a configuration file, kind of like `make`!
The configuration file is called `rtfm.yml`, so we can start of
with creating that:
```console
touch rtfm.yml
```
Open it. RTFM operates by using a YAML-like configuration (tough I built this parser from
scratch, so it's much worse than say, libyaml3). This is an example:
```yaml
console:
    cmd: echo "Hello World"
building:
    use: roff
    build: main.1
tooling:
    tool: mytool troff
    use: mytool
    build: main.1
```
This will eventually run:
```console
echo "Hello World"
groff main.1
troff main.1
```
Then compile with the command `rtfm` and you're good to go:
```console
rtfm
```
Manual generated! There are also examples included in the repo
which you can run with:

```sh
cd examples
sudo rtfm
man rtfm-test
```
