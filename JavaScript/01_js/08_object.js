const myInfo = {
  name: 'jack',
  phoneNumber: '123456',
  'samsung product': {
    buds: 'Buds pro',
    galaxy: 'S99',
  },
}

console.log(myInfo.name)
console.log(myInfo['name'])

console.log(myInfo['samsung product'])  // 띄어쓰기가 있으니까 .으로 접근 불가
console.log(myInfo['samsung product'].galaxy)


const obj = {
  name: 'jack',
  greeting() {
    console.log('hi!')
  }
}
console.log(obj.name)
console.log(obj.greeting())


const key = 'country'  // 바꾸면 아래 key 값이 바뀜
const value = ['한국', '미국', '일본', '중국']

const myObj = {
  [key]: value,
}

console.log(myObj)
console.log(myObj.country)

//구조 분해 할당 !!중요!!



const jsonData = {
  coffee: 'Americano',
  iceCream: 'Mint Choco',
}

// Object -> json
const objToJson = JSON.stringify(jsonData)

console.log(objToJson)  // {"coffee":"Americano","iceCream":"Mint Choco"}

console.log(typeof objToJson)  // string

// json -> Object
const jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj)
console.log(typeof jsonToObj)  // object
console.log(jsonToObj.coffee)  // Americano


// 앞에  괄호로 시작하는 것은 좋은 코드가 아님, 거기다 세미콜론;을 안쓰기로 했으므로 문제가 생기는 경우가 있음
// arr = [1, 2, 3, 4, 5]
// foo()
// arr.forEach(...)

// 아래의 경우는 하나의 코드로 인식해서 ;가 있어야만 함 아니면 하나로 인식, 그러니까 변수 할당해서 쓰자
// foo()
// [1, 2, 3, 4, 5].forEach(...)