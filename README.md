# Overview

This repository provides a much more efficient method to input LaTeX code in VSCode compared to traditional user-snippets-based input method.

This repository is a kind of extension of preceding works [latex-setup][latex-setup] and [Latex Snippets for Visual Studio Code][latex-snippets]. We utilize the [Hypersnips Extension for VSCode][hsnip-ext] to introduce "dynamic" snippets in addition to traditional VSCode user snippets. It provides a faster way of inputting routine commands, such as `\alpha`, `\mathbb{R}`, `x_1, \\ldots, x_n` and `\lim_{n \to \infty}`, as the demos below show.

- In what sense is it efficient? It is
  - intelligent in that it understands "context", i.e., whether you are in a math environment or not
  - flexible and powerful in that it works with RegExp and JavaScript
  - faster because it converts texts automatically without any interaction
  - not annoying because it does not flood your input suggestion

This repository owes much to the preceding works cited above. In fact, many snippets are borrowed from them, often with slight modification. My work is summarized as:

- Relative feature of this repository:
  - Extended [latex.hsnips][my-hsnips]
  - Supplementary style files: [commands.sty][my-commands], [env.sty][envs]
  - Well-organized [Markdown Cheat Sheet][cheatsheet] and [Reference][my-reference]
  - Experimental [utf dynamic snippets][utf-hsnips] and corresponding [commands_UTF.sty][my-utf-command]

Most of what follows can also be read in [my Japanese article][my-japanese-article].

## Demos

Each demo shows keystrokes and the result of the input.
For simplicity <kbd>Tab</kbd> is represented by "|", which is frequently used to jump to the next tab stop.
The point is that we apply various conversions to (a part of) preceding text instead of inputting pre-registered texts. As a result, most input is done without <kbd>Enter</kbd> and <kbd>←↑→↓</kbd>.

Throughout demos, E represents <kbd>Enter</kbd>, and braces `{}` are not typed in reality. They are inserted in order to visualize word breaks that are otherwise difficult to see.

### demo 1: definition of continuous real function

`Let U{;;}|be an open subset of {;;}{R#}|.CE A function {;;}f:U to {R#}|is said to be {tit}contnuous at|{;;}{x0}|if for any {;;}{ze}>0|there is {;;}{zd}>0|such that {eqv}{E}{abs}x-x0|<{zd}{imp}{abs}f(x→-f(x0→<{ze}|.`<kbd>Ctrl+S</kbd>, where C represents <kbd>Ctrl</kbd>.

![demo 1][demo-continuity]
![demo-continuity-png][demo-continuity-png]

- `U{;;}` at the beginning becomes `\( U \)`. Here `;;` is a function that puts the preceding term into an inline math and puts the cursor next to it. In contrast, `;;` just before `R#` creates an empty inline math but puts the cursor inside it. In this way, the same string of snippet can be defined to behave differently in different situations.
- `R#` turns into `\mathbb{R}`. Here `#` is a function that assigns, to each uppercase alphabet, the corresponding black board character.
- `x0` turns into `x_0`. In this situation, `0`(more precisely, the digits of length <= 2) is a function that equips digit(s) itself to an input.
- `ze` becomes `\epsilon`. In this case, `z` is a function that assigns, to each alphabet, the corresponding Greek letter.
- `eqv` is an ordinary VSCode user-snippets, and the only non-dynamic snippet appearing in our demos, which is defined to be a shortcut for non-numbered equation environment.

Note that the word "to" in `A function {;;}f:U to {R#}|` is converted to `\to` but not in "is said to be", as expected.

### demo 2: dual basis

`Let {;;}e1{,,}{D}n|be a basis of a vector space V{;;}|and let ;;{lr)}{f1}{tt}{,,}{D}n|be the...`, where D represents <kbd>Delete</kbd>.

![demo 2][demo-dual-basis]
![demo-dual-basis-png][demo-dual-basis-png]

- `e1` turns into `e_1` as before. The two consecutive commas `,,` is a function that repeats the preceding term with `, \ldots,`. The output is `e_1, \ldots, e_1`.
- `lr` is a function and `)` is its argument. `lr)` returns the `\left \right` version of the input. So, in this case, it outputs `\left( \right)`.
- `tt` acting on `f_1` is, of course, a function that turns subscript into superscript (and the inverse of `tt` is `tt` itself). We get `f^1` from `f_1tt`.

### demo 3: Taylor expansion of exponential function

`{eqv}{E}{exp}x= {sum}{_}{n}|||{xNN}{tt}|/n!|{\\}{E}={lim} {_}{n}|| {lr)}1+x/n|{^^}n`<kbd>Ctrl+S</kbd>.

![demo 3][demo-taylor-expansion]
![demo-taylor-expansion-png][demo-taylor-expansion-png]

