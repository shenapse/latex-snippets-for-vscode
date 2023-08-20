# CHEAT SHEET

<style>
.column-left{
  float: left;
  width: 47.5%;
  text-align: left;
}
.column-right{
  float: right;
  width: 47.5%;
  text-align: left;
}
.column-one{
  float: left;
  width: 100%;
  text-align: left;
}
</style>

<div class="column-left">

## Environments

### `\begin \end`

| snippet |                                                     |
| :------ | :-------------------------------------------------- |
| mbeg    | `\begin{} \end{}`                                   |
| eq      | `\begin{equation}`                                  |
| eqv     | `\begin{equation*}`                                 |
| ali     | `\begin{aligned}`                                   |
| gat     | `\begin{gather}`                                    |
| cas     | `\begin{cases}`                                     |
| enm     | `\begin{enumerate}`                                 |
| itz     | `\begin{itemize}`                                   |
| thm     | `\begin{theorem}`                                   |
| prp     | `\begin{proposition}`                               |
| dfn     | `\begin{definition}`                                |
| lem     | `\begin{lemma}`                                     |
| prf     | `\begin{proof}`                                     |
| ex      | `\begin{example}`                                   |
| exe     | `\begin{exercise}`                                  |
| rem     | `\begin{remark}`                                    |
| Mp34xb  | `\begin{pmatrix}` size `3 x 4`, all components `=x` |
| Mb23yb  | `\begin{bmatrix}` size `2 x 3`, all components `=y` |

- Add suffix `v` to get `*` version.
- `Bmatrix`, `vmatrix`, `Vmatrix` are also available.

### Misc

| snippet |                   |
| :------ | :---------------- |
| ;;      | `\(  \)`          |
| x;;     | `\( x \)`         |
| lr)     | `\left(  \right)` |

- `lr` also works for `]`, `>`, `}`, `v`(vert), `V`(Vert).

## Subscripts and Superscripts

|  snippet  |           |
| :-------- | :-------- |
| __        | `_{}`     |
| ^^        | `^{}`     |
| inv       | `^{-1}`   |
| x1        | `x_1`     |
| x23       | `x_{23}`  |
| xNN       | `x_n`     |
| a_ipk     | `a_{i+k}` |
| b_ip1     | `b_{i+1}` |
| a_jmk     | `a_{j-k}` |
| b_jm1     | `b_{j-1}` |
| xJJpk     | `x_{j+k}` |
| x_{i+1}tt | `x^{i+1}` |
| sq        | `^2`      |
| cb        | `^3`      |

## Dots

|  snippet  |                             |
| :-------- | :-------------------------- |
| ..        | `\ldots`                    |
| ,.        | , `\ldots`,                 |
| x_{i+1},, | `x_{i+1}, \\ldots, x_{i+1}` |
| sdd       | `\ddots`                    |
| sdv       | `\vdots`                    |
| dc        | `\cdot`                     |

- sd + \[dvlc\](dot type) -> `\\(dot type)dots`

</div>
<div class="column-right">

## Characters

|   snippet    |                |                |
| :----------- | :------------- | :------------- |
| za           | `\alpha`       | $\alpha$       |
| zG           | `Gamma`        | $\Gamma$       |
| R#           | `\mathbb{R}`   | $\mathbb{R}$   |
| Acal         | `\mathcal{A}`  | $\mathcal{A}$  |
| B@           | `\mathscr{B}`  | $\mathscr{B}$  |
| \mathbb{R}#  | `\mathcal{R}`  |                |
| \mathcal{R}# | `\mathscr{R}`  |                |
| \mathscr{R}# | `\mathbb{R}`   |                |
| \mathbb{Z}+  | `\mathbb{Z}_+` | $\mathbb{Z}_+$ |
| \mathbb{R}*  | `\mathbb{R}^*` | $\mathbb{R}^*$ |

- adding `#` converts `mathbb` -> `mathcal` -> `mathscr` -> `mathbb`

## Math Commands

### Commands with Short Names

For commands of less than or equal to four characters in length, you may assume that their snippets are defined in an obvious way as follows:

| snippet |          |           |
| :------ | :------- | :-------- |
| in      | `\in`    | $\in$     |
| int     | `\int`   | $\int$    |
| notin   | `\notin` | $\notin$  |
| sim     | `\sim`   | $\sim$    |
| simeq   | `\simeq` | $\simeq$  |
| dot     | `\dot`   | $\dot{x}$ |

- more than 50 snippets are defined in this way.

### Commands with Longer Name

| snippet |                   |                   |
| :------ | :---------------- | :---------------- |
| imp     | `\implies`        | $\Rightarrow$     |
| imb     | `\impliedby`      | $\Leftarrow$      |
| ssb     | `\subset`         | $\subset$         |
| ssp     | `\supset`         | $\supset$         |
| stm     | `\setminus`       | $\setminus$       |
| emps    | `\emptyset`       | $\emptyset$       |
| ee      | `\exists`         | $\exists$         |
| fa      | `\forall`         | $\forall$         |
| mpt     | `\mapsto`         | $\mapsto$         |
| uuto    | `\upuparrows`     | $\upuparrows$     |
| ddto    | `\downdownarrows` | $\downdownarrows$ |
| lra     | `\leftrightarrow` | $\leftrightarrow$ |
| Lra     | `\Leftrightarrow` | $\Leftrightarrow$ |
| xto     | `\xrightarrow`    | $\longrightarrow$ |
| xot     | `\xleftarrow`     | $\longleftarrow$  |
| oo      | `\infty`          | $\infty$          |
| asin    | `\arcsin`         | $\arcsin$         |
| app     | `\approx`         | $\approx$         |
| xx      | `\times`          | $\times$          |
| oxx     | `\otimes`         | $\otimes$         |
| o+      | `\oplus`          | $\oplus$          |
| inte    | `\interior`       | $A^{\circ}$        |
| ovl     | `\overline`       | $\overline{x}$    |
| uset    | `\underset`       |                   |
| oset    | `\overset`        |                   |
| ff      | `\frac`           | $\frac{1}{2}$     |
| tit     | `\textit`         |                   |
| tbf     | `\textbf`         |                   |
| mrm     | `\mathrm`         |                   |

### Suggestion

| snippet  |                                |                          |
| :------- | :----------------------------- | :----------------------- |
| \sum _   | `\sum_{i=1}`                   | $\sum_{i=1}$             |
| \prods _ | `\prod_{i=1}`                  | $\prod_{i=1}$            |
| \lim _   | `\lim_{x \to \infty}`          | $\lim_{x \to \infty}$    |
| \sum ^   | `\sum_{i=1}^{\infty}`          | $\sum_{i=1}^{\infty}$    |
| \prods ^ | `\prod_{i=1}^{n}`              | $\prod_{i=1}^{n}$        |
| \to ^    | `\xrightarrow{{x} \to \infty}` |                          |
| \int ^   | `\int_{\infty}^{\infty}`       | $\int_{\infty}^{\infty}$ |

- `_`: modest suggestion
- `^`: aggressive

</div>
