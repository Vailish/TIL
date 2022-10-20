const numbers = [90, 80, 70, 100]

// 총합
// result 첫번째 인자에 누적값이 들어감, 함수 뒤의 인자는 첫 인자(result)의 초기값
const sumNum = numbers.reduce(function (result, number) {
  return result + number
}, 0)

console.log(sumNum)

const sumNum = numbers.reduce((result, number) => {
//   console.log(result)
    return result + number
}, 0)

const avgNum = numbers.reduce((result, number) => result + number, 0) / numbers.length