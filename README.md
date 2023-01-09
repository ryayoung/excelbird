<h1> excelbird &nbsp;&nbsp;&nbsp; <a href="https://pypi.org/project/excelbird/" alt="Version"> <img src="https://img.shields.io/pypi/v/excelbird.svg" /></a> &nbsp;&nbsp;&nbsp; <a href="https://github.com/ryayoung/excelbird/actions"> <img src="https://github.com/ryayoung/excelbird/actions/workflows/tests.yaml/badge.svg"/> </a> </h1>

```text
pip install excelbird
```

> **A front-end framework for Excel that can do magical things.**

**The problem:** With traditional tools, scripting Excel is tedious for two reasons:
1. **Layout**: You must refer to actual cell locations in your code, and tell them each what to do.
2. **Cell References**: The most important feature of a spreadsheet - the ability to see how calculations were made - is not available to you when scripting.

**With excelbird:**
1. Layout and styling is as easy as building an HTML page. You don't have to tell cells where to go.
2. A dataframe library where all calculations are lazily evaluated as formulas and cell references at write time.

#

<img src="https://i.imgur.com/We95Soe.png" width="600">

# Elements

<table>
    <th colspan=2><i>Workbook</i></th>
    <tr>
    <td><code>Book</code></td>
    <td><code>Sheet</code></td>
    </tr>
</table>

<table>
    <th colspan=2><i>Stack</i></th>
    <tr>
    <td><code>HStack</code> / <code>VStack</code></td>
    <!-- <td><code>HStack</code></td> -->
    </tr>
</table>

<table>
    <tr>
    <th><i>DataFrame</i></th>
    <th><i>Series</i></th>
    <th><i>Value</i></th>
    </tr>
    <tr>
    <td><code>HFrame</code> / <code>VFrame</code></td>
    <!-- <td><code>VFrame</code></td> -->
    <td><code>Col</code> / <code>Row</code></td>
    <!-- <td><code>Row</code></td> -->
    <td><code>Cell</code></td>
    </tr>
</table>


<table>
    <th colspan=3><i>Other</i></th>
    <tr>
    <td><code>Gap</code></td>
    <td><code>Expr</code></td>
    <td><code>I</code> (<code>ImpliedType</code>)</td></tr>
</table>

# Examples


<img src="https://i.imgur.com/Cx1yVN3.png" width="350">

![]()

![]()