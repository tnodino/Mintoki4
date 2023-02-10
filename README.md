# 00_Clear input and output.bat
このバッチを起動すると input, output ファイルを一度削除して、新しく空のフォルダを作り直します。

# 01_Testcase generator.bat
seed.txt にシード値を書き込んでこのバッチを起動すると、seed.txt に対応したテストケースが input フォルダに作られます。
0 ~ 99 のテストケースが既に input フォルダに作られています。

# 02_Make an output.bat
main.py にコードを書き込んでこのバッチを起動すると、input フォルダにあるテストケースを main.py で実行し、output フォルダに出力します。