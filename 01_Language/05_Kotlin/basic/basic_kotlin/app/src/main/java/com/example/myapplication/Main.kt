package com.example.myapplication

import java.util.Scanner
import kotlin.math.max
import kotlin.random.Random

const val num =- 1

fun main() {
//    test1()
//    test2()
//    test3()
//    test4()
//    test5()
    println(sum(b=29, a=1))
}


fun test1() {
    println("Hello Word")
    var age : Int = 10
    var name : String = "James"

    println(age.toString() + " ~V~ " + name)

    var age2 : Long = 20L
    age = age2.toInt()
    age2 = age.toLong()

    println(name.uppercase())
    println(name.lowercase())

    println(name[2])
    println("나이는 $age 이름은 ${name}이다.")

    var numA : Int = 50
    var numB : Int = 100
    println(max(numA, numB))

    val randomNum = Random.nextInt()
    val randomNum2 = Random.nextInt(0, 100)
    println("$randomNum $randomNum2")

    val reader = Scanner(System.`in`)
    println(reader.nextInt())
}

fun test2() {
    var i = 50
    print("${i}는 ")
    if (i > 30) {
        println("30보다 크다")
    } else if (i > 10) {
        println("10보다 크다")
    } else
        println("10보다 작다")

    var j = 11
    print("${j}는 ")
    when {
        j > 30 -> {
            println("30보다 크다")
        }
        j > 10 -> {
            println("10보다 크다")
        }
        else -> {
            println("10보다 작다")
        }
    }

    var k = 6
    var result = if (k > 30) {
        "30보다 크다"
    } else if (k > 10) {
        "10보다 크다"
    } else
        "10보다 작다"
    print("${k}는 $result")
}

fun test3() {
    var i = 29
    var check = if (i > 30) true else false
    println(check)

    var items = listOf(1, 2, 3, 4, 5)

    for (item in items) {
        println(item)
    }

    items.forEach { item ->
        println(item)
    }

    for ((index, item) in items.withIndex()) {
        println(item)
    }

    for (i in 0..(items.size-1)) {
        print(items[i])
    }
}

fun test4() {
    val items = mutableListOf(1, 2, 3, 4, 5, 4, 3, 2, 1)

    items.add(6)
    items.remove(1)

    println(items)

    val items2 = arrayOf(1, 2, 3, 4, 5)
    items2[4] = 50

    println(items2)

    try {
        items[99]
    } catch (e: Exception) {
        print(e.message)
    }
}

fun test5() {
    var name : String? = null
    name = "ㅇㅅㅇ"
    name = null
    println(name)

    var name2 : String = ""
    println(name==name2) // String과 String?는 타입이 다르므로 변환해서 처리해줘야함
//    name2 = name!! // 강제로 넣어줄 수 있으나 문제생기면 개발자책임이므로 적합하지 않음

    name?.let { println("null이 아니라면 블록을 실행하자.") }
}

fun sum(a: Int, b: Int, c: Int=0) = a + b + c

