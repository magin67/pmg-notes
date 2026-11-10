---
title: "Installing the Library and Running Examples"
date: 2026-10-29
updated: 2026-11-11
revision: 13
translated_revision: 13
status: draft
text_prepared_by: ChatGPT
translation_key: python-examples-getting-started
lang: en
description: "Installing polyform_algebra, first calculations, and running examples locally and in Google Colab."
order: 1
---

This note describes the shared environment for [[en/PythonExamples/PythonExamples|Programming Examples]]. The installed package is sufficient for calculations; the weighted-chain notebook combines explanations and executable code.

[[ru/PythonExamples/Установка библиотеки и запуск примеров|Русский]]

## Package version

The examples were checked with **`polyform_algebra 0.9.0`** on Python 3.12. The installation commands use the package’s `v0.9.0` source archive. Neither Git nor a source checkout is needed to run the fragments. Dependencies are installed automatically without version pins, so the package version does not fix the entire environment.

For the [[en/PythonExamples/Example - Metric Parameters of Graphs|Metric Parameters]], [[en/PythonExamples/Example - Checking Structural Identities|Structural Identities]], [[en/PythonExamples/Example - Checking Symmetric Polyform Identities|Symmetric Polyforms]], [[en/PythonExamples/Example - Combinatorial Potentials|Combinatorial Potentials]], [[en/PythonExamples/Example - Partition Toponomes|Partition Toponomes]], and [[en/PythonExamples/Example - Polynomial Toponomes|Polynomial Toponomes]] notebooks, use the commit specified in the corresponding example. The first code cell installs it in Colab.

## Local installation

Create a separate virtual environment. In Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install "https://github.com/magin67/polyform_algebra/archive/refs/tags/v0.9.0.zip"
```

On Linux/macOS:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install "https://github.com/magin67/polyform_algebra/archive/refs/tags/v0.9.0.zip"
```

Activation is optional: call the environment’s interpreter directly. Save a note’s sequential fragments in `my_example.py`, then run `.\.venv\Scripts\python.exe my_example.py` on Windows or `.venv/bin/python my_example.py` on Linux/macOS.

## First calculation

```python
import polyform_algebra
print(polyform_algebra.get_version())  # 0.9.0
```

This calculation builds a unit triangle and checks its spanning-tree coefficient and resistance:

```python
from math import isclose
from polyform_algebra import Point, quForm

# Construct a unit triangle and its metric polyform.
a, b, c = Point.create_list("abc")
f_ab = quForm([(a, b)])
f_ac = quForm([(a, c)])
f_bc = quForm([(b, c)])
laplacian = f_ab + f_ac + f_bc
metric = laplacian.exp()

# Check the spanning-tree coefficient and effective resistance.
tau = metric.potential(quForm.one())
r_ab = metric.norm(f_ab)
print("tau =", tau)
print("R_ab =", r_ab)
assert isclose(tau, 3.0)
assert isclose(r_ab, 2/3)
```

Expect $\tau=3$ and $R_{ab}=2/3$. `exp()` computes the exponential in the algebra of forms, `potential()` gives an unnormalized potential, and `norm()` divides it by the spanning-tree coefficient. Printed formatting may differ; `assert` checks the numerical value.

## Working in Google Colab

[Open in Colab](https://colab.research.google.com/github/magin67/pmg-notes/blob/v5/pmg-library/en/PythonExamples/notebooks/weighted-chain.ipynb) · [Download notebook](https://raw.githubusercontent.com/magin67/pmg-notes/v5/pmg-library/en/PythonExamples/notebooks/weighted-chain.ipynb)

Open the notebook and run all cells. Its first cell installs the package version; the diagram, calculation, and checks follow. Save a copy to Google Drive or download the `.ipynb` to edit your own version.

In a new blank notebook, use this installation cell:

```python
%pip install -q "https://github.com/magin67/polyform_algebra/archive/refs/tags/v0.9.0.zip"
```

Then run the chosen note’s fragments in order. Restart the runtime after changing an already imported package version. Colab runtimes are temporary: repeat installation in a new session. Mounting Google Drive is not required for the calculations.

The notebook was checked by running all cells in a fresh local Python 3.12 kernel. Execution in a hosted Colab session was not separately checked.

## Checks and source code

The notes provide expected values and result checks. Complete programs and tests are available in the [version 0.9.0 sources](https://github.com/magin67/polyform_algebra/tree/v0.9.0/examples/introductory). They help explain the implementation but are not required to run the fragments or notebook.

For development, download and extract the [source archive](https://github.com/magin67/polyform_algebra/archive/refs/tags/v0.9.0.zip), then run from the directory containing `pyproject.toml`:

```bash
python -m pip install -e ".[dev]"
python -m pytest tests/introductory -q
```

Here `python` means the selected environment’s interpreter. These steps are for working with the package tests.

## Troubleshooting

- `ModuleNotFoundError`: check that installation and execution use the same environment.
- `NameError`: run the preceding cells in this note.
- Unexpected result: check `polyform_algebra.get_version()`, conductances, and cell order.
- `ValueError` on normalization after bridge deletion: this expected case is explained in [[Example - Deleting an Edge and a Bridge]].
