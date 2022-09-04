package entity

import software.amazon.awssdk.enhanced.dynamodb.mapper.annotations.*
import java.time.ZoneId
import java.time.ZonedDateTime
import java.time.format.DateTimeFormatter

@DynamoDbBean
data class Event(
    @get:DynamoDbPartitionKey
    var id: String = String(),
    @get:DynamoDbSortKey
    @get:DynamoDbAttribute("order")
    var order: String = String(),
    @get:DynamoDbSecondaryPartitionKey(indexNames = ["eventName-index"])
    var eventName: String = String(),
    var title: String = String(),
    var createdAt: String = ZonedDateTime.now(ZoneId.of("Asia/Seoul")).plusDays(1)
        .format(DateTimeFormatter.ofPattern("yyyy-MM-dd"))
) {
    companion object {
        fun toEntity(id: String, order: String, eventName: String, title: String): Event {
            return Event(id, order, eventName, title)
        }
    }
}