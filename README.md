<a name="readme-top"></a>
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
        <li><a href="#dependencies">Dependencies</a></li>
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

#### 1. Using pip [Демонстрация](https://asciinema.org/a/MwxcwiKeeYnqhAfq5asKOGTuY)

```
pip install --user git+https://github.com/Viewsoul237/python-project-50
```

#### 2. Using poetry [Демонстрация](https://asciinema.org/a/ShWliOs89DVj8a396XvhevHzD)
1. Clone the repo
   ```
   git clone https://github.com/Viewsoul237/python-project-50.git
   cd python-project-50
   ```
2. Install dependencies
   ```
   make install-dependencies
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



<!-- USAGE EXAMPLES -->
## Usage
```
usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output (default: stylish).
                        Formats: {stylish, plain, json}.

```
<br></p>
*"Specify the absolute path to the file.*
### 1. Output as PLAIN format
   ```
   gendiff -f plain file1.json file2.json
   gendiff --format plain file1.json file2.json 
   ```

[Demonstration plain](https://asciinema.org/a/oxog97znofEhp8TcPxV2Q4bDe)
<br></p>
![](/images/plain.png)


### 2. Output as STYLISH format
Stylish format is by default, but you can specify it explicitly.
   ```
   gendiff --format stylish file1.json file2.json
   gendiff -f stylish file1.yaml file2.json
   gendiff file1.json file2.yml   
   ```

[Demonstration stylish](https://asciinema.org/a/nVDDWGMrCqg2GFkHR4OMrdSsL)
<br></p>
![](/images/stylish.png)


### 3. Output as JSON format
Structured format output is often required, for example, in json.
This allows other programs to utilize your output for their functionality.
   ```
   gendiff --format json file1.yaml file2.json
   gendiff -f json file1.yaml file2.json 
   ```

[Demonstration json](https://asciinema.org/a/o5WnxRzOy55WZnGIWUVdrKeRB)
<br></p>

![](/images/json.png)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Andrey Yudakov - [telegram](https://t.me/viewsoul237) - viewsoul91@gmail.com

Project Link: [https://github.com/Viewsoul237/python-project-50](https://github.com/Viewsoul237/python-project-50)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



