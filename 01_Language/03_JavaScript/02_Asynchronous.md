# 비동기
- 동기(Synchronous) VS 비동기(Asynchronous)
- 비동기 : 타이머 설정시에만 잠깐 멈추고 그 뒤에는 CPU가 Idle 상태가 되면서 처리가 가능함
```js
function delay_word(word, delay) {
    return new Promise(resolve => {
        setTimeout(function () {
            resolve(word)
        }, delay)
    })
}
```

## Chaining 처리, Hard Code
```js
delay_word('VAILISH', 500).then((resolve) => {

    colsole.log(resolve)

    delay_word('is', 490).then((resolve) => {

        console.log(resolve)

        delay_word('hardworking', 480).then((resolve) => {

            console.log(resolve)

            delay_word('Developer', 470).then((resolve) => {

                console.log(resolve)
            })
        })
    })
})
```
```js
async function test() {
    const resolve_0 = await delay_word('VAILISH', 500)
    console.log(resolve_0)
    const resolve_1 = await delay_word('is', 490)
    console.log(resolve_1)
    const resolve_2 = await delay_word('hardworking', 480)
    console.log(resolve_2)
    const resolve_3 = await delay_word('Developer', 470)
    console.log(resolve_3)
}
```
- 두 방식 모두 성능의 차이는 없음, 가독성의 차이. 중요한건 일관성!

## Chaining 처리 Soft Code
```js
const array = [{word:'VAILISH', delay:500}, {word:'is', delay:490}
               {word:'hardworking', delay:480}, {word:'developer', delay:470}]

array.reduce((prev, item) => {

  return prev.then(() =>
    delay_word(item.word, item.delay).then((promise) => {console.log(promise)}))

}, Promise.resoleve())
```
```js
const array = [{word:'VAILISH', delay:500}, {word:'is', delay:490}
               {word:'hardworking', delay:480}, {word:'developer', delay:470}]

async function test(){

    for(const item of array) {
        const resolve = await delay_word(item.word, item.delay)

        console.log(resolve)
    }
}
```

## All 처리, 비 순차 결과
- 먼저 끝나는 테스크부터 처리하는 방법
```js
const array = [{word:'VAILISH', delay:500}, {word:'is', delay:490}
               {word:'hardworking', delay:480}, {word:'developer', delay:470}]

array.forEach(async (item) => {

    delay_word(item.word, item.delay).then((resolve) => {console.log(resolve)})
}}
// developer
// hardworking
// is
// VAILISH
```
```js
const array = [{word:'VAILISH', delay:500}, {word:'is', delay:490}
               {word:'hardworking', delay:480}, {word:'developer', delay:470}]

array.forEach(async (item) => {

    const resolve = await delay_word(item.word, item.delay)
    
    console.log(resolve)
}}
// developer
// hardworking
// is
// VAILISH
```

## All 처리, 순차 결과
- 순서대로 처리하는 방법
```js
const array = [{word:'VAILISH', delay:500}, {word:'is', delay:490}
               {word:'hardworking', delay:480}, {word:'developer', delay:470}]

const promise_list = []

array.forEach((item) => {

    const promise = delay_word(item.word, item.delay)
    
    promise_list.push(promise)
}}
Promise.all(promise_list).then((values) => {

    values.forEach((resolve) => {console.log(resolve)})
})
// VAILISH
// is
// hardworking
// developer
```
```js
const array = [{word:'VAILISH', delay:500}, {word:'is', delay:490}
               {word:'hardworking', delay:480}, {word:'developer', delay:470}]

async function test(){

    const async_fun_list = []

    for(item of array){

        const async_fun = delay_word(item.word, item.delay)

        async_fun_list.push(async_fun)
    }

    for(async_fun of async_fun_list){

        const resolve = await async_fun

        console.log(resolve)
    }
}
// VAILISH
// is
// hardworking
// developer
```