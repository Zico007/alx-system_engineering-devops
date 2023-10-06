# Puppet introduction

In this repository, we will look at the concept of configuration management. Puppet is a great tool for automating stuff and configurations on the web servers and we will learn how to use puppet resources to achieve just that. Using manifests, resources, one can write classes to manage nodes, via the puppet master. Note only 'nix devices, os can be a Puppet master. Windows cannot be a puppet master

## Manifests :scroll:

This repo contains the following puppet manifests
|Manifest|Action|
|:---|:---|
|[0-create_a_file.pp](./0-create_a_file.pp)|This file creates a file in /tmp/ directory named school with the contents "I love school"|
|[1-install_a_package.pp](./1-install_a_package.pp)|This manifest uses puppet to install via pip3|
|[2-excute_a_command.pp](./2-execute_a_command.pp)|This manifest kills a process named "killmenow"|
