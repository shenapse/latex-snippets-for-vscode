# LaTeX Snippets for VSCode

ここにある Snippets は

- [latex setup](https://github.com/gruvw/latex-setup)
- [Latex Snippets for Visual Studio Code](https://github.com/Einlar/latex_snippets)

の亜種なので, まずはそちらを確認されたい.

## .code-snippets

`latex.code-snippets` はプロジェクトディレクトリにスコープを持つユーザー定義の Snippets.
<kbd><kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd></kbd> -> Configure User Snippets でアクセスできるグローバルな Snippets (たとえば, tex.json ) と同様に書かれ, スコープを除いて同様に動作する. `.tex` ファイルだけでなく `.sty` ファイルにも効くっぽい. プロジェクトの .vscode フォルダに置く.
詳しくは [Snippets in Visual Studio Code](https://code.visualstudio.com/docs/editor/userdefinedsnippets) 参照.

## .hsnips

`latex.hsnips` は [Hypersnips Extension](https://marketplace.visualstudio.com/items?itemName=draivin.hsnips) の設定ファイル.
<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> -> HyperSnips: Open Snippet file -> `latex.hsnips` にコピペで `.tex` ファイルに対してグローバルに有効になる. ローカルに定義する方法は拡張機能の Usage に書いてある.

ここにある Snippets は冒頭に挙げたうちの前者を元に手を加えたもの.
Snippets の中で使用されている定理環境やマクロはユーザーが適宜定義する必要があるものも含まれ得る.

Hypersnips の Usage にある通り, LaTex Workshop Extension に定義されたスニペットと衝突する場合があるので, 必要に応じて [Control Snippets](https://marketplace.visualstudio.com/items?itemName=svipas.control-snippets) でスニペットのON/OFFを調整すること.

## Cheat Sheet for Snippets

最新版とは限らないけど, それなりに頼りになる[チートシート Notion](https://www.notion.so/shena46/TeX-Cheat-Sheet-in-VS-Code-084f26ccfb8a4a1ea38e95e82190c817). これを書く中の人が管理している.
