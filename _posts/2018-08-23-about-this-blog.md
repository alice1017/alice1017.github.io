---
layout: post
title: このブログについて
tags: [about]
excerpt_separator: <!--more-->
---


# ブログというものについて

2018年8月23日、このブログを作った。
以前[はてなブログ](http://intention.hateblo.jp)の方でブログを書いていたが、数年前にやめた。
そもそもブログを書く目的や書く内容などをあらかじめ決めておらず、ただただ「近況報告用」として書いていたから、
書くことがなくなったらそりゃぁ書かないようになっちゃうという話で。

<!--more-->

## 何故新しくブログを作ったのか

今回ブログを立ち上げた理由は、純粋に「**アウトプットする場が欲しかった**」からだ。
自分は[Qiita](http://qiita.com/alice1017)に記事を書いているが、個人のアウトプット用として書いているわけではなく、
*自分が知っていて、他の誰かに有用かもしれないもの*を書いている。

## 誰に対して書くのか

今回このブログが純粋にアウトプットだけをする場合は、自分の「**備忘録**」という形で
自分をターゲットにして書いていこうと思う。

## である調で書くべきかですます調で書くべきか

ブログを書くにあたって悩むのがこれだ。もう別にである調で書いていい気がする。
でもたまにですます調で書いている時があるから気をつけて二重適用は防ごう。

## このブログのアーキテクチャ

このブログは[Jekyll](https://jekyllrb.com/)で制作しており、
[Type on Strap](https://github.com/sylhare/Type-on-Strap)というテーマを使っている。

### jekyllにした理由

最初ははてなブログで新しくブログを作ろうかと悩んでいたが、最終的にはてなブログはやめた。
一番大きい理由は「**ブログをvimで書きたかった**」だと思う。

vimのキーバインドが体に染み付いている自分としては、オンラインのWYSIWYGエディタでブログを書くのは耐え難い苦痛。
しかしローカルで一度vimで書いてそれをコピペするというやり方も考えたが…冗長だ。

それにはてなブログはデザインの変更がめんどくさい。（個人の意見である）

jekyllは最初から最後まで自分で関われるのが良かった。Github Pagesで公開も簡単にできるし、実際のHTMLやCSSを
いじくり回せる。

### シングルカラム

見ての通りこのブログはシングルカラム。新しくブログを作るにあたって、シングルカラムにするということを最初から決めていた。
もうサイドバーとかいらない。

シングルカラムのメリットは**ユーザーが目移りしない**こと。
サイドバーなどに著者の情報や人気の投稿などが掲載されていると、コンテンツではなくサイドの情報に目移りしてしまうから。

### フォント

このブログでは日本語を表示するのに「**さわらび明朝**」と、「**さわらびゴシック**」を使用している。

![さわらび明朝とさわらびゴシック](http://res.cloudinary.com/dojpz83hh/image/upload/q_auto:good/v1535029031/Blog%20Post%20Images/Google_Fonts.jpg)

見出しは明朝、コンテンツはゴシックに設定している。唯一の難点は、*さわらびゴシックがRegularしかない*ことだった。
なのでstrongタグで囲っても見た目が変わらない。そのため**赤色(#bf1e56)**をつけることにした。

# ブログタイトルについて

上記でも説明したが「アウトプット専用ブログ」として「独白」という単語を使いたかったのと、
このブログではただプログラム系のアウトプットをするのではなく、**自分が感心のあるものすべて**を対象にしたかった。

## 趣味人とは

>しゅみ‐じん【趣味人】<br>
>趣味を生活の一部として楽しむ人。また、趣味を生きがいとする人。<br>
>（デジタル大辞泉より）

自分は、自分が好きな趣味をやっている時間が**一番楽しい時間**である。
仕事のために人生を生きるのではなく、*趣味のために人生を生きる人でありたい*。

## 今の趣味

### プログラミング
主に`Python`を使ってプログラムを書いている。未だに2.7系をつかうジジイである。[Github](http://github.com/alice1017)

### DTM
主にクラブミュージック系の曲をLogic proというソフトで作っている。[SoundCloud](http://soundcloud.com/alice_records)

### 読書
主に哲学系の本が好きで、2018年8月現在は「[その悩み、哲学者がすでに答えを出しています](https://www.amazon.co.jp/%E3%81%9D%E3%81%AE%E6%82%A9%E3%81%BF%E3%80%81%E5%93%B2%E5%AD%A6%E8%80%85%E3%81%8C%E3%81%99%E3%81%A7%E3%81%AB%E7%AD%94%E3%81%88%E3%82%92%E5%87%BA%E3%81%97%E3%81%A6%E3%81%84%E3%81%BE%E3%81%99-%E5%B0%8F%E6%9E%97-%E6%98%8C%E5%B9%B3/dp/4866510056)」という本を読んでいる。
とてもおもしろい本で、哲学初心者に向いていると思う。

### 映画鑑賞
昔からジャッキー・チェンが好きで、アクション映画をよく見る。
日本のジャニーズ系が出てる恋愛モノみたいなやつ以外はたいていなんでも興味があれば見に行く。

映画はもっぱら**一人鑑賞**派である。これについてもいつかブログで書きたい。

### 音楽鑑賞

クラブミュージックからゲームのサウンドトラックまで、なんでも聞くが、演歌は除く。
最近はSpotifyで音楽聴き放題の生活。
クラブミュージックを聞き始めたのは、サカナクションという日本のバンドの曲をラジオで聞いたのがきっかけ。
その後クラブミュージックにハマりDJをやった経験もある。

## 今後やりたい趣味

 - 楽器 - いつかチャレンジしたい。チェロを弾けるようになるのが夢。
 - 海外旅行 - 趣味の範囲に入るのか不明だが、将来お金がたくさん溜まったら世界遺産を見に海外を旅行したい。
 - 囲碁 - 中学時代は囲碁部だった。最近はもっぱらやってないが老後の趣味にとっておく。

## 興味があるモノ・コト

- 哲学 - 哲学は自分の思考の礎を築いてくれるものだ。
- 量子力学 - シュレディンガーの猫とか、二重スリット実験とか、多次元宇宙論とかすごい好き。

# まとめ

疲れた。最後の趣味のあたりからだんだん投げやりになってしまったのが反省点。
三日坊主にならないように、ブログを書くことを習慣付けなくては。
