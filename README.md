Screencast
----------
Emacs 社區錄影集合區，相關說明參考 [仿 sublime 首頁動畫製作 emacs 動畫](https://yfwu.github.io/%E6%8A%80%E8%A1%93/2014/09/03/animated-emacs.html)

## 錄製腳本

```
M-x
"emacs-lisp-mode"
Return
"(message "hello")"
C-x C-e
```

腳本撰寫注意事項

1. 一行可以容納多個組合鍵，如上例中的 ``C-x C-e``
    1. Ctrl: C-
	2. Alt: M-
	3. Shift: S-
	4. Super(Win): 請直接寫 Super+ (不過這個鍵通常用不到)
2. 參數部分請分開兩行，並注意寫上 Return
3. 字串請前後用 ``"`` 包裹

## Repo 結構

```
.
└ screencast
   ├ README.md
   ├ recip
   └ result
```

1. Recipe 放腳本
2. Result 則放輸出成果 (爲資料夾，含輸出圖及時間軸 json)