- Commands with short names such as `\exp` and `\sum` have obvious snippets, i.e., `exp` and `sum`.
- `^` just after `\sum` is a "suggestion" function that auto-completes a typical content that follows. Its default behavior for `\sum` is to suggest `_{i=1}^{\infty}`. So, we have `\sum_{i=1}^{\infty}`. Similarly, `_` for `\lim` is also a suggestion function.
- `xNN` is a friend of `x0`, in that `NN` is a function that equips its lowercase subscript to an input.
- Even `/` is a function, that returns the `\frac` whose numerator is the preceding term.
- Finally, `^^` turns into `^{}`. Note that `^` does not behave as a suggestion function since the preceding term does not belong to the family who wants a suggestion. Instead, it acts simply like a shortcut for `^{}`.

### demo 4: Tensor isomorphism

`;;V {oxx}W {sim}{eq}W {oxx}V|.{E}Indeed, the map ;;V {oxx}W {ni}(x,y→{mpt}(y,x→{in}W {oxx}V| is...`.

![demo 4][demo-tensor-isomorphism]
![demo-tensor-isomorphism-png][demo-tensor-isomorphism-png]

- `sim` turns into `\sim`, and then `\sim eq` rewrites `\sim` to `\simeq`. `eq` is a rewrite function that adds the suffix "eq" to the preceding commands if it thinks it should. We have many rewrite functions other than `eq`, such as `neq` and `in`.

## Snippets Overview

This repository provides two different types of snippets: static one ([latex.code-snippets][my-code-snippets]) and dynamic one ([latex.hsnips][my-hsnips]).
Our emphasis is on the latter.

|         |    Trigger     |        Interactition        |            Output            | Defined by  |
| :-----: | :------------: | :-------------------------: | :--------------------------: | :---------: |
| Static  |      Text      | Yes<br>(Suggestion to user) |       Registered Text        |    JSON     |
| Dynamic | Context & Text |   No<br>(Auto conversion)   | Transformation of Input Text | RegExp & JS |

### Static Snippets

The static snippets are just typical VSCode snippets. It consists of snippets for `\begin \end` style math environments, such as `\begin{equation}` and `\begin{proof}`. They can be used everywhere on a tex file.
If you skim through the first section of the cheat sheets and then try some commands such as `eq`, `eqv`, `gat`,`gatv`, you'll know how to use it.

For instance,
`cas` gets you the suggestion for `\begin{cases} \end{cases}`.
The "v"ed version `casv` gives you the non-numbered cases `\begin{cases*} \end{cases*}`. Here, `v` means "void". The suffix `v` works similarly for other `\begin-\end` style environments.

One thing to note here about static snippet is that defined snippets `thm`, `dfn` and `prf` etc. do not yield `\begin{theorem}`, `\begin{definition}` and `\begin{proof}` etc. Actually, it yields ALIASes for them such as `\begin{thm}`, `\begin{dfn}` and `\begin{prf}` defined in [envs.sty][envs]. They are expected to be customized according to user preferences, but may of course be used as is.

### Dynamic Snippets

For the practical usage of our dynamic snippets, we refer to the [cheat sheet][cheatsheet] and [snippets reference][my-reference]. If you encounter snippets that are not defined in de facto latex packages, [commands.sty][my-commands] would be your help.

If you want a hands-on experience, I suggest you try to reproduce the above demos yourself. It's the essence of dynamic snippets in a nutshell. [The demo directory](./demo/) contains a tex file for this exercise.

#### Math Context

HyperSnips Extension provides "context", which we use to tell our snippets whether cursor is within a math environment (such as `\(x\)`, `\[ \]` and `\begin-\end{equation}`) or not.
(Technically, it is an array of strings provided through vscode-textmate library.)
Its benefit and limitation are very important to know since it plays a fundamental role in determining the domain of dynamic snippets.

Triggers for dynamic snippets for math are defined to get active only when we are in a math environment. Here is a demo. The point is that the word "to" is converted to `\to` only when it is typed within a math environment.

![demo-math-context][demo-math-context]

More than 99% of our dynamic snippets are for math. So you may reasonably assume that dynamic snippets are designed to be used like this, but there are trivial exceptions:

- globally active dynamic snippets
  - `;;` for inline math mode `\( \)`
  - `tit` and `tbf` for `\textit{}` and `\textbf{}`

A dynamic snippet for `$ $` is intentionally not defined. More importantly, our dynamic snippets (more precisely, the function `math(context)` in our latex.hsnips) does not recognize `$` based inline math as a math environment. In other words, `$` math inline is not supported. This is not just because `\( \)` is recommended instead of `$`. In fact, `$` based math environments can have a confusing context, and allowing it can cause unintended behavior; for instance, "to" is converted into `\to` outside math environment, which is really annoying. For this reason, I gave it up at least for the current version. (If you are interested, read my comments for `math(context)` function in latex.hsnips file.)

