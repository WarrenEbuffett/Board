window.addEventListener('DOMContentLoaded', () => {
    const imageSets = document.querySelectorAll('.image-set');
    let current = 0;
  
    function showNextSet() {
      // 현재 보이는 것 숨기기
      imageSets[current].classList.remove('active');
  
      // 다음 index 계산
      current = (current + 1) % imageSets.length;
  
      // 다음 이미지셋 보이기
      imageSets[current].classList.add('active');
    }
  
    // 최초 1개만 보이게
    imageSets[current].classList.add('active');
  
    // 2초마다 이미지 전환
    setInterval(showNextSet, 2000);
  });
  