# 함수형 프로그래밍과 JAVASCRIPT ES6+

평가
  - 코드가 계산 되어 값을 만드는 것

일급
  - 값으로 다룰 수 있다.
  - 변수에 담을 수 있다.
  - 함수의 인자로 사용될 수 있다.
  - 함수의 결과로 사용될 수 있다.

```js
const a = 10; // 일급
const addA = a => a + 10; // 일급
addA(a); // 일급
```

일급 함수
  - 함수를 값으로 다룰 수 있따.

```js
const add5 = a => a + 5;
console.log(add5);;
console.log(add5(5));

const f1 = () => () => 1; // 함수가 함수를 반환하는 일급 함수.
console.log(f1());

const f2 = f1(); // 함수가 변수에 할당된다.
console.log(f2()); // 출력된다.
```

함수를 인자로 받아서 실행하는 함수
  - apply1
  - times

```js
const apply1 = f => f(1);
const add2 = a => a + 2;

apply1(add2);

// 이러면 apply1에서 add2 함수를 인자로받아 실행한다.
// apply1(add2(1)); 이렇게 실행된다.

const times = (f, n) => {
  let i = -1;
  while (++i < n) f(i);
};

// times에서 안에있는 함수가 실행된다.
```

함수를 만들어서 리턴하는 함수 (클로저를 만들어 리턴한다)
  - addMaker

```js
const addMaker = a => b => a + b;
const add10 = addMaker(10);

// b => a + b; 라는 함수가 리턴된다
// a에 10이 할당된 상태 (클로저 내부의 A가 할당된다)
console.log(add10(5)); // 15
console.log(add10(10)); // 20
```

