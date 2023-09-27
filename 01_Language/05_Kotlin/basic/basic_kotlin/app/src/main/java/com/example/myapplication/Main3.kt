package com.example.myapplication

fun main() {
    val dog: Animal = Dog()
    val cat = Cat()

    if (dog is Dog) {
        println("멍뭉")
    }
}

abstract class Animal { 
    open fun move() { // 코틀린은 상속받을때 기본적으로 오버라이드 불가 open으로 열어줘야함
        println("이동")
    }
}

class Dog : Animal(), Drawable {
    override  fun move() {
        println("껑충")
    }

    override fun draw() {
        TODO("Not yet implemented")
    }
}

class Cat : Animal(), Drawable {
    override fun move() {
        println("살금")
    }

    override fun draw() {
        TODO("Not yet implemented")
    }
}

// 일반 클래스 상속도 막혀있음, 사용하려면 얘도 open 해줘야함
open class Girl
class SuperGirl : Girl()

interface Drawable {
    fun draw()
}
