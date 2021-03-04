
[MicroPython](https://micropython.org/)是Python的一个精简版本，它是为了运行在单片机这样的性能有限的微控制器上，最小体积仅256K，运行时仅需16K内存。

MicroPython是基于Python 3.4的语法标准。因为要适应嵌入式微控制器，所以裁剪了大部分标准库，仅保留部分模块如`math`、`sys`的部分函数和类。此外，很多标准模块如`json`、`re`等在MicroPython中变成了以`u`开头的`ujson`、`ure`，表示针对MicroPython开发的标准库。

目前，MicroPython除了可以运行在最初开发的[pyboard](https://store.micropython.org/pyb-features)微控制器上外，还可以运行在大量基于ARM的嵌入式系统，如[Arduino](https://www.arduino.cc/)，这样我们就可以通过Python来非常方便地开发自动控制、机器人这样的应用。

本章我们介绍如何使用MicroPython开发简单的机器人应用程序。
