# Gulp Hello World demo
## Introduction
Gulp: Automate and enhance your workflow.

## Personal View
Gulp is very like the Grunt

## Install Gulp
```
$ sudo npm install -g gulp-cli --verbose
```

### Runt the demo
```
$ git clone https://github.com/qiuzhong/mis-notes.git
$ cd misc-notes/node/gulp/demo
$ npm install --verbose
$ gulp
[16:53:22] Using gulpfile ~/00-workspace/github/qiuzhong/misc-notes/node/gulp/demo/gulpfile.js
[16:53:22] Starting 'default'...
Hello World!
[16:53:22] Finished 'default' after 136 μs
```

### Steps to generate a gulp project
```
$ mkdir project
$ cd project
$ npm init
$ npm install gulp --save-dev
$ touch gulpfile.js
```

After update the gulpfile.js, run
```
$ gulp
```
