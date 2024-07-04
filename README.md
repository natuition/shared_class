# Python Shared Classes for Natuition

This repository contains a collection of shared classes for Natuition projects. They are designed to be included and shared across multiple Git projects.

## Introduction

The purpose of this repository is to centralize common and useful Python classes for various projects. The classes present here have been carefully designed to be modular and easy to integrate into other projects.

## Available Classes

### List of Classes

1. `RobotSynthesis` - Enum representing the data that a Violette robot can send to give a status of its current state.
2. `RobotMonitoring` - Enum representing the different statuses when monitoring a Violette robot.

## Installation

To use these classes in your project, import this repository as a submodule.

### Import the Repository

```bash
git submodule add git@github.com:natuition/shared_class.git
```

### Usage

Here is an example of using the `RobotSynthesis` class :

```python
from shared_class import *

...

if self.__get_current_synthesis() in [RobotSynthesis.OP, RobotSynthesis.UI_CHECK_STATE]:

...
```

## Contact

For any questions or suggestions, contact:

- Email: v.lambert@natuition.com
- GitHub: [https://github.com/natuition](https://github.com/natuition)
