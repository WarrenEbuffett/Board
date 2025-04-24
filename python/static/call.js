
/* Jquery없는 순수 자바 스크립트 */


/*
document.addEventListener() : document(웹 문서)에 이벤트 리스너를 추가함.
DOMContentLoaded : HTML 문서가 모두 로드된 후 실행되는 이벤트(JS내장 이벤트).
function () {...} : 이벤트가 발생하면 실행할 코드 블록.
*/
document.addEventListener("DOMContentLoaded", function () {
    let profileCard = document.querySelector(".profile-card");//class="profile-card"인 요소를 찾아서 변수에 저장하는 코드.
    profileCard.style.opacity = "0"; // profileCard요소의 CSS로 요소의 투명도를 0으로 설정하여 완전히 숨김.

    setTimeout(() => { //setTimeout() : 일정 시간이 지난 후 특정 코드를 실행하는 JavaScript 내장 함수.//{ ... } : 이후 실행할 코드(콜백 함수).
        profileCard.style.transition = "opacity 1s ease-in-out";
        profileCard.style.opacity = "1"; // 1초 동안 부드럽게 나타남
    }, 0); // 0초 후 바로 실행
});

//transition : CSS속성이 변할때 부드럽게 에니메이션 효과를 주는 속성.기본적으로 CSS는 속성 값이 바뀌면 즉시 적용되지만 transition을 사용하면 일정 시간동안 서서히 변하도록 설정할수있다
//"DOMContentLoaded"는 웹 페이지의 DOM(Document Object Model)이 모두 로드되었을 때 발생하는 이벤트다.
//이벤트 리스너(event listener)란? 특정 이벤트가 발생할 때 자동으로 실행할 함수를 지정하는 것.