package day03

import readInput

fun main() {
    fun part1(input: List<String>): Int {
        var total = 0

        for (string: String in input) {
            val first = string.take(string.length/2).toList()
            val second = string.takeLast(string.length/2).toList()
            val intersect = first.intersect(second.toSet())
            total += if (intersect.first() in 'a'..'z') {
                Character.getNumericValue(intersect.first()) - 9
            } else {
                Character.getNumericValue(intersect.first()) - 9 + 26
            }
        }
        return total
    }

    fun part2(input: List<String>): Int {
        var total = 0

        for (i in 0..input.size-2 step 3) {
            val first = input[i].toList()
            val second = input[i+1].toList()
            val third = input[i+2].toList()
            val intersect = first.intersect(second.toSet()).intersect(third.toSet())
            total += if (intersect.first() in 'a'..'z') {
                Character.getNumericValue(intersect.first()) - 9
            } else {
                Character.getNumericValue(intersect.first()) - 9 + 26
            }
        }
        return total
    }

    val input = readInput("day03/Day03")
    println("Part 1 Solution: ${part1(input)}")
    println("Part 2 Solution: ${part2(input)}")
}
