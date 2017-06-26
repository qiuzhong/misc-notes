# Introduction
Useful information about Node.js native-related modules

## Tools
To build a native Node.js module, you need to the following pre-conditions:
* Build tools:
  * [windows-build-tools](https://github.com/felixrieseberg/windows-build-tools): Windows-specific tools. It will download Visual C++ Build Tools 2015 and Python and install them. The Visual C++ Build Tools 2015 is installed at **C:\Program Files (x86)\Microsoft Visual Studio\Shared\14.0**. For the VC++ compiler version, please refer to [VC++ compiler](https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B). Python is installed at **C:\Users\<USER>\.windows-build-tools\python27**.
  * GCC or Clang: for other Unix-like platform.
* [node-gyp](https://github.com/nodejs/node-gyp): a cross-platform command-line tool written in Node.js for compiling native addon modules for Node.js

## Current status:
Because V8 changes crazy. All the Node.js addons code needs to update or compile for eeach platform. There are two projects try to fix this problem:
* [nan](https://github.com/nodejs/nan)
* [N-API](https://github.com/nodejs/abi-stable-node)
