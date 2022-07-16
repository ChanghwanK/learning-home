import java.util.Collections

fun main() {
    val listA = listOf<String>("Apple", "Orange")
    val listB = listOf<String>("Apple", "Banana")
    val a = listB - listA
    println(a)
    println(a.javaClass.name)
//    val listC = listOf<String>(listA - listB)
//    println(listC)
}
