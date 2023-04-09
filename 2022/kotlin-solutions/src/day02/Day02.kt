package day02

import readInput

fun main() {
    fun part1(input: List<String>): Int {
        val initScore = mapOf("X" to 1, "Y" to 2, "Z" to 3)
        val draw = mapOf("X" to "A", "Y" to "B", "Z" to "C")
        val win = mapOf("X" to "C", "Y" to "A", "Z" to "B")
        var total = 0

        for (turn: String in input) {
            val new = turn.split(" ")
            total += initScore[new[1]]!!
            total += if (win[new[1]] == new[0]) 6 else if (draw[new[1]] == new[0]) 3 else 0
        }
        return total
    }

    fun part2(input: List<String>): Int {
        val cond = mapOf("X" to 0, "Y" to 3, "Z" to 6)
        val score = mapOf("A" to 1, "B" to 2, "C" to 3)
        val toWin = mapOf("A" to "B", "B" to "C", "C" to "A")
        val toLose = mapOf("A" to "C", "B" to "A", "C" to "B")
        var total = 0

        for (turn: String in input) {
            val new = turn.split(" ")
            total += cond[new[1]]!!
            total += if (new[1] == "Y") {
                score[new[0]]!!
            } else if (new[1] == "Z") {
                score[toWin[new[0]]]!!
            } else {
                score[toLose[new[0]]]!!
            }
        }
        return total
    }

    val input = readInput("day02/Day02")
    println("Part 1 Solution: ${part1(input)}")
    println("Part 2 Solution: ${part2(input)}")
}
