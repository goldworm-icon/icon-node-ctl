# ICON Node Controller

## Overview

* Control all ICON-related docker images on QAVMNet.
    * docker images include both loopchain and iconservice.
* Author: Chiwon Cho (goldworm@iconloop.com)

## Features

* Apply a Docker Image Tag to .env file.
* Start and stop ICON docker image set.
* Remove old database.

## How to use

### Help

```bash
# iconnodectl --help
```

### Start service

```bash
# iconnodectl start --help
# iconnodectl start
```

### Stop service

```bash
# iconnodectl stop --help
# iconnodectl stop
```

### Remove database

```bash
# iconnodectl removedb --help
# iconnodectl removedb
```

### Restart service

```bash
# iconnodectl restart --help
# iconnodectl restart --reset-db --tag 1907161122x07ce31
```
