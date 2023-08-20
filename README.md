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

## Demos

Each demo shows keystrokes and the result of the input.
For simplicity <kbd>Tab</kbd> is represented by "|", which is frequently used to jump to the next tab stop.
The point is that we apply various conversions to (a part of) preceding text instead of inputting pre-registered texts. As a result, most input is done without <kbd>Enter</kbd> and <kbd>←↑→↓</kbd>.

Throughout demos, E represents <kbd>Enter</kbd>, and braces `{}` are not typed in reality. They are inserted in order to visualize word breaks that are otherwise difficult to see.

demo 1:

`Let U{;;}|be an open subset of {;;}{R#}|.CE A function {;;}f:U to {R#}|is said to be {tit}contnuous at|{;;}{x0}|if for any {;;}{ze}>0|there is {;;}{zd}>0|such that {eqv}{E}{abs}x-x0|<{zd}{imp}{abs}f(x→-f(x0→<{ze}|.`<kbd>Ctrl+S</kbd>, where C represents <kbd>Ctrl</kbd>.

![demo 1][demo-continuity]

demo 2:

`Let {;;}e1{,,}{D}n|be a basis of a vector space V{;;}|and let ;;{lr)}{f1}{tt}{,,}{D}n|be the...`, where D represents <kbd>Delete</kbd>.

![demo 2][demo-dual-basis]

demo 3:

`{eqv}{E}{exp}x= {sum}{_}{n}|||{xNN}{tt}|/n!|{\\}{E}={lim} {_}{n}|| {lr)}1+x/n|{^^}n`<kbd>Ctrl+S</kbd>.

![demo 3][demo-taylor-expansion]

demo 4:

`;;V {oxx}W {sim}{eq}W {oxx}V|.{E}Indeed, the map ;;V {oxx}W {ni}(x,y→{mpt}(y,x→{in}W {oxx}V| is...`.

![demo 4][demo-tensor-isomorphism]

## Usage and Examples

This repository provides two different types of snippets: static one ([latex.code-snippets][my-code-snippets]) and dynamic one ([latex.hsnips][my-hsnips]).
The emphasis is on the latter.

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

In this section, we begin with the concept of "context" provided by HyperSnips Extension.
(Technically, it is an array of strings provided through vscode-textmate library.)
Its benefit and limitation are very important to know since it plays a fundamental role in determining the domain of dynamic snippets.

For the usage of dynamic snippets, we refer to the [cheat sheet][cheatsheet] and [snippets reference][my-reference]. If you encounter snippets that are not defined in de facto latex packages, [commands.sty][my-commands] would be your help.

If you want a hands-on experience, I suggest you try to reproduce the above demos yourself. It's the essence of dynamic snippets in a nutshell. The tex file for this exercise is available at [demo directory.](./demo/)

#### Math Context

HyperSnips Extension provides "context", which we use to tell our snippets whether cursor is within a math environment (such as `\(x\)`, `\[ \]` and `\begin-\end{equation}`) or not.
Triggers for dynamic snippets for math are defined to get active only when we are in a math environment. Here is a demo. The point is that the word "to" is converted to `\to` only when it is typed within a math environment.

![demo-math-context][demo-math-context]

More than 99% of our dynamic snippets are for math. So you may reasonably assume that dynamic snippets are designed to be used like this, but there are trivial exceptions:

- globally active dynamic snippets
  - `;;` for inline math mode `\( \)`
  - `tit` and `tbf` for `\textit{}` and `\textbf{}`

A dynamic snippet for `$x$` is intentionally not defined. In fact, `$` based math environments can have a confusing context, and can cause unintended behavior; for instance, "to" is converted into `to` outside the math environment (really annoying)! For this reason, I gave it up at least for the current version. (If you are interested, read my comments for `math(context)` function in latex.hsnips file.)

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
% great readability!
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

If you might want to turn off other snippets, for instance, those provided by LaTeX Workshop Extension, then [Control Snippets][control-snip-ext] is useful.

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

[latex-setup]:<https://github.com/gruvw/latex-setup>
[latex-snippets]:https://github.com/Einlar/latex_snippets
[hsnip-ext]:<https://marketplace.visualstudio.com/items?itemName=draivin.hsnips>
[page-snippets-in-vscode]:https://code.visualstudio.com/docs/editor/userdefinedsnippets
[control-snip-ext]:https://marketplace.visualstudio.com/items?itemName=svipas.control-snippets
[envs]:./sty/envs.sty

[my-commands]:./sty/commands.sty
[my-utf-command]:./sty/commands_UTF.sty
[utf-hsnips]:./.vscode/utf_latex.hsnips
