import http from "k6/http" // http test

export let options = {
    vus: 50,          // 가상의 유저 수
    duration: '1m'   // 테스트 진행 시간
};

export default function () {

    let getUrl = "http://localhost:8000/users";

    http.get(getUrl);
}
