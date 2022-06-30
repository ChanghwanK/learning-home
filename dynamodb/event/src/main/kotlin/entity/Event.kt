package entity
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbBean
import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.DynamoDbPartitionKey
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

@DynamoDbBean
data class Event (
    @get:DynamoDbPartitionKey
    var id: String = String(),
    var title: String = String(),
    var createdAt: String = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy/MM/dd:HH"))
) {
    init {
        id = "${this.id}-${this.createdAt}".lowercase()
    }
    companion object {
        fun toEntity(id: String, title: String): Event {
            return Event(id,title)
        }
    }
}