package com.example.myapplication

fun main() {
    myFunc { print("함수 호출") }
    myFunc2(10) { print("함수 호출") }
}

fun myFunc(callBack : () -> Unit) {
    println("함수 시작!!!")
    callBack()
    println("함수 끝!!!")
}

fun myFunc2(a: Int, callBack : () -> Unit) {
    println("함수 시작!!!")
    callBack()
    println("함수 끝!!!")
}