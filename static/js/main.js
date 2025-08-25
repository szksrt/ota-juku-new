// static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    // 必要な要素を取得
    const menu = document.getElementById('menu');
    const menuBtn = document.querySelector('.menu-btn');
    const closeBtn = document.querySelector('.close-btn');
    const body = document.body; // body要素を取得

    // メニューを開く関数
    function openMenu() {
        menu.classList.add('is-open');
        body.classList.add('menu-is-open'); // ← 背景スクロール禁止クラスを追加
    }

    // メニューを閉じる関数
    function closeMenu() {
        menu.classList.remove('is-open');
        body.classList.remove('menu-is-open'); // ← 背景スクロール禁止クラスを削除
    }

    // メニューを開くボタンがクリックされた時の処理
    if (menuBtn) {
        menuBtn.addEventListener('click', openMenu);
    }

    // 閉じるボタンがクリックされた時の処理
    if (closeBtn) {
        closeBtn.addEventListener('click', closeMenu);
    }

    // メニューの背景（外側）がクリックされた時に閉じる処理
    if (menu) {
        menu.addEventListener('click', function(event) {
            // event.target: 実際にクリックされた要素
            // this: イベントリスナーが設定された要素 (この場合はmenu)
            if (event.target === this) {
                closeMenu();
            }
        });
    }
});