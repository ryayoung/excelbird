"""

<div class="output_area rendered_html docutils container">
<table class="dataframe">
<thead>
<tr>
<th>Python</th>
<th>Excel</th>
</tr>
</thead>
<tbody>

<tr>
<td>`a >> b`</td>
<td>`a : b`</td>
</tr>

<tr>
<td>`a == b`</td>
<td>`a = b`</td>
</tr>

<tr>
<td>`a == b`</td>
<td>`a = b`</td>
</tr>

<tr>
<td>`a != b`</td>
<td>`a <> b`</td>
<td> </td>
</tr>

<tr>
<td>`a > b < c`</td>
<td>`a > b < c`</td>
<td> </td>
</tr>

<tr>
<td>`a >= b`</td>
<td>`a >= b`</td>
<td> </td>
</tr>

<tr>
<td>`a + b`</td>
<td>`a + b`</td>
<td> </td>
</tr>

<tr>
<td>`a & b`</td>
<td>`a & b`</td>
<td> </td>
</tr>

<tr>
<td>`a - b`</td>
<td>`a - b`</td>
<td> </td>
</tr>

<tr>
<td>`a * b`</td>
<td>`a * b`</td>
<td> </td>
</tr>

<tr>
<td>`a / b`</td>
<td>`a / b`</td>
<td> </td>
</tr>

<tr>
<td>`a ** b`</td>
<td>`a ^ b`</td>
<td> </td>
</tr>

<tr>
<td>`a ^ b`</td>
<td>`a ^ b`</td>
<td> </td>
</tr>

<tr>
<td>`a | b`</td>
<td>`OR(a, b)`</td>
<td> </td>
</tr>

<tr>
<td>`a % b`</td>
<td>`MOD(a, b)`</td>
<td> </td>
</tr>

<tr>
<td>`a % a`</td>
<td>`a%`</td>
<td>Notice same object is on each sides</td>
</tr>

<tr>
<td>`~ a`</td>
<td>`NOT(a)`</td>
<td> </td>
</tr>



</tbody>
</table>
</div>

Built-in python functions work as well. **Important** For `sum()`, you
must place your element(s) inside a list, like `sum([my_col, my_row])`.
This is true even if you're only summing one thing: `sum([my_col])`


<div class="output_area rendered_html docutils container">
<table class="dataframe">
<thead>
<tr>
<th>Python</th>
<th>Excel</th>
</tr>
</thead>
<tbody>

<tr>
<td>`sum(a)`</td>
<td>`N/A`</td>
<td>Don't do this. Pass list instead</td>
</tr>

<tr>
<td>`sum([a])`</td>
<td>`SUM(a)`</td>
<td> </td>
</tr>

<tr>
<td>`sum([a, b])`</td>
<td>`SUM(a, b)`</td>
<td> </td>
</tr>

<tr>
<td>`round(a, 2)`</td>
<td>`ROUND(a, 2)`</td>
<td> </td>
</tr>

<tr>
<td>`abs(a)`</td>
<td>`ABS(a)`</td>
<td> </td>
</tr>

<tr>
<td>`math.trunc(a)`</td>
<td>`TRUNC(a)`</td>
<td> </td>
</tr>

<tr>
<td>`math.floor(a)`</td>
<td>`FLOOR(a, 1)`</td>
<td>Excel's floor takes extra param.</td>
</tr>

<tr>
<td>`math.ceil(a)`</td>
<td>`CEILING(a, 1)`</td>
<td>Excel's ceiling takes extra param.</td>
</tr>



</tbody>
</table>
</div>










"""
