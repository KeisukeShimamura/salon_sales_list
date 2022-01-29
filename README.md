# サロン営業リスト管理ソフト
## 概要
* いろんなサイトからサロンの情報や、掲載している求人情報などをスクレイピングする
  * HOT PAPPER BEAUTY
  * リクエストQJ
  * リジョブ
  * etc..
* スクレイピングした情報を突合して１つにまとめる
  * どこに掲載されているかなども持たせる
* 機械学習でデータ分析する
  * 教師なし学習。営業成約率の高いサロンを分類する
    * いろんな媒体を使っているか？
    * 店舗拡大しようとしているか？
    * 上記などを判定して採用に困っているサロンを判定

## 開発
### スクレイピング
#### 開発環境構築
* 仮想環境構築

```
conda create -n salon_sales_list_env python=3.8
conda activate salon_sales_list_env
pip install scrapy
conda install beautifulsoup4
```

* scrapy作成
```
scrapy startproject scraping
```


### 突合
### データ分析
