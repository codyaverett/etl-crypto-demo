# Slither

Slither is a static analysis too for ethereum smart contracts. [Basic slither cli usage](./slither_usage.md)

I have been using slither from a docker container to try and analyse patterns in my list of smart contracts in an attempt to find some useful/interesting metrics.  There are various output modes called [printers](https://github.com/crytic/slither#printers) that are available to provide various output options. 

I've combined my love of basic shell scripting with slither's toolbox container to dig into some contracts and find interesting metrics.  I think interactive toolsets like these to be handy when performing manual semi automated research against a large number of contracts.  If some useful or interesting metric is found time can then be invested into automatically populating the discovered metric over time against any number of smart contract addresses.

Given more time, I'd probably invest in building out a more strucutured CLI framework in python or nodejs to streamline the toolset where accounts can be sourced from a shared db, new lists can be created and managed by the team, and provide selectively mapped output variables instead of generating large json files for furture parsing, etc.

## Setup

Create `share/.env` with a valid etherscan apikey defined.

```.env
ETHERSCAN_API_KEY=A_VALID_API_KEY
```

## Usage

[it.sh](./it.sh) - runs a slither toolbox container in interactive mode and mounts the `./share` directory to the containers `/share` directory

[run](./share/run) - shell script that will run a command script against the list of contract addresses.  Used inside the slither container.

### Commands

Commands are simple shell scripts that can run any shell commands available in the container.

There are a few varibles that are automatically defined in the [./share/run](./share/run) script that may be used within a command script.

- CURRENT_RUN_NAME
- CURRENT_RUN_LINE
- OUTPUT_DIR
- ETHERSCAN_API_KEY (defined in [./share/.env](./share/.env))

For an example using these environment variables reference [example2](./share/commands/example2.sh)

### From within the container

From the `/share` directory in the container you can run the `run` script to run command scripts specified in `/share/commands/`

#### e.g. You want to run `/share/commands/example.sh` across all the lines of `/share/list.txt`

##### /share/commands/example.sh
```shell
echo "Example Args: $@"
```

##### /share/list.txt
```txt
0x3caca7b48d0573d793d3b0279b5f0029180e83b6
0xcc9a0b7c43dc2a5f023bb9b738e45b0ef6b06e04
```

##### /share/run
```shell
ethsec@22abfc8658ff:/share$ ./run example

start: 0x3caca7b48d0573d793d3b0279b5f0029180e83b6
----------------------------------------
Example Args: 0x3caca7b48d0573d793d3b0279b5f0029180e83b6
----------------------------------------
end: 0x3caca7b48d0573d793d3b0279b5f0029180e83b6

start: 0xcc9a0b7c43dc2a5f023bb9b738e45b0ef6b06e04
----------------------------------------
Example Args: 0xcc9a0b7c43dc2a5f023bb9b738e45b0ef6b06e04
----------------------------------------
end: 0xcc9a0b7c43dc2a5f023bb9b738e45b0ef6b06e04

```

### JSON Output can be saved to files using the --json property

```shell
# From within a slither container
slither --json "$OUTPUT_DIR/$CURRENT_RUN_LINE.json" --etherscan-apikey "$ETHERSCAN_API_KEY" $CURRENT_RUN_LINE```
