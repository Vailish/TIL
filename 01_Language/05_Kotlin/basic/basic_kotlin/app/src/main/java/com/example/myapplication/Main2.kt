package com.example.myapplication

fun main() {
    val peter = Person("Peter", 20)
    println(peter.name)
    println(peter.age)

//    peter.name = "ㅇㅁㅇ"  // 안되는 이유는 val -> var val만 사용해서 getter setter 효과 볼 수 있음
    
    val tomas = Person2("tomas", 25)
//    println(tomas.name)  // private으로 막아서 불가

    val peter2 = Person("peter", 20)
    println(peter == peter2)  // 해쉬코드 재정의하면 가능 혹은 date class사용하면 가능
    
//    peter2.hobby // private set으로인해 접근 불가
}

//class Person(val name: String, var age: Int,)
data class Person(val name: String, var age: Int,)

class Person2(
    private val name: String,
    var age: Int,
) {
    var hobby = "축구"
        private set
        get() = "ㅇㅅㅇ : $field" // 이런식으로 getter 재정의 가능
    init {
        println("생성 완료!")
    }

    fun changeHobby() {
        hobby = "야구"
    }

}

