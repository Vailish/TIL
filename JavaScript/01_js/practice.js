// console.log('hello, javascript')

// 이런식으로 선언하는 식은 호이스팅이 발생하므로 표현식이 더 바람직함.
// function add(num1, num2) {
//     return num1 + num2
// }
// console.log(add(2, 7))


// 함수 표현식
// const sub = function (num1, num2) {
//   return num1 - num2
// }
// console.log(sub(7, 2))


// 디버깅용
// const mySub = function namedSub(num1, num2) {
//     return num1 - num2
// }

// console.log(mySub(1, 2))
// console.log(namedSub(1, 2))


// const greeting = function (name = 'Anonmous') {
//     return `Hi ${name}`
// }
// console.log(greeting())


// 파라미터 개수보다 초과 되어도 상관 없이 출력됨
// const noArgs = function () {
//     return 0
// }
// console.log(noArgs(1, 2, 3, 4, 5))


// 파라미터 개수보다 적어도 undefined로 출력됨
// const threeArgs = function (arg1, arg2, arg3) {
//     return [arg1, arg2, arg3]
// }

// console.log(threeArgs(1))


// Spread syntax 전개구문
// const restOpr = function (arg1, arg2, ...restArgs) {
//     return [arg1, arg2, restArgs]
// }

// console.log(restOpr(1, 2, 3, 4, 5))
// console.log(restOpr(1, 2))


// Arrow Function(화살표 함수), 표현식에서만 가능
// Airbnb에서는 1단계 혹은 3단계로 하고, 3단계의 경우 인자에 ()쳐주는 걸 권장함

// const greeting = function (name) {return `Hi ${name}`}
// console.log(greeting())

// // 1단계
// const greeting = (name) => {return `Hi ${name}`}

// // 2단계
// const greeting = name => {return `Hi ${name}`}

// // 3단계
// const greeting = name => `Hi ${name}`

// 인자가 없다면 () 혹은 _로 표시가능
// let noArgs = () => 'No args'
// noArgs = _ => 'No args'

// // object를 return 할 경우 return 명시적으로 적어줘야 함
// let returnObject = () => { return { key: 'value'} }
// // return을 적지 않으려면 괄호를 붙여야 함
// returnObject = () => ({ Key: 'value' })

// 즉시 실행 함수 : 일회성 함수
// (function(num) { return num ** 3 })(2)
// (num => num ** 3)(2)


// Array 배열

const numbers = [1, 2, 3, 4, 5]
console.log(numbers[0])
console.log(numbers[-1])
console.log(numbers.length)
console.log(numbers[numbers.length - 1])

numbers.reverse()
console.log(numbers)

numbers.push(100)
console.log(numbers)

numbers.pop()
console.log(numbers)

console.log(numbers.includes(1))
console.log(numbers.includes(100))

console.log(numbers.indexOf(3))
console.log(numbers.indexOf(100))

console.log(numbers.join())
console.log(numbers.join(''))
console.log(numbers.join(' '))
console.log(numbers.join('-'))