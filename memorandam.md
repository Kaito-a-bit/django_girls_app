初めての djangoアプリ作成
---

・djangoの概要  
`makemigrations`→利用できるモデルを全て確認し、まだ作成されていないテーブルを作るためのマイグレーションを生成する。  
`migrate`→マイグレーションを実行し、実際にデータベースにテーブルを作成する。  
Djangoではマイグレーションでモデルの変更を保存する。  

・開発用サーバの起動  
`python manage.py runserver`: **`manage.py`ファイルがあるディレクトリで行うことに注意**  
アクセスするURLは [http://127.0.0.1:8000/ ](http://127.0.0.1:8000/ )

---

`view`には`url`に紐付けが必要でそれを行うのは`URLconf`

・モデルの変更手順  
 - `models.py`からモデルを変更
 - これらの変更のためのマイグレーションを作成するために`python manage.py makemigrations`を実行
 - データベースにこれらの変更を適用するために`python manage.py migrate`を実行
