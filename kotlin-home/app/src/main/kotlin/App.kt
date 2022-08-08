import java.io.File
import java.io.InputStream
import java.time.LocalDate
import java.time.LocalDateTime
import java.time.ZonedDateTime
import java.time.format.DateTimeFormatter
import java.util.Collections

fun main() {
    val date = "2022-08-01"
    val date2 = "2022-08-02"

    val parsed1 = LocalDate.parse(date, DateTimeFormatter.ISO_DATE)
    val parsed2 = LocalDate.parse(date2, DateTimeFormatter.ISO_DATE)

    if (parsed1.isAfter(parsed2)) {
        println("$date is after $date2")
    } else {
        println("$date is before $date2")
    }
}

inline
