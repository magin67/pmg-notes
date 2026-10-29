---
title: "Installing the Library and Running Examples"
date: 2026-10-29
updated: 2026-10-29
revision: 4
source_revision: 4
status: draft
text_prepared_by: ChatGPT
translation_key: python-examples-getting-started
lang: en
description: "Installing polyform_algebra, first calculations, and running examples locally and in Google Colab."
order: 1
---

This note describes the shared environment for [[en/PythonExamples/PythonExamples|Programming Examples]]. You can perform your own Python calculations or run the complete programs and tests from the repository.

[[ru/PythonExamples/Установка библиотеки и запуск примеров|Русский]]

## Code version

The examples use revision [`95cea4c`](https://github.com/magin67/polyform_algebra/commit/95cea4c37e8b743a4ede2bf01392c8b3babdcfb3). Local validation of that revision used Python 3.12. Dependencies are installed through pip without pinning their versions, so fixing the code revision does not fix the entire environment. Newer library versions may differ from the version used by a note.

## Local installation

Install Python and Git. Run the commands in a terminal from the directory where a separate `polyform-examples` checkout should be created. In Windows PowerShell:

```powershell
git clone https://github.com/magin67/polyform_algebra.git polyform-examples
cd polyform-examples
git checkout 95cea4c37e8b743a4ede2bf01392c8b3babdcfb3
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
```

On Linux/macOS:

```bash
git clone https://github.com/magin67/polyform_algebra.git polyform-examples
cd polyform-examples
git checkout 95cea4c37e8b743a4ede2bf01392c8b3babdcfb3
python3 -m venv .venv
.venv/bin/python -m pip install -e ".[dev]"
```

The virtual environment isolates dependencies. Activation is optional because the commands invoke its Python directly. The editable installation `-e` connects the package to its sources; `[dev]` adds testing tools. For ordinary library use, installation without `[dev]` is sufficient.

## First calculation

Save the code as `my_example.py` inside the new directory. On Windows run `.\.venv\Scripts\python.exe my_example.py`; on Linux/macOS run `.venv/bin/python my_example.py`. In a notebook, put the same code in a cell:

```python
from math import isclose
from polyform_algebra import Point, quForm

# Construct a unit triangle and its metric polyform.
a, b, c = Point.create_list(["1", "2", "3"])
f12 = quForm([(a, b)])
f13 = quForm([(a, c)])
f23 = quForm([(b, c)])
laplacian = f12 + f13 + f23
metric = laplacian.exp()

# Check the spanning-tree coefficient and effective resistance.
tau = metric.potential(quForm.one())
r12 = metric.norm(f12)
print("tau =", tau)
print("R12 =", r12)
assert isclose(tau, 3.0)
assert isclose(r12, 2/3)
```

Expect `tau = 3` and `R12 ≈ 0.6666666667`; printed formatting may differ. `Point` creates vertices, `quForm` defines a quadratic form, and their sum constructs the Laplacian. `exp()` computes the exponential in the algebra of forms, `potential()` extracts an unnormalized coefficient, and `norm()` gives a normalized metric evaluation. An assertion passes when it raises no error.

For further experiments, change conductances, for example `laplacian = 2*f12 + f13 + f23`, then recompute `metric`. Expected values must also match the new network. Negative coefficients are valid in the algebra, while an ordinary electrical network requires admissible conductances. This series stays within the implemented quadratic subalgebra.

## Complete programs and tests

From the cloned repository root, in PowerShell:

```powershell
.\.venv\Scripts\python.exe -m examples.introductory.note01_weighted_chain
.\.venv\Scripts\python.exe -m examples.introductory.note05_triangle_geometry
.\.venv\Scripts\python.exe -m examples.introductory.note06_single_edge
.\.venv\Scripts\python.exe -m examples.introductory.note07_two_edges
.\.venv\Scripts\python.exe -m examples.introductory.note10_path_cycle
.\.venv\Scripts\python.exe -m pytest tests/introductory -q
```

On Linux/macOS replace the interpreter path with `.venv/bin/python`. Omit `tests/introductory` to run all tests. Programs print their results; pytest checks expected values. See [[Weighted Chain in Python]] and [[Triangle Coupling Variations in Python]] for the mathematical discussion.

## Google Colab

Open [Google Colab](https://colab.research.google.com/), create a Python notebook, and connect a standard CPU runtime. These examples do not need a GPU. Execute cells in order, for example with Shift+Enter.

### Your own calculations

Install the library in the first cell:

```python
%pip install "polyform_algebra @ git+https://github.com/magin67/polyform_algebra.git@95cea4c37e8b743a4ede2bf01392c8b3babdcfb3"
```

Paste the code from “First calculation” into the second cell. The `%pip` command installs the package in the current [IPython kernel](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-pip). It is a notebook command and should not be copied into an ordinary `.py` file.

### Complete series programs and tests

For this route, clone the sources instead of using the first installation cell. The installed package alone does not include `examples` and `tests`:

```python
# Run once in a fresh runtime to obtain the example and test files.
!git clone https://github.com/magin67/polyform_algebra.git /content/polyform-examples
%cd /content/polyform-examples
!git checkout 95cea4c37e8b743a4ede2bf01392c8b3babdcfb3
%pip install -e ".[dev]"
```

Run the programs and checks in the next cell:

```python
import subprocess
import sys

# Use the notebook kernel's interpreter and stop on failure.
for module in (
    "examples.introductory.note01_weighted_chain",
    "examples.introductory.note05_triangle_geometry",
    "examples.introductory.note06_single_edge",
    "examples.introductory.note07_two_edges",
    "examples.introductory.note10_path_cycle",
):
    subprocess.run([sys.executable, "-m", module], check=True)
subprocess.run(
    [sys.executable, "-m", "pytest", "tests/introductory", "-q"],
    check=True,
)
```

Do not clone an existing directory again: omit the `git clone` line when repeating these steps. If the library was imported before changing its version, restart the Python session and execute the cells again.

### Saving your work

Save the notebook to Google Drive or download the `.ipynb` file. Colab runtimes are temporary: installed packages and files under `/content` can disappear with the runtime. Repeat installation and cell execution in a new runtime. These examples do not require mounting Google Drive. See the [official Colab FAQ](https://research.google.com/colaboratory/faq.html) for these runtime properties.

## Validation and troubleshooting

- `ModuleNotFoundError: polyform_algebra`: ensure installation and execution use the same environment. In Colab, run the installation cell first.
- `examples.introductory` cannot be found: change to the cloned repository root; installing the package alone is insufficient.
- `NameError` in a notebook: run earlier cells that create the objects.
- Unexpected results: check the revision with `git rev-parse HEAD`, initial conductances, and cell execution order.

The first calculation was checked locally. Colab instructions follow the service documentation; execution in a hosted Colab session has not been separately verified. Checking particular examples does not replace a mathematical proof.
