package day01

import readInput
import java.lang.Integer.max

fun main() {
    fun part1(input: List<String>): Int {
        var maxVal = 0
        var temp = 0
        for (num: String in input) {
            if (num != "") {
                temp += num.toInt()
            } else {
                maxVal = max(temp, maxVal)
                temp = 0
            }
        }
        return maxVal
    }

    fun part2(input: List<String>): Int {
        val calorieList = mutableListOf<Int>()
        var temp = 0
        for (num: String in input) {
            if (num != "") {
                temp += num.toInt()
            } else {
                calorieList.add(temp)
                temp = 0
            }
        }
        calorieList.sortDescending()
        return calorieList.take(3).sum()
    }

    val input = readInput("day01/Day01")
    println("Part 1 Solution: ${part1(input)}")
    println("Part 2 Solution: ${part2(input)}")
}