#### Experimental: UTF Snippets and Commands

This subsection might be safely skipped. We wrote the following code in demo 4:

```tex
% demo 4: tensor isomorphism
\( V \otimes W \simeq W \otimes V \).
Indeed, the map \( V \otimes W \ni x \otimes y \mapsto y \otimes x \in W \otimes V \) is an isomorphism.
```

If we allow ourselves to use UTF character in a command name (this is possible, for instance, with LuaLaTeX and XeLaTeX), then UTF version would look like:

```tex
% demo 4 UTF version
% PC browser might fail to render this 
\( V \⊗ W \≃ W \otimes V \).
Indeed, the map \( V \⊗ W \∋ x \⊗ y \↦ y \⊗ x \∈ W \⊗ V \) is an isomorphism.
```

But how can we input the characters like `⊗` and `≃` in some reasonable way?
Just use [utf_latex.hsnips][utf-hsnips] and [commands_UTF.sty][my-utf-command]. They contain snippets for UTF commands and the definition of UTF commands.

We can use many UTF snippets by the simple rule "utf trigger = u + traditional trigger". For instance, `uoxx` -> `\⊗`, `uin` -> `\∈`, but `ueqsim`
-> `\≃` (an exception since we have `simeq` -> $\simeq$). As they are experimental, there are many problems to be solved, such as coverage of UTF characters, consistency of snippets names, and integrability with traditional tools etc. I introduced it here out of curiosity that some readers might be interested in UTF latex coding.

## Install

For static snippets [latex.code-snippets][my-code-snippets], see [Snippets in Visual Studio Code][page-snippets-in-vscode].
It can be installed locally and globally.

For dynamic snippets [latex.hsnips][my-hsnips], see [Hypersnips Extension][hsnip-ext]. UTF snippets are enabled just by adding its functions to a properly placed [latex.hsnips][my-hsnips]. (Remember [commands_UTF.sty][my-utf-command] if you compile UTF commands!)

You might want to turn off other snippets, for instance, those provided by LaTeX Workshop Extension. Then [Control Snippets][control-snip-ext] is useful.

## Contribution

This repository was born as a byproduct of my TeX writing. My main objective has been "write faster". It makes snippets tend to be written for practical convenience rather than perfection, with the excuse that assumed use is limited to a pure interactive process (latex coding) and the risk of bugs is small. This resulted in a lot of code that needed to be fixed.
So suggestion for improvements (whether in the direction of perfection or practical convenience) are REALLY welcome.

## References

- [latex-setup][latex-setup]
- [latex-snippets][latex-snippets]
- [HyperSnips Extension][hsnip-ext]
- [page-snippets-in-vscode][page-snippets-in-vscode]
- [control-snip-ext][control-snip-ext]

[my-hsnips]:./.vscode/latex.hsnips
[my-code-snippets]:./.vscode/latex.code-snippets
[cheatsheet]:./cheatsheet.md
[my-reference]:./snippets-reference.md
[demo-continuity]:https://user-images.githubusercontent.com/87386937/261810044-f974ba47-6877-4e17-a7f3-d3a8a1bb02a8.gif
[demo-dual-basis]:https://user-images.githubusercontent.com/87386937/261810046-91c2cadb-f1db-46d1-908b-179645a450f0.gif
[demo-taylor-expansion]:https://user-images.githubusercontent.com/87386937/261810040-cddb9673-fdda-4377-bf32-b30680cd2cd4.gif
[demo-tensor-isomorphism]:https://user-images.githubusercontent.com/87386937/261844955-016a1701-2755-4122-9fd5-ce86fcf53e51.gif
[demo-math-context]:https://user-images.githubusercontent.com/87386937/261810049-c75e86d4-3d4a-4764-98b0-ac1282a3b992.gif
[demo-continuity-png]:./demo/demo-continuity.png
[demo-dual-basis-png]:./demo/demo-dual-basis.png
[demo-taylor-expansion-png]:./demo/demo-taylor-expansion.png
[demo-tensor-isomorphism-png]:./demo/demo-tensor-isomorphism.png

[latex-setup]:<https://github.com/gruvw/latex-setup>
[latex-snippets]:https://github.com/Einlar/latex_snippets
[hsnip-ext]:<https://marketplace.visualstudio.com/items?itemName=draivin.hsnips>
[page-snippets-in-vscode]:https://code.visualstudio.com/docs/editor/userdefinedsnippets
[control-snip-ext]:https://marketplace.visualstudio.com/items?itemName=svipas.control-snippets
[envs]:./sty/envs.sty

[my-commands]:./sty/commands.sty
[my-utf-command]:./sty/commands_UTF.sty
[utf-hsnips]:./.vscode/utf_latex.hsnips
[my-japanese-article]:https://zenn.dev/shena46/articles/latex-snippets-vscode
