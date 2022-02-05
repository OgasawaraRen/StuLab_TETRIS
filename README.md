### 実行方法
1. cdコマンドでRev_Tetrisディレクトリに移動
2. Rev_Tetrisフォルダ内のvenvをアクティベートする(Game内で使用するpygameやnumpyは添付したvenv内にインストール済み)
3. ターミナルにて「python App.py」を実行  

※ライブラリ・仮想環境の問題で実行できない場合はpygameとnumpyをインストールした環境で、
Rev_Tetrisディレクトリ内で「python App.py」を実行してください

### ルール
1. ミノを積み重ねボードの最上位に到達するとクリアとなる.
2. ミノの動作仕様には右左の90度回転、左右移動、急降下がある.
3. トラップマス(赤いマス)上に置くか、横一列揃えたゲームオーバーとなる.
4. Kキーでホールドが使用可能.  
  ホールド・・・落ちてくるミノをストックでき任意のタイミングで取り出す事ができる.  
  ホールドした場合、ミノを設置するまで再度ホールドはできない。
5. ゲーム終了後に盤面占有率でスコアが表示される.

### 操作方法
下記のキー入力にて操作する  

|キー|動作|
|:-:|:-|
|A |  左に1マス移動|
|D |  右に1マス移動|
|W |  急降下|
|S |  1マス落下|
|J |  左に90°回転|
|L |  右に90°回転|
|K |  ホールド|
