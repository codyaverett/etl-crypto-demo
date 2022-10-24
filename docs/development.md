# Development



## Dependencies

- pydev
- python3 (dnf install python)
- poetry
- pipenv
- podman
- buildah

> NOTE: I'm using fedora linux for development of this project.

## Install pyenv

```shell
curl https://pyenv.run | bash
```

## Setup build environment for your system
https://github.com/pyenv/pyenv/wiki#suggested-build-environment

## Add this to your ~/.bashrc
```shell
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

# Install additional dependencies
```shell
sudo dnf install podman buildah
```
