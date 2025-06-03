document.addEventListener('DOMContentLoaded', () => {
    // 要素の取得
    const timeDisplay = document.getElementById('time');
    const startBtn = document.getElementById('startBtn');
    const pauseBtn = document.getElementById('pauseBtn');
    const resetBtn = document.getElementById('resetBtn');
    const modeButtons = document.querySelectorAll('.mode-btn');
    const cycleDisplay = document.getElementById('cycle');
    
    // 変数の初期化
    let timeLeft = 25 * 60; // 25分を秒で表現
    let timerId = null;
    let isRunning = false;
    let isWorkMode = true;
    let cycles = 0;
    
    // 時間表示を更新する関数
    function updateDisplay() {
        const minutes = Math.floor(timeLeft / 60);
        const seconds = timeLeft % 60;
        timeDisplay.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }
    
    // タイマーを開始する関数
    function startTimer() {
        if (isRunning) return;
        
        isRunning = true;
        startBtn.disabled = true;
        pauseBtn.disabled = false;
        
        timerId = setInterval(() => {
            timeLeft--;
            updateDisplay();
            
            if (timeLeft <= 0) {
                clearInterval(timerId);
                isRunning = false;
                
                // 作業モードと休憩モードを切り替え
                if (isWorkMode) {
                    cycles++;
                    cycleDisplay.textContent = cycles;
                    
                    // 4サイクルごとに長い休憩
                    const isLongBreak = cycles % 4 === 0;
                    const breakMinutes = isLongBreak ? 15 : 5;
                    
                    if (confirm(`お疲れ様でした！${isLongBreak ? '15分の長い休憩' : '5分の休憩'}を始めますか？`)) {
                        timeLeft = breakMinutes * 60;
                        updateMode(false);
                        startTimer();
                    }
                } else {
                    // 休憩終了後、作業モードに戻る
                    if (confirm('休憩時間が終了しました。作業を再開しますか？')) {
                        timeLeft = 25 * 60;
                        updateMode(true);
                        startTimer();
                    }
                }
            }
        }, 1000);
    }
    
    // タイマーを一時停止する関数
    function pauseTimer() {
        clearInterval(timerId);
        isRunning = false;
        startBtn.disabled = false;
        pauseBtn.disabled = true;
    }
    
    // タイマーをリセットする関数
    function resetTimer() {
        clearInterval(timerId);
        isRunning = false;
        startBtn.disabled = false;
        pauseBtn.disabled = true;
        
        // 現在のモードに応じて時間をリセット
        timeLeft = isWorkMode ? 25 * 60 : 5 * 60;
        updateDisplay();
    }
    
    // モードを更新する関数
    function updateMode(workMode) {
        isWorkMode = workMode;
        modeButtons.forEach(btn => {
            const minutes = parseInt(btn.dataset.minutes);
            btn.classList.toggle('active', (workMode && minutes === 25) || (!workMode && minutes === 5));
        });
    }
    
    // イベントリスナーの設定
    startBtn.addEventListener('click', startTimer);
    pauseBtn.addEventListener('click', pauseTimer);
    resetBtn.addEventListener('click', resetTimer);
    
    modeButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            if (isRunning) return;
            
            const minutes = parseInt(btn.dataset.minutes);
            timeLeft = minutes * 60;
            updateDisplay();
            updateMode(minutes === 25);
        });
    });
    
    // 初期表示を更新
    updateDisplay();
});
