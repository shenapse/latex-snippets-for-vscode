# Snippets Reference

This document is a collection of descriptions for dynamic snippets.
It is not comprehensive but (I think) is sufficient to understand the behavior of non-trivial dynamic snippets.

- [Snippets Reference](#snippets-reference)
  - [Characters](#characters)
    - [letter to `\mathxxx{}`](#letter-to-mathxxx)
    - [conversion among `\mathxxx{}`](#conversion-among-mathxxx)
    - [alphabet to Greek letter](#alphabet-to-greek-letter)
  - [Subscripts and Superscripts](#subscripts-and-superscripts)
    - [auto-subscript (digit)](#auto-subscript-digit)
    - [auto-subscript (lower case alphabet)](#auto-subscript-lower-case-alphabet)
    - [modification of subscript](#modification-of-subscript)
    - [conversion between subscript and superscript](#conversion-between-subscript-and-superscript)
  - [Dots](#dots)
    - [repeat with ldots](#repeat-with-ldots)
  - [Math Commands](#math-commands)

## Characters

### letter to `\mathxxx{}`

- Trigger: an uppercase alphabet (A, for instance) + operator(# or 'cal' or @)
- Output: `\mathbb{A}`, `\mathcal{A}`, `\mathscr{A}`, resp
- Example:
  - `R#` -> `\mathbb{R}`
  - `Acal` -> `\mathcal{A}`
  - `B@` -> `\mathscr{B}`

### conversion among `\mathxxx{}`

- Trigger: `\mathxxx{}` + #
- Output: `\mathbb` -> `\mathcal` -> `\mathscr` -> `\mathbb`
- Example: `\mathbb{A}#` -> `\mathcal{A}`

### alphabet to Greek letter

- Trigger: z + an alphabet
- Output: corresponding greek letter
- Examples:
  - `za` -> `\alpha`
  - `zG` -> `\Gamma`

## Subscripts and Superscripts

### auto-subscript (digit)

- Trigger: (a letter or a command) + (digits of length <= 2)
- Output: letter or command with that subscript
- Examples:
  - `x1` -> `x_1`
  - `\ell23` -> `\ell_{23}`

### auto-subscript (lower case alphabet)

- Trigger: (X: a letter or a command) + (an uppercase alphabet)×2
- Output: X subscripted by the lowercase alphabet
- Examples:
  - `xNN` -> `x_n`
  - `qKK` -> `q_k`

### modification of subscript

- Trigger: (a letter or a command with a subscript of depth 1) + (operator "p" or "m") + (value: a lowercase alphabet or a digit)
- Output: add plus or minus value to the subscript
- Examples:
  - `x_kp1` -> `x_{k+1}`
  - `C_{m}mk` -> `C_{m-k}`

### conversion between subscript and superscript

- Trigger: (a letter or a command with either a subscript or a superscript of depth 1) + tt
- Output: subscript(superscript) is turned to superscript(subscript, resp)
- Example: `A^{\ell+1}tt` -> `A_{\ell+1}`, and conversely.

## Dots

### repeat with ldots

- Trigger: (single term not containing a space but space-separated with other terms) + (double comma,,)
- Output: repeat the same term after ", ...,"
- Examples
  - `A_{i_1}^{j_1}`,, -> `A_{i_1}^{j_1}, \ldots, A_{i_1}^{j_1}`
  - `\ell\ell_{i_1}^{j_1},,` does not work as they are not properly separated.

## Math Commands

This category includes numerous snippets. For instance, triggers `le`, `ge`, `div`, `to`, `not`, `in`, `sup`, `inf`, `dim`, `deg`, `ker`, `range`, `grad`, `rot`, `Div`, `rank`, `diag`, `det`, `arg`, `max`, `min`, `argmax`, `argmin`, `sin`, `cos`, `tan`, `cot`, `ln`, `log`, `exp`, `perp`, `cup`, `cap`, `sim`, `pm`, `iff`, `mid`, `Im`, `Re`, `succ`, `prec`, `circ`, `neq`, `ni`, `lim`, `sum`, `prod`, `const`, are defined for their commands (e.g., `le` -> `\le`).

Moreover, those snippets that begin with `not` and `in` as well as those end with `eq`, `neq` are defined in this way. This category includes `notin`, `simeq`, `subsetneq` etc. (More precisely, the trigger for `\simeq` is defined as `\sim` + eq, not `simeq`. The same is true for the other members.) `supp` also belongs to this category for similar reason.

There are also a number of abbreviated commands, for instance, `emps` for `\emptyset`, `oo` for `\infty`, and `o+` for `\oplus` and so on.
The cheat sheet has the (nearly?) complete list for the abbreviated, but the best way to get accurate information is to go to definition of snippets, which is always up-to-date.
