[![Actions Status](https://github.com/Viewsoul237/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Viewsoul237/python-project-50/actions)
[![Actions Status](https://github.com/Viewsoul237/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/Viewsoul237/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/1bc0ca1e3fa3f4d83705/maintainability)](https://codeclimate.com/github/Viewsoul237/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/1bc0ca1e3fa3f4d83705/test_coverage)](https://codeclimate.com/github/Viewsoul237/python-project-50/test_coverage)


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Viewsoul237/python-project-50">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
<h2 align="center">Gendiff</h2>
  <p align="center">
    "Gendiff (Difference generator) is a command-line interface (CLI)
    tool designed to illustrate the differences between two JSON and/or YAML files."
    <br />
    <br />
    <br />
    <a href="https://asciinema.org/a/az1xRy7EXWdPvPNxVrKmYU76p">View Demo</a>

  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Dependencies</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- GETTING STARTED -->
## Getting Started

### Dependencies

  ```
  Python = "^3.10"
  Pyyaml = "^6.0.1"
  ```

### Installation

#### 1. Using pip [Демонстрация](https://asciinema.org/a/3W9d4bSFyOAAjThDFNvm0rT3F)

```
pip install --user git+https://github.com/Viewsoul237/python-project-50
```

#### 2. Using poetry [Демонстрация](https://asciinema.org/a/3W9d4bSFyOAAjThDFNvm0rT3F)
1. Clone the repo
   ```
   git clone https://github.com/Viewsoul237/python-project-50.git
   cd python-project-50
   ```
2. Install dependencies
   ```
   poetry install
   ```
3. Install Gendiff
   ```
   make build
   make package-install
   ```
   
#### Uninstall
   ```
   pip uninstall hexlet-code
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Вычислитель отличий

Программа, определяющую разницу между двумя структурами данных.

# Пример использования

[![asciicast](https://asciinema.org/a/az1xRy7EXWdPvPNxVrKmYU76p.svg)](https://asciinema.org/a/az1xRy7EXWdPvPNxVrKmYU76p)
